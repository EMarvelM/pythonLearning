#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list

    # 1 2 3 4 5 6 --> len
    # 0 1 2 3 4 5 --> index
    if idx >= len(my_list):
        return my_list

    my_list[idx] = element
    return my_list
