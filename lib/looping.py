# lib/looping.py

def happy_new_year():
    """Counts down from 10 to 1 using a while loop, then prints a celebratory message."""
    count = 10
    while count >= 1:
        print(count)
        count -= 1
    print("Happy New Year!")


def square_integers(int_list):
    """
    Accepts a list of integers and returns a new list containing
    the square of each integer.
    """
    squared = []
    for num in int_list:
        squared.append(num * num)
    return squared


def fizzbuzz():
    """
    Prints numbers from 1 to 100, but:
    - Replaces multiples of 3 with "Fizz"
    - Replaces multiples of 5 with "Buzz"
    - Replaces multiples of both 3 and 5 with "FizzBuzz"
    """
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

