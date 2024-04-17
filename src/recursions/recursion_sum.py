class SumOfNaturalNumber:
    def getNumber(self):
        return int(input("How many numbers to sum?\t"))

    def addNumbers(self, number):
        if number == 1:
            return 1
        else:
            return int(number) + int(self.addNumbers(number - 1))

    def run(self):
        number_to_sum = self.getNumber()
        print(f"The sum of {number_to_sum} is {self.addNumbers(number_to_sum)}")
