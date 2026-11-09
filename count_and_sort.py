'''
Write functions to count occurrences of integers outside a specified range in a list.

The program should:

- Take as input a list of integers and two integers m and n defining an inclusive range [m, n].
- Return a dictionary with keys as integers from the list that are NOT in the range [m, n], and values as the count of their occurrences.

Example:  
Input: int_list = [4, 4, 10, 4, 2, 1, 2], m = 4, n = 8  
Output: {1: 1, 2: 2, 10: 1}

Functions:

- is_outside_range(num, m, n): Takes an integer num and range bounds m, n, returns True if num is not in [m, n].
- update_frequency(freq_dict, num): Updates the count of num in the dictionary freq_dict.
- count_outside_range(int_list, m, n): Processes int_list, uses the above functions, and returns the frequency dictionary.

Example usage:  
>>> count_outside_range([4, 4, 10, 4, 2, 1, 2], 4, 8)  
{1: 1, 2: 2, 10: 1}
'''

def is_outside_range(num, m, n):
    # if num not in range(m, n+1):
    #     return True
    # else:
    #     return False  
    return num < m or num > n

def update_frequency(freq_dict, num):
    if num in freq_dict:  # we met the number before in the list and we already saved a value
        freq_dict[num] += 1   # freq_dict[num] = freq_dict[num] + 1
    else:  # this is the first time we see the number
        freq_dict[num] = 1  # first time I see it, so I've seen it once

def count_outside_range(int_list, m, n):
    dictionary_to_return = {}
    for number in int_list:
        if is_outside_range(number, m, n):
            update_frequency(dictionary_to_return, number)

    # sorted_list_of_k_v_couples = sorted(dictionary_to_return.items(), key=lambda k_v_tuple: k_v_tuple[0])
    # final_dict = dict(sorted_list_of_k_v_couples)
    # return final_dict

    return dictionary_to_return