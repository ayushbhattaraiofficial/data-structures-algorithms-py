from stack import Stack


def main():
    user_name = input("Enter your username\n")
    print(f"Hello and Welcome, {user_name}")
    print(f" 1. Stack\n ")
    user_choice = int(
        input("Press the number on the list to call the function\n")
    )
    if user_choice == 1:
        call = Stack().run()


if __name__ == "__main__":
    main()
