"""
- Pick the first number of the array
- find de lower value of the array 
- swap both values 
Loop: 
- starting from the next index
- find the new minimu value 
- swap both of them 
"""
# Got it after 2h30 of coding, i was having a big problem when the first pointer number was already the lower, it took me time to understand that, my code was a mess, I wasn't beeing able to identify the problem and resolve it because of that, after rewriting it to something simple and readble i coould make it

def selection_sort(list: list):
    for pointer, fixed_item in enumerate(list):
        minimum = fixed_item
        for current_index in range(pointer+1, len(list)):
            current_item = list[current_index]
            if current_item < minimum:
                minimum = current_item
                minimum_index = current_index
        if fixed_item != minimum:
            list[pointer], list[minimum_index] = minimum, fixed_item
    return list

if __name__ == '__main__':
    array =  [-5, 10, 3, -2, 7]
    var = selection_sort(array)
    print(var)



# array = [20, 18, 15, 10, 5, 0]

# for pointer01, fixed_item in enumerate(array):
#     minimum = fixed_item
#     for current_index in range(pointer01+1, len(array)):
#         current_item = array[current_index]
#         if current_item < minimum:
#             minimum = current_item
#             minimum_index = current_index
#     if fixed_item != minimum:
#         temp = array[pointer01]
#         array[pointer01] = minimum
#         array[minimum_index] = temp
# print(array)

