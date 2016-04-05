#!/usr/bin/env python
def get_cent_count(num):    
    cent_count_arr = []
    cents = [25, 10, 5, 1]

    left = num
    i = 0
    while left != 0:
        cent_count_arr.append(left // cents[i])
        left = left % cents[i]
        i += 1

    return cent_count_arr

print get_cent_count(76)
print get_cent_count(123)
print get_cent_count(88)