import sys
input = sys.stdin.readline

class Event:
    def __init__(self, name, cost):
        self.name = name
        self.cost = int(cost)
        self.members = []

    def ADD(self, userName):
        if userName not in self.members:
            self.members.append(userName)
            print("SUCCESSFUL")
        else:
            print("USER ALREADY ADDED TO EVENT")

    def REMOVE(self, userName):
        if userName in self.members:
            self.members.remove(userName)
            print("SUCCESSFUL")
        else:
            print("USER NOT FOUND IN EVENT")

    def COST(self):
        total = self.cost * len(self.members)
        print(f"{total}")


events = {}

while True:
    line = input().strip()

    data = line.split()

    if data[0] == "FINISH":
        break

    if data[0] == "CREATE":
        name = data[1]
        cost = data[2]

        if name in events:
            print("UNSUCCESSFUL CREATE")
            continue

        events[name] = Event(name, cost)
        print("SUCCESSFUL")
        continue

    elif data[0] == "DELETE":
        name = data[1]

        if name not in events:
            print(f"INVALID EVENTNAME")
            continue

        del events[name]
        print("SUCCESSFUL")
        continue

    elif data[0] == "ADD":
        user = data[1]
        name = data[2]

        if name not in events:
            print("INVALID EVENTNAME")
            continue

        events[name].ADD(user)

    elif data[0] == "REMOVE":
        user = data[1]
        name = data[2]

        if name not in events:
            print("INVALID EVENTNAME")
            continue

        events[name].REMOVE(user)

    elif data[0] == "COST":
        name = data[1]

        if name not in events:
            print("INVALID EVENTNAME")
            continue

        events[name].COST()
