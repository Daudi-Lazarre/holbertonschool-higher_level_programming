#!/usr/bin/python3
def search_replace(my_list, search, replace):
    add = []
    for thing in my_list:
        if thing == search:
            add.append(replace)
        else:
            add.append(thing)
    return(add)