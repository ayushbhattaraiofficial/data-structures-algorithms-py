from dsa_queue import Queue
from dsa_stack import Stack
from recursions.recursion_factorial import Factorial
from recursions.recursion_fibonacci import Fibonacci
from recursions.recursion_reverse_number import ReverseNumber
from recursions.recursion_sum import SumOfNaturalNumber
from recursions.tower_of_hanoi import TowerOfHanoi


def main():
    user_name = input("Enter your username\n")
    print(f"Hello and Welcome, {user_name}")
    print(
        f"""1. Stack
2. Queue
3. Fibonacci
4. Factorial
5. Sum of Natural Numbers
6. Tower of Hanoi
7. Reverse Number"""
    )
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
    elif user_choice == 5:
        call = SumOfNaturalNumber().run()
    elif user_choice == 6:
        call = TowerOfHanoi().run()
    elif user_choice == 7:
        call = ReverseNumber().run()


if __name__ == "__main__":
    main()
