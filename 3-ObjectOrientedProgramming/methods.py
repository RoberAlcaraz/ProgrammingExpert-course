class Group:
    def __init__(self, name, members=[]):
        self.name = name
        self.members = members

    def add(self, name):
        self.members.append(name)

    def delete(self, name):
        if name in self.members:
            self.members.remove(name)
        else:
            raise Exception("Member not in group.")

    def get_members(self):
        return sorted(self.members)

    def merge(self, another_group):
        return Group(self.name, self.members + another_group.members)


group6 = Group("group6", ["A", "D"])
group7 = Group("group7", ["B", "C"])
merged_group = group6.merge(group7)

print(merged_group)
print(merged_group.get_members())
