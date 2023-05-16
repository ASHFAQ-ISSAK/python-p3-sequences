#!/usr/bin/env python3


def print_fibonacci(length):
    fibonacci = []  # Initialize an empty list to store Fibonacci numbers

    if length == 0:  # If length is 0, print an empty list
        print(fibonacci)
    elif (
        length == 1
    ):  # If length is 1, print a list containing only the first Fibonacci number
        print([0])
    else:
        fibonacci = [0, 1]  # Initialize the Fibonacci list with the first two numbers

        # Generate Fibonacci sequence until it reaches the desired length
        while len(fibonacci) < length:
            # Calculate the next Fibonacci number by summing the last two numbers
            next_number = fibonacci[-1] + fibonacci[-2]
            fibonacci.append(
                next_number
            )  # Append the next number to the Fibonacci list

        print(fibonacci)  # Print the generated Fibonacci sequence
