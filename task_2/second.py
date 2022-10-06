import re


def get_option(x):
    res = re.findall('(\d+|[A-Za-z]+)', x)
    action = res[0].upper()
    value = res[1]
    return [action, value]


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


# def get_object_values(obj):
#     value_x = get_option(obj.x)
#     value_y = get_option(obj.y)
#     return [value_x[1], value_y[1]]


def getargs(args):
    for arg in args:
        print(arg)


class Prototype():
    def __init__(self, north, south, east, west, direction,  *args, **kwargs):
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.start_point = 0
        self.end_point = 0
        self.direction = direction.upper()
        self.l = 0
        self.r = 0

    def move(self, action, value, *args, **kwargs):
        if action == 'F' and self.direction == 'E':
            boat.east += value * waypoint.east
            boat.north += value * waypoint.north
            boat.end_point += boat.east

        elif action == 'N' and self.direction == 'E':  # actions to move waypoint
            waypoint.north += value

        elif action == 'R' and self.direction == 'E':  # actions to move waypoint
            print('waypoint actual para girar',
                  f'N{waypoint.north}, S{waypoint.south}, E{waypoint.east}, W{waypoint.west}, direcction={waypoint.direction}, trayectoria={waypoint.end_point}')

        return

    def addpos(self, x, y, obj, **kwargs):
        obj.x = x
        obj.y = y
        return


# waypoint and boat initialization
# north, south, east, west
waypoint = Prototype(1, 0, 10, 0, 'E')
boat = Prototype(0, 0, 0, 0, 'E')
print('waypoint',
      f'N{waypoint.north}, S{waypoint.south}, E{waypoint.east}, W{waypoint.west}, direcction={waypoint.direction}, trayectoria={waypoint.end_point}')
print('boat B',
      f'N{boat.north}, S{boat.south}, E{boat.east}, W{boat.west}, direcction={boat.direction}, trayectoria={boat.end_point}')

panel('F10')
print('boat A',
      f'N{boat.north}, S{boat.south}, E{boat.east}, W{boat.west}, direcction={boat.direction}, trayectoria={boat.end_point}')

panel('N3')
print('waypoint',
      f'N{waypoint.north}, S{waypoint.south}, E{waypoint.east}, W{waypoint.west}, direcction={waypoint.direction}, trayectoria={waypoint.end_point}')


panel('F7')
print('boat A',
      f'N{boat.north}, S{boat.south}, E{boat.east}, W{boat.west}, direcction={boat.direction}, trayectoria={boat.end_point}')

panel('R90')
