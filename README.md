# HumandITcare - Technical solutions

## Coding task
### Define Zeroes, 




## Ship navigation - Part One:
**Question:** Figure out where the navigation instructions lead. What is the Manhattan distance between that location and the ship's starting position?

**Answer:** Checking with a detail of instructions the navigation computer do not really have a problem, the problem come when the sequence of commands are not correct, check details bellow:

`F10->` Will move the ship 10 units east | resume : boat is at east 10,  north 0. - (good)

`N3->`  Will move the ship 3 units to north - (error)

**Error:** appear the ship is moved 3 units to north , leaving the boat in a position to east 10, north 3, but this is impossible because the boat is still facing to east.

The correct way to turn left the ship is using the command L90 and after F3 so this means that the boat will keep in east 10, north 0.

**Next commands**

`F7->` will move the ship another 7 units east (because the ship is still facing east) to east 17, north 3.

`R90->` will cause the ship to turn right by 90 degrees and face south; it remains at east 17, north 0.

`F11->` will move the ship 11 units south to east 17, south 11.

`Calculation: 17 + 11 = 28`

**Vectors:**
```python
a = (10, 0)
b = (17, 11)
```

`The correct Manhattan distance: 18`
