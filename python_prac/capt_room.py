import collections

num_groups, rooms = 5, '1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2'

roomFreqs = {}

for room in rooms.split():
    roomFreqs.setdefault(room, 0)
    roomFreqs[room] += 1

print(min(roomFreqs, key=roomFreqs.get))
