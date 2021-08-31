'''Once upon a time, on a way through the old wild mountainous west,…
… a man was given directions to go from one point to another.
The directions were "NORTH", "SOUTH", "WEST", "EAST".
Clearly "NORTH" and "SOUTH" are opposite, "WEST" and "EAST" too.

Going to one direction and coming back the opposite direction right away is a needless effort.
Since this is the wild west, with dreadfull weather and not much water,
it's important to save yourself some energy, otherwise you might die of thirst!

How I crossed a mountainous desert the smart way.
The directions given to the man are, for example, the following (depending on the language):

["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"].
or
{ "NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST" };
or
[North, South, South, East, West, North, West]
You can immediatly see that going "NORTH" and immediately "SOUTH" is not reasonable,
better stay to the same place! So the task is to give to the man a simplified version of the plan.

A better plan in this case is simply:

["WEST"]
or
{ "WEST" }
or
[West]
Other examples:
In ["NORTH", "SOUTH", "EAST", "WEST"], the direction "NORTH" + "SOUTH"
is going north and coming back right away.

The path becomes ["EAST", "WEST"], now "EAST" and "WEST" annihilate each other,
therefore, the final result is [] (nil in Clojure).

In ["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"], "NORTH" and "SOUTH" are
not directly opposite but they become directly opposite after the reduction
of "EAST" and "WEST" so the whole path is reducible to ["WEST", "WEST"].

Task
Write a function dirReduc which will take an array of strings and returns
an array of strings with the needless directions removed (W<->E or S<->N side by side).

The Haskell version takes a list of directions
with data Direction = North | East | West | South.

The Clojure version returns nil when the path is reduced to nothing.

The Rust version takes a slice of enum Direction {North, East, West, South}.
See more examples in "Sample Tests:"

Notes
Not all paths can be made simpler. The path ["NORTH", "WEST", "SOUTH", "EAST"]
is not reducible. "NORTH" and "WEST", "WEST" and "SOUTH",
"SOUTH" and "EAST" are not directly opposite of each other and
can't become such. Hence the result path is itself : ["NORTH", "WEST", "SOUTH", "EAST"].
if you want to translate, please ask before translating.'''

'''
5x5
[[0 0 0 0 0]
 [0 0 0 0 0]
 [0 0 1 0 0]
 [0 0 0 0 0]
 [0 0 0 0 0]]
arr = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
 '''

import numpy as np

def dirReduc(arr):
    array = np.zeros((7,7), dtype=np.uint8)
    (y, x) = (3, 3) #startpos
    array[3, 3] = 1 #startpos value
    '''
    position = array[x, y]
    
    '''
    count = 0
    dict_dir = {}
    for i, direction in enumerate(arr):
        array[3, 3] = 1
        try:
            if direction == 'NORTH':
                if arr[0:i].count("NORTH") == 0:
                    array[y-1, x] = 1
                    (y, x) = (y-1, x)
                    dict_dir['NORTH'] = 1
                    if count > 0:
                        if arr[i-1] == 'SOUTH':
                            array[y, x] = 0
                            array[y+1, x] = 0
                            del dict_dir['SOUTH']
                            del dict_dir['NORTH']
                        else:
                            (y, x) = (y, x)
                if arr[0:i].count("NORTH") > 0:
                    array[y-1, x] = 1
                    (y, x) = (y-1, x)
                    dict_dir['NORTH'] = 1
                    if count > 0:
                        if arr[i-1] == 'SOUTH':
                            array[y, x] = 0
                            array[y+1, x] = 0
                        elif (arr[0:i].count("SOUTH") % 2) == 0:
                            if 'NORTH' in dict_dir.keys():
                                del dict_dir['NORTH']
                            if 'SOUTH' in dict_dir.keys():
                                del dict_dir['SOUTH']
                        else:
                            (y, x) = (y, x)

            elif direction == 'SOUTH':
                if arr[0:i].count("SOUTH") == 0:
                    array[y+1, x] = 1
                    (y, x) = (y+1, x)
                    dict_dir['SOUTH'] = 1
                    if count > 0:
                        if arr[i-1] == 'NORTH':
                            array[y, x] = 0
                            array[y-1, x] = 0
                            del dict_dir['NORTH']
                            del dict_dir['SOUTH']
                        else:
                            (y, x) = (y, x)
                if arr[0:i].count("SOUTH") > 0:
                    array[y+1, x] = 1
                    (y, x) = (y+1, x)
                    dict_dir['SOUTH'] = 1
                    if count > 0:
                        if arr[i-1] == 'NORTH':
                            array[y, x] = 0
                            array[y-1, x] = 0
                        elif (arr[0:i].count("NORTH") % 2) == 0:
                            if 'SOUTH' in dict_dir.keys():
                                del dict_dir['SOUTH']
                            if 'NORTH' in dict_dir.keys():
                                del dict_dir['NORTH']
                        else:
                            (y, x) = (y, x)

            elif direction == 'WEST':
                if arr[0:i].count("WEST") == 0:
                    array[y, x - 1] = 1
                    (y, x) = (y, x - 1)
                    dict_dir['WEST'] = 1
                    if count > 0:
                        if arr[i-1] == 'EAST':
                            array[y, x] = 0
                            array[y, x+1] = 0
                            del dict_dir['EAST']
                            del dict_dir['WEST']
                        else:
                            (y, x) = (y, x)
                if arr[0:i].count("WEST") > 0:
                    array[y, x - 1] = 1
                    (y, x) = (y, x - 1)
                    dict_dir['WEST'] = 1
                    if count > 0:
                        if arr[i-1] == 'EAST':
                            array[y, x] = 0
                            array[y, x+1] = 0
                            del dict_dir['EAST']
                        elif (arr[0:i].count("WEST") % 2) == 0:
                            if 'EAST' in dict_dir.keys():
                                del dict_dir['EAST']
                            if 'WEST' in dict_dir.keys():
                                del dict_dir['WEST']
                        else:
                            (y, x) = (y, x)

            elif direction == 'EAST':
                if arr[0:i].count("EAST") == 0:
                    array[y, x+1] = 1
                    (y, x) = (y, x+1)
                    dict_dir['EAST'] = 1
                    if count > 0:
                        if arr[i - 1] == 'WEST':
                            array[y, x] = 0
                            array[y, x-1] = 0
                            del dict_dir['WEST']
                            del dict_dir['EAST']
                        else:
                            (y, x) = (y, x)

                if arr[0:i].count("EAST") > 0:
                    array[y, x+1] = 1
                    (y, x) = (y, x+1)
                    dict_dir['EAST'] = 1
                    if count > 0:
                        if arr[i - 1] == 'WEST':
                            array[y, x] = 0
                            array[y, x-1] = 0
                        elif (arr[0:i].count("EAST") % 2) == 0:
                            if 'WEST' in dict_dir.keys():
                                del dict_dir['WEST']
                            if 'EAST' in dict_dir.keys():
                                del dict_dir['EAST']
                        else:
                            (y, x) = (y, x)

            count += 1

        except ValueError:
            print('not valid move')

    print(count)
    print(array)
    print(dict_dir)
    print(x, y)
    fastest_way = [x for x in dict_dir.keys()]
    return fastest_way
    # print(fastest_way)




# arr = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
# arr = ["NORTH", "SOUTH", "SOUTH", "WEST", "EAST", "WEST"]
arr = ["EAST", "WEST", "WEST", "NORTH", "WEST", "NORTH"]

dirReduc(arr)