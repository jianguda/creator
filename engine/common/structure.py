import binascii

from .category import Chain, Normal


class Area:
    def __init__(self, w=0, h=0):
        self.w = w
        self.h = h


class Dot:
    # x: coord
    # y: coord
    # z: coord
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Dot(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Dot(self.x - other.x, self.y - other.y, self.z - other.z)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __hash__(self):
        return binascii.crc32(f'X{self.x}Y{self.y}Z{self.z}'.encode())

    def __str__(self):
        return f'#X{self.x}#Y{self.y}#Z{self.z}'


class Link:
    # major: idx
    # minor: idx
    def __init__(self, major, minor):
        self.major = major
        self.minor = minor

    def __str__(self):
        return f'#Major{self.major} #Minor{self.minor}'


class Action:
    def __init__(self, tag, step, reach, chain=Chain.SOFT, normal=Normal.Z):
        self.tag = tag
        self.step = step
        self.reach = reach
        self.chain = chain
        self.normal = normal


class Pose:
    def __init__(self, tag, dot, speed=1):
        self.tag = tag
        self.dot = dot
        # speed, not duration
        self.speed = speed
