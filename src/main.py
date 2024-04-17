from dsa_queue import Queue
from dsa_stack import Stack
from recursions.recursion_factorial import Factorial
from recursions.recursion_fibonacci import Fibonacci


def main():
    user_name = input("Enter your username\n")
    print(f"Hello and Welcome, {user_name}")
    print(f"1. Stack\n2. Queue\n3. Fibonacci\n4. Factorial")
    user_choice = int(
        input("Press the number on the list to call the function\n")
    )
    if user_choice == 1:
        call = Stack().run()
    elif user_choice == 2:
        call = Queue().run()
    elif user_choice == 3:
        call = Fibonacci().run()
    elif user_choice == 4:
        call = Factorial().run()


if __name__ == "__main__":
    main()
