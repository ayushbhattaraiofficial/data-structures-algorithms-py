from enum import StrEnum
from sys import maxsize


class Stack:
    size = int

    def createEmptyStack(self, size):
        self.size = size
        stack = []
        return stack

    def isEmpty(self, stack):
        return len(stack) == 0

    def isFull(self, stack):
        return len(stack) == self.size

    def push(self, stack, item):
        if self.isFull(stack):
            print("Stack Overflow")
            return 1
        stack.append(item)
        print(item + "pushed to stack")

    def pop(self, stack):
        if self.isEmpty(stack):
            return "Stack Underflow"

        return stack.pop()

    def display(self, stack):
        if self.isEmpty(stack):
            return "Stack is Empty"

        return stack[len(stack) - 1]

    def search(self, stack, search_term):
        for i in range(len(stack) - 1):
            if stack[i] == search_term:
                return f"Item found in index {i+1}"
        return "Item not in stack"

    def run(self):
        stack = self.createEmptyStack(
            int(input("Give me the size of the stack"))
        )
        print(f"1. Push\n2. Pop\n3. Display\n4. Search\n5. Exit")
        while True:
            user_call = int(input("Choose the number to call function\n"))
            if user_call == 1:
                self.push(stack, str(input("Enter number to push\n")))
            elif user_call == 2:
                print(f"{self.pop(stack)}")
            elif user_call == 3:
                print(f"{self.display(stack)}")
            elif user_call == 4:
                print(self.search(stack, str(input("Enter item to search\n"))))
            elif user_call == 5:
                break
