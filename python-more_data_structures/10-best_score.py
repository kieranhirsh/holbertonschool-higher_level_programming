#!/usr/bin/python3

def best_score(a_dictionary):
    best = "None"
    
    if a_dictionary:
        for key in a_dictionary:
            if best == "None":
                current_best = a_dictionary[key]
                best = key

            if a_dictionary[key] > current_best:
                current_best = a_dictionary[key]
                best = key

    return best
