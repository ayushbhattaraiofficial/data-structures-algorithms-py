class Fibonacci:
    def getNumber(self):
        return int(input("Fibonacci Terms\t"))

    def fibonacciRecursion(self, items):
        if items == 0:
            return 0
        if items == 1 or items == 2:
            return 1
        else:
            return self.fibonacciRecursion(items - 1) + self.fibonacciRecursion(
                items - 2
            )

    def run(self):
        number_of_items = self.getNumber()
        print(f"The fibonacci sequence upto {number_of_items}th term is\n")
        for i in range(1, number_of_items + 1):
            print(f"{self.fibonacciRecursion(i)}")
