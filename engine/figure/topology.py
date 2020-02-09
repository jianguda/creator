from queue import Queue

from engine.common.structure import Link
from engine.motion.movement import Motion


class Topology:
    def __init__(self, template, area):
        self.tag = template.tag
        self.scale = template.scale
        self.offset = template.offset
        self.joint = template.joint
        self.skeleton = template.skeleton

        # collection of Dots
        self.dots = list()
        # graph of Dots
        self.links = dict()
        # degrees
        self.degrees = list()
        # powers
        self.powers = list()
        # swings
        self.swings = dict()

        # fill self.dots and self.links
        self.dot2idx = dict()
        for key, value in self.skeleton.items():
            for dot in value:
                if dot not in self.dots:
                    idx = len(self.dots)
                    self.dot2idx.setdefault(dot, idx)
                    self.dots.append(dot)
                    self.links.setdefault(idx, set())
        for key, values in self.skeleton.items():
            values = [self.dot2idx.get(value) for value in values]
            size = len(values)
            for idx in range(size - 1):
                curr_value = values[idx]
                next_value = values[idx + 1]
                self.links.get(curr_value).add(next_value)
                self.links.get(next_value).add(curr_value)
        # compute degrees of dots
        self.degrees = [-1] * len(self.dots)
        for key, values in self.links.items():
            self.degrees[key] = len(values)
        # compute powers of dots
        self.powers = [-1] * len(self.dots)
        powers_dict = dict()
        queue = Queue()
        for key, values in self.links.items():
            power = len(values)
            if power <= 1:
                self.powers[key] = power
            else:
                queue.put(key)
        while not queue.empty():
            item = queue.get()
            values = [self.powers[link] for link in self.links.get(item)]
            values = list(filter(lambda tt: tt > 0, values))
            if values:
                power = min(values) + 1
                self.powers[item] = power
                powers_dict.setdefault(power, list())
                powers_dict.get(power).append(item)
            else:
                queue.put(item)
        # clean powers of dots
        for values in list(powers_dict.values()) + list(powers_dict.values())[::-1]:
            for value in values:
                self.powers[value] = min(self.powers[link] for link in self.links.get(value)) + 1
        # collect swings
        for key, value in self.joint.items():
            minor_idx = self.dot2idx.get(value)
            links = list(self.links.get(minor_idx))
            powers = [self.powers[link] for link in links]
            major_idx = links[powers.index(max(powers))]
            self.swings.setdefault(key, Link(major_idx, minor_idx))
        # update coordinates of dots
        for dot in self.dots:
            dot.x = (dot.x + self.offset.x) * self.scale + area.w // 2
            dot.y = (dot.y + self.offset.y) * self.scale + area.h // 2
        # motion
        self.motion = Motion(self.dots, self.links, self.swings)

    def draw(self, fn):
        fn.text(0, 0, self.tag, 3)
        for key, values in self.links.items():
            major_dot = self.dots[key]

            # fn.pix(major_dot.x, major_dot.y, 2)
            fn.circ(major_dot.x, major_dot.y, 1, 2)
            fn.circ(major_dot.x, major_dot.z // 2, 1, 2)
            fn.circ(major_dot.z // 2, major_dot.y, 1, 2)
            fn.text(major_dot.x + 2, major_dot.y + 2, str(key), 4)
            # fn.text(major_dot.x + 2, major_dot.y + 8, str(self.degrees[key]), 5)
            # fn.text(major_dot.x + 2, major_dot.y + 8, str(self.powers[key]), 5)
            for value in values:
                minor_dot = self.dots[value]
                fn.line(major_dot.x, major_dot.y, minor_dot.x, minor_dot.y, 1)

    def show(self):
        self.motion.perform()
