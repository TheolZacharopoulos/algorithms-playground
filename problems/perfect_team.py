"""
Students: n
Each student skilled in on subject
Subjects: p, c, m, b, z
A team:
- Group of five different students
- Each student is skilled in different subject
- One student is not part of any other team

TODO: Find number of teams.
"""

class Team:
    def __init__(self):
        self.members = []

    def is_complete(self):
        return 'p' in self.members and \
               'c' in self.members and \
               'm' in self.members and \
               'b' in self.members and \
               'z' in self.members

    def add_member(self, skill):
        if skill in self.members:
            return False
        else:
            self.members.append(skill)
            return True


def differentTeams(skills):
    teams = []
    skills = list(skills)

    while True:
        team = Team()

        i = 0
        while True:
            if i == len(skills):
                break
            if team.add_member(skills[i]):
                skills.pop(i)
                i -= 1
            i += 1

        if team.is_complete():
            teams.append(team)
        else:
            break

    return len(teams)


if __name__ == '__main__':
    sk = "pcmpcmbbbzz"
    # sk = "pcmpp"
    print(differentTeams(sk))
