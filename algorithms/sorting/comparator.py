# https://www.hackerrank.com/challenges/ctci-comparator-sorting

from functools import cmp_to_key


class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return str(self.score) + " " + str(self.name)

    @staticmethod
    def comparator(a, b):
        if a.score > b.score:
            return -1
        elif a.score < b.score:
            return 1
        # they are equal, relative sorting here
        else:
            if a.name > b.name:
                return 1
            elif a.name < b.name:
                return -1
            return 0


if __name__ == "__main__":
    data = [
        Player("amy", 100),
        Player("david", 100),
        Player("heraldo", 50),
        Player("aakansha", 75),
        Player("aleksa", 150)
    ]

    data = sorted(data, key=cmp_to_key(Player.comparator))

    for i in data:
        print(i.name, i.score)
