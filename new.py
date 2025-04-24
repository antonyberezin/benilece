import threading

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def print_even():
    print("Even numbers: ", [num for num in numbers if num % 2 == 0])

def print_odd():
    print("Odd numbers: ", [num for num in numbers if num % 2 != 0])

def print_multiple_of_3():
    print("Multiples of 3: ", [num for num in numbers if num % 3 == 0])

# Creating threads
even_thread = threading.Thread(target=print_even)
odd_thread = threading.Thread(target=print_odd)
multiple_thread = threading.Thread(target=print_multiple_of_3)

# Starting and joining threads
even_thread.start()
even_thread.join()

odd_thread.start()
odd_thread.join()

multiple_thread.start()
multiple_thread.join()
