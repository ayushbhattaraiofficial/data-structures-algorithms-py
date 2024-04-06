class Stack:

    def __init__(self):
        self.stack = self.top = [None] * 5

    def push(self, element):
        if self.stack[4]:
            print("Stack Overflow")
        else:
            self.stack.insert(0, element)
            self.stack.remove(None)

    def pop(self):
        if self.stack[0]:
            self.stack.pop(0)
            self.top = self.stack
        else:
            print("Stack Underflow")

    def display(self):
        if self.top:
            print(f"{self.top}")
        else:
            print("Empty Stack")

    def search(self, element):
        try:
            print(f"{self.stack.index(element)}")
        except ValueError:
            print(f"Value not found")

    def run(self):
        print(f"1. Push\n2. Pop\n3. Display\n4. Search\n5. Exit")
        while True:
            user_call = int(input("Choose the number to call function\n"))
            if user_call == 1:
                self.push(int(input("Enter number to push\n")))
            elif user_call == 2:
                self.pop()
            elif user_call == 3:
                self.display()
            elif user_call == 4:
                self.search(int(input("Enter item to search\n")))
            elif user_call == 5:
                break
