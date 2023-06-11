#!/usr/bin/python3
def uniq_add(my_list=[]):
    sigma = 0
    uniq = list(set(my_list))
    for x in uniq:
        sigma += x
    return (sigma)
