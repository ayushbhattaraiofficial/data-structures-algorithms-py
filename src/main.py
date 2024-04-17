from dsa_queue import Queue
from dsa_stack import Stack


def main():
    user_name = input("Enter your username\n")
    print(f"Hello and Welcome, {user_name}")
    print(f" 1. Stack\n2.Queue ")
    user_choice = int(
        input("Press the number on the list to call the function\n")
    )
    if user_choice == 1:
        call = Stack().run()
    elif user_choice == 2:
        call = Queue().run()


if __name__ == "__main__":
    main()
