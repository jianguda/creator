import math
from queue import Queue
from collections import defaultdict

from engine.common import Dot, Chain, Normal
from .director import Director


class Motion:
    def __init__(self, dots, links, swings):
        # collection of Dots
        self.dots = dots
        # graph of Dots
        self.links = links
        # swings
        self.swings = swings

        self.actions = Director().direct()
        self.trigger = 0
        self.checks = defaultdict(lambda: True)

    def perform(self):
        if self.trigger < len(self.actions):
            action = self.actions[self.trigger]
            for idx, move in enumerate(action):
                if self.checks[idx]:
                    self.checks[idx] = self.operate(move)
            checker = True
            for check in self.checks.values():
                checker = checker and not check
            if checker:
                self.trigger += 1
                self.checks = defaultdict(lambda: True)

    def operate(self, move):
        if move.tag:
            self.rotate(move.tag, move.step, move.chain, move.normal)
        move.reach -= abs(move.step)
        return move.reach >= 0

    def p3d(self, vector, normal, sin_t, cos_t):
        if normal is Normal.X:
            yox = vector.y * cos_t - vector.z * sin_t
            zox = vector.z * cos_t + vector.y * sin_t
            return Dot(vector.x, yox, zox)
        elif normal is Normal.Y:
            xoy = vector.x * cos_t - vector.z * sin_t
            zoy = vector.z * cos_t + vector.x * sin_t
            return Dot(xoy, vector.y, zoy)
        elif normal is Normal.Z:
            xoz = vector.x * cos_t - vector.y * sin_t
            yoz = vector.y * cos_t + vector.x * sin_t
            return Dot(xoz, yoz, vector.z)

    def rotate(self, tag, theta, chain, normal):
        swing = self.swings.get(tag)
        sin_t = math.sin(math.radians(theta))
        cos_t = math.cos(math.radians(theta))
        major = self.dots[swing.major]
        minor = self.dots[swing.minor]
        vector = minor - major
        delta = self.p3d(vector, normal, sin_t, cos_t) - vector
        self.dots[swing.minor] = minor + delta

        taboo_list = list()
        taboo_list.append(swing.major)
        queue = Queue()
        queue.put(swing.minor)
        while not queue.empty():
            item = queue.get()
            taboo_list.append(item)
            for link in self.links.get(item):
                if link not in taboo_list:
                    queue.put(link)
                    if chain is Chain.SOFT:
                        self.dots[link] += delta
                    elif chain is Chain.HARD:
                        tmp_dot = self.dots[link]
                        vector = tmp_dot - major
                        delta = self.p3d(vector, normal, sin_t, cos_t) - vector
                        self.dots[link] = tmp_dot + delta
