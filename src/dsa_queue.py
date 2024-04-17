class Queue:
    size = int

    def makeEmpty(self, size):
        self.size = size
        queue = []
        return queue

    def isEmpty(self, queue):
        return len(queue) == 0

    def isFull(self, queue):
        return len(queue) == self.size

    def enqueue(self, queue, item):
        if self.isFull(queue):
            return "Stack Overflow"
        queue.append(item)
        return f"Pushed {item} to queue"

    def dequeue(self, queue):
        if self.isEmpty(queue):
            return "Queue Empty"
        return f"{queue.pop(0)} removed from queue"

    def traverse(self, queue):
        print("The current queue is \n")
        for i in range(len(queue)):
            print(f"{queue[i]}\n")
        return

    def run(self):
        queue = self.makeEmpty(int(input("Enter the size of queue")))
        while True:
            print("1. Enqueue\n2. Dequeue\n3. Traverse\n4. Exit")
            choice = int(input("Which command to run?"))
            if choice == 1:
                print(
                    f"{self.enqueue(queue,str(
                        input("Enter item to insert")
                    ))}"
                )
            elif choice == 2:
                print(f"{self.dequeue(queue)}")
            elif choice == 3:
                print(f"{self.traverse(queue)}")
            elif choice == 4:
                break
