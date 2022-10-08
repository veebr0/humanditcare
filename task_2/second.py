
import re


# some  ways to calculate  Manhattan distances

# Elegand mode jejejejejejejj ,just received two vectors
def get_manhattan(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a, b))


# more complicate
def get_manhattan2(x1, y1, x2, y2):
    distance = (x2-x1) + (y2-y1)
    return distance


def get_option(x):
    res = re.findall('(\d+|[A-Za-z]+)', x)
    action = res[0].upper()
    value = res[1]
    return [action, value]

# panel is na fucntion that you can send a value or run empty
# if you send a value this process the object that need an action


def panel(value=""):

    actions = ['N', 'S', 'E', 'W', 'L', 'R', 'F']
    if value:
        action, val = get_option(value)
    else:
        action = ""
        val = ""
    try:
        while action not in actions:
            print(
                "Commands that you can use to move the object ['N','S','E','W', 'L', 'R','F']")
            action = input(
                "Insert a command or press ctrl+c to cancel: ").upper()

        while not val.isdigit():
            val = input(f"Insert a valid value for {action} ")

        if action == 'F':
            boat.move(action, int(val))
        else:
            waypoint.move(action, int(val))
    except KeyboardInterrupt:
        pass


# Prototype is a class to be able to represent a boat or waypoint
# this class can contain more method but actually I just create move method
# this permit move any object however this method need to be improved due to
# need to cover more option.....
class Prototype():
    def __init__(self, north, south, east, west, direction,  *args, **kwargs):
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.start_point = {}
        self.direction = direction.upper()
        self.l = 0
        self.r = 0

    def move(self, action, value, *args, **kwargs):
        if action == 'F' and self.direction == waypoint.direction:
            boat.east += value * waypoint.east
            boat.north += value * waypoint.north

            if len(self.start_point) == 0:  # check if dict is empty
                print(waypoint.north, waypoint.east)
                self.start_point = {
                    'x1': waypoint.east,
                    'y1': waypoint.north
                }

        elif action == 'F' and self.direction != waypoint.direction:
            boat.direction = waypoint.direction
            boat.east += value * waypoint.east
            boat.south += (value * waypoint.south) - boat.north

            boat.north = 0

        elif action == 'N' and self.direction == 'E':  # actions to move waypoint
            waypoint.north += value

        elif action == 'R' and self.direction == 'E':  # actions to move waypoint

            waypoint.south = waypoint.east
            waypoint.east = waypoint.north
            waypoint.direction = 'S'
            waypoint.north = 0

        return


# waypoint and boat initialization
# north, south, east, west
waypoint = Prototype(1, 0, 10, 0, 'E')  # Initialitation of waypoint
boat = Prototype(0, 0, 0, 0, 'E')  # Initialitation of boat


'''
The bellow lines just are a representative of the exercice 2
'''
panel('F10')
print('boat F10',
      f'N{boat.north}, S{boat.south}, E{boat.east}, W{boat.west}, direcction={boat.direction}')

panel('N3')
print('waypoint N3',
      f'N{waypoint.north}, S{waypoint.south}, E{waypoint.east}, W{waypoint.west}, direcction={waypoint.direction}')


panel('F7')
print('boat  F7',
      f'N{boat.north}, S{boat.south}, E{boat.east}, W{boat.west}, direcction={boat.direction}')

panel('R90')
print('waypoint R90',
      f'N{waypoint.north}, S{waypoint.south}, E{waypoint.east}, W{waypoint.west}, direcction={waypoint.direction}')


panel('F11')
print('boat  F11',
      f'N{boat.north}, S{boat.south}, E{boat.east}, W{boat.west}, direcction={boat.direction}')
print(
    f"boat start point - x1: {boat.start_point['x1']} | y1: {boat.start_point['y1']}")
print(f"boat end   point - x2: {boat.east} | y2: {boat.south}")


'''
To resolved the manhattan distances in task 1
I just send two vectors. 
'''
a = (10, 0)
# b = (17, 8) wrong calculation
b = (17, 11)
print('Manhattan distance for task 1', get_manhattan(a, b))

''' 
to get the second answer
'''
a = (boat.start_point['x1'], boat.start_point['y1'])
b = (boat.east, boat.south)
print('Manhattan distance for task 2', get_manhattan(a, b))
