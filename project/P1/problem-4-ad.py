class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    output = False

    # check if user is already in group
    for u in group.get_users():
        if u == user:
            return True

    # if user not in group, maybe he's inside our subgroup?
    for g in group.get_groups():
        if is_user_in_group(user, g):
            return True

    # if all else fails, return false
    return output

# TEST


"""
Group Structure:

    Parent
    |--Child1
    |  `--+--SubChild11
    |     `--SubChild12
    |
    `--Child2
       `--+--SubChild21
"""

# Groups
parent = Group("parent")

child1 = Group("child1")
sub_child11 = Group("subchild11")
sub_child12 = Group("subchild12")

child2 = Group("child2")
sub_child21 = Group("subchild21")

parent.add_user('parent_user_1')
parent.add_user('parent_user_2')

parent.add_group(child1)
child1.add_user('child1_user_1')
child1.add_user('child1_user_2')

parent.add_group(child2)
child2.add_user('child2_user_1')
child2.add_user('child2_user_2')

child1.add_group(sub_child11)
sub_child11.add_user('sub_child11_user_1')
sub_child11.add_user('sub_child11_user_2')

child1.add_group(sub_child12)
sub_child12.add_user('sub_child12_user_1')
sub_child12.add_user('sub_child12_user_2')

child2.add_group(sub_child21)
sub_child21.add_user('sub_child21_user_1')
sub_child21.add_user('sub_child21_user_2')


# Parent1 in Parent
print("Pass" if is_user_in_group('parent_user_1', parent) else "Fail")

# Child1_1 in Parent
print("Pass" if is_user_in_group('child1_user_1', parent) else "Fail")

# SubChild11_2 in Parent
print("Pass" if is_user_in_group('sub_child11_user_2', parent) else "Fail")

# Subchild21_2 in Child1
print("Pass" if not is_user_in_group('sub_child21_user_2', child1) else "Fail")

# Subchild11_1 in Child2
print("Pass" if not is_user_in_group('sub_child11_user_1', child2) else "Fail")
