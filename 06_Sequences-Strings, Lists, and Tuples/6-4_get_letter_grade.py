#!/usr/bin/env python
def cal_average_score(score_list):
    sum = 0
    for score in score_list:
        sum += score
    return float(sum) / len(score_list)

def get_letter_grade(score_list):
    average_score = cal_average_score(score_list)
    if average_score >= 90 :
        return 'A'
    elif average_score >=80 :
        return 'B'
    elif average_score >=70 :
        return 'C'
    elif average_score >= 60 :
        return 'D'
    else :
        return 'F'

print get_letter_grade([79,23,99,82,54,43])