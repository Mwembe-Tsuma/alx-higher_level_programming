#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    total_sum = 0
    total_weight = 0

    for num in my_list:
        total_sum += num[0] * num[1]
        total_weight += num[1]
    return(total_sum / total_weight)
