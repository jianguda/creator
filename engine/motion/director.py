from engine.common import Action, Chain, Normal


class Director:
    def __init__(self):
        self.actions0 = [[
            Action('neck', 1, 25, Chain.HARD),
            Action('left_arm', 1, 15, Chain.HARD),
            Action('right_arm', -1, 15, Chain.HARD),
        ], [
            Action('belly', -1, 15, Chain.HARD),
            Action('left_arm', -1, 15, Chain.HARD),
            Action('right_arm', 1, 15, Chain.HARD),
        ], [
            Action('belly', -1, 15, Chain.HARD),
            Action('left_leg', 1, 15, Chain.SOFT),
            Action('right_leg', -1, 15, Chain.SOFT),
        ], [
            Action('neck', -1, 25, Chain.HARD),
            Action('left_foot', 1, 15, Chain.SOFT),
            Action('left_leg', -1, 15, Chain.HARD),
            Action('right_foot', -1, 15, Chain.SOFT),
            Action('right_leg', 1, 15, Chain.HARD),
        ], [
            Action('belly', 1, 15, Chain.HARD),
            Action('left_foot', -1, 15, Chain.SOFT),
            Action('right_foot', 1, 15, Chain.SOFT),
        ], [
            Action('belly', 1, 15, Chain.HARD),
            Action('left_foot', 1, 15, Chain.SOFT),
            Action('right_foot', -1, 15, Chain.SOFT),
        ], [
            Action('neck', -1, 25, Chain.HARD),
            Action('left_arm', 1, 15, Chain.HARD),
            Action('right_arm', -1, 15, Chain.HARD),
        ], [
            Action('belly', 1, 15, Chain.HARD),
            Action('left_arm', -1, 15, Chain.HARD),
            Action('right_arm', 1, 15, Chain.HARD),
        ], [
            Action('belly', 1, 15, Chain.HARD),
            Action('left_leg', 1, 15, Chain.SOFT),
            Action('right_leg', -1, 15, Chain.SOFT),
        ], [
            Action('neck', 1, 25, Chain.HARD),
            Action('left_foot', 1, 15, Chain.SOFT),
            Action('left_leg', -1, 15, Chain.HARD),
            Action('right_foot', -1, 15, Chain.SOFT),
            Action('right_leg', 1, 15, Chain.HARD),
        ], [
            Action('belly', -1, 15, Chain.HARD),
            Action('left_foot', -1, 15, Chain.SOFT),
            Action('right_foot', 1, 15, Chain.SOFT),
        ], [
            Action('belly', -1, 15, Chain.HARD),
            Action('left_foot', 1, 15, Chain.SOFT),
            Action('right_foot', -1, 15, Chain.SOFT),
        ]]
        self.actions1 = [[
            Action('neck', -2, 30, Chain.HARD),
            Action('left_arm', 2, 30, Chain.SOFT),
            Action('right_arm', -2, 30, Chain.SOFT),
            Action('left_leg', -4, 60, Chain.SOFT),
            Action('left_leg', 4, 60, Chain.SOFT, Normal.Y),
        ], [
            Action('neck', 2, 30, Chain.HARD),
            Action('left_arm', 2, 30, Chain.SOFT),
            Action('right_arm', -2, 30, Chain.SOFT),
            Action('left_foot', -4, 60, Chain.HARD),
            Action('left_foot', 4, 60, Chain.HARD, Normal.Y),
        ], [
            Action('neck', 2, 30, Chain.HARD),
            Action('left_hand', -2, 30, Chain.SOFT),
            Action('left_arm', -2, 30, Chain.HARD),
            Action('right_hand', 2, 30, Chain.SOFT),
            Action('right_arm', 2, 30, Chain.HARD),
            Action('left_leg', -4, 60, Chain.HARD, Normal.Y),
            Action('left_leg', 4, 60, Chain.HARD),
        ], [
            Action('neck', -2, 30, Chain.HARD),
            Action('left_hand', -2, 30, Chain.SOFT),
            Action('left_arm', -2, 30, Chain.HARD),
            Action('right_hand', 2, 30, Chain.SOFT),
            Action('right_arm', 2, 30, Chain.HARD),
            Action('right_leg', 4, 60, Chain.SOFT),
            Action('right_leg', -4, 60, Chain.SOFT, Normal.Y),
        ], [
            Action('neck', -2, 30, Chain.HARD),
            Action('left_hand', 2, 30, Chain.SOFT),
            Action('right_hand', -2, 30, Chain.SOFT),
            Action('right_foot', 4, 60, Chain.HARD),
            Action('right_foot', -4, 60, Chain.HARD, Normal.Y),
        ], [
            Action('neck', 2, 30, Chain.HARD),
            Action('left_hand', 2, 30, Chain.SOFT),
            Action('right_hand', -2, 30, Chain.SOFT),
            Action('right_leg', 4, 60, Chain.HARD, Normal.Y),
            Action('right_leg', -4, 60, Chain.HARD),
        ]]
        self.actions2 = [[
            Action('chest', 1, 20, Chain.HARD),
            Action('butt', -1, 20, Chain.HARD),
            Action('right_hand', -3, 60, Chain.SOFT),
        ], [
            Action('chest', -1, 20, Chain.HARD),
            Action('butt', 1, 20, Chain.HARD),
            Action('right_hand', 3, 60, Chain.SOFT),
        ], [
            Action('chest', -1, 20, Chain.HARD),
            Action('butt', 1, 20, Chain.HARD),
            Action('left_hand', 3, 60, Chain.SOFT),
        ], [
            Action('chest', 1, 20, Chain.HARD),
            Action('butt', -1, 20, Chain.HARD),
            Action('left_hand', -3, 60, Chain.SOFT),
        ], [
            Action('chest', 1, 20, Chain.HARD),
            Action('butt', -1, 20, Chain.HARD),
            Action('left_hand', -3, 60, Chain.SOFT),
        ], [
            Action('chest', -1, 20, Chain.HARD),
            Action('butt', 1, 20, Chain.HARD),
            Action('left_hand', 3, 60, Chain.SOFT),
        ], [
            Action('chest', -1, 20, Chain.HARD),
            Action('butt', 1, 20, Chain.HARD),
            Action('right_hand', 3, 60, Chain.SOFT),
        ], [
            Action('chest', 1, 20, Chain.HARD),
            Action('butt', -1, 20, Chain.HARD),
            Action('right_hand', -3, 60, Chain.SOFT),
        ]]
        self.actions3 = [[
            Action('neck', 1, 15, Chain.HARD),
            Action('chest', 1, 15, Chain.SOFT),
            Action('left_leg', 1, 15, Chain.HARD),
            Action('left_foot', -1, 15, Chain.HARD),
            Action('left_hand', -3, 45, Chain.HARD),
            Action('right_hand', 3, 45, Chain.HARD),
            Action('left_arm', 2, 30, Chain.SOFT),
            Action('right_arm', -2, 30, Chain.SOFT),
        ], [
            Action('neck', -1, 15, Chain.HARD),
            Action('chest', -1, 15, Chain.SOFT),
            Action('left_foot', 1, 15, Chain.HARD),
            Action('left_hand', -3, 45, Chain.HARD),
            Action('right_hand', 3, 45, Chain.HARD),
            Action('left_arm', 2, 30, Chain.SOFT),
            Action('right_arm', -2, 30, Chain.SOFT),
        ], [
            Action('neck', -1, 15, Chain.HARD),
            Action('chest', -1, 15, Chain.SOFT),
            Action('right_leg', -1, 15, Chain.HARD),
            Action('right_foot', 1, 15, Chain.HARD),
            Action('left_hand', -2, 30, Chain.HARD),
            Action('right_hand', 2, 30, Chain.HARD),
            Action('left_arm', 2, 30, Chain.SOFT),
            Action('right_arm', -2, 30, Chain.SOFT),
        ], [
            Action('neck', 1, 15, Chain.HARD),
            Action('chest', 1, 15, Chain.SOFT),
            Action('right_foot', -1, 15, Chain.HARD),
            Action('left_hand', -2, 30, Chain.HARD),
            Action('right_hand', 2, 30, Chain.HARD),
            Action('left_arm', 2, 30, Chain.SOFT),
            Action('right_arm', -2, 30, Chain.SOFT),
        ], [
            Action('left_arm', -3, 45, Chain.HARD, Normal.X),
            Action('right_arm', -3, 45, Chain.HARD, Normal.X),
        ]]

    def direct(self):
        return self.actions0 + self.actions1 + self.actions2 + self.actions3
