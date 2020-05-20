import random

# This function allows input of the number of players
def playercount():
    while True:
        try:
            players = int(input("Please enter the number of players: "))
            print("You have selected", players, "players")
            if players < 6:
                print("The minimum number of players is 6" + "\n")
                continue
            if players > 20:
                print("The maximum number of players is 20" + "\n")
                continue
            return players
        except(ValueError):
            playercount()

# This function generates the number of werewolves based on the number of players
def werewolfcount(players):
    if players < 9:
        werewolves = 1
        return werewolves
    if 12 > players >= 9:
        werewolves = 2
        return werewolves
    if 15 > players >= 11:
        werewolves = 3
        return werewolves
    if 18 > players >= 15:
        werewolves = 4
        return werewolves
    else:
        werewolves = 5
        return werewolves


# This function creates a list of the roles and shuffles them
def shuffle(players, werewolves):
    roles = []
    for x in range(werewolves):
        roles.append("Werewolf")
    roles.append("Seer")
    roles.append("Healer")
    remaining = players - len(roles)
    for y in range(remaining):
        roles.append("Villager")
    random.shuffle(roles)
    return roles


# This function allows the user to input names
def names(players):
    while True:
        decision = input("Would you like to enter names? ")
        if decision not in ["Yes", "yes", "y", "Y", "YES", "No", "NO", "n", "N", "no"]:
            continue
        else:
            if decision in ["No", "NO", "n", "N", "no"]:
                return players
            else:
                nameslist = []
                for i in range(players):
                    nameslist.append(input("Please enter a name: "))
                return nameslist


# This function prints the final assignment of names and roles
def final(assignment):
    if assignment.keys() is int:
        for i in assignment:
            print(i+1, assignment[i])
    else:
        for i in assignment:
            print(i, "-", assignment[i])


def main():
    print("Welcome to Werewolf!")
    print("NOTE: The minimum number of players with default roles is 6, and the maximum number of players is 20" + "\n")
    players = playercount()
    werewolves = werewolfcount(players)
    roles = shuffle(players, werewolves)
    players = names(players)
    if type(players) is int:
        assignmentkey = dict.fromkeys((range(players)))
        assignment = dict(zip(assignmentkey, roles))
    else:
        assignmentkey = dict.fromkeys(players)
        assignment = dict(zip(assignmentkey, roles))
    final(assignment)


if __name__ == '__main__':
    main()

