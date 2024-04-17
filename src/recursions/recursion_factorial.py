class Factorial:
    def getNumber(self):
        return int(input("Factorial of Number\t"))

    def getFactorial(self, number):
        if number == 0:
            return 1
        else:
            return int(number) * int(self.getFactorial(number - 1))

    def run(self):
        factorial_number = self.getNumber()
        print(f"The factorial number is {self.getFactorial(factorial_number)}")
