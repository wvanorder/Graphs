from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
from collections import deque

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
opposite_directions= {'n': 's', 's': 'n', 'w': 'e', 'e': 'w', None: None}

traversal_path = []


def explore(room, visited=None):
    if visited is None:
        visited = set()
    path = []
    visited.add(room.id)
    for direction in room.get_exits():
        new_room = room.get_room_in_direction(direction)
        if new_room.id not in visited:
            new_room_path = explore(new_room, visited)
            if new_room_path:
                local_path = [direction] + new_room_path + [opposite_directions[direction]]
            else:
                local_path = [direction, opposite_directions[direction]]
            path = path + local_path
    
    return path





# # TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)


traversal_path = explore(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
