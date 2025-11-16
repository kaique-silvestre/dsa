# Here I was leraning how recursions works, reading "Understanding Algorithms", I've learned about base case and the recursion case or however they called in english

from time import sleep

def counting_seconds(number):
    if number <= 0:
        return 
    print(number); number -= 1 # Just seeing how thr semi colon works
    sleep(1)
    counting_seconds(number)


print(counting_seconds(100))
