class ReverseNumber:
    def getNumber(self):
        return int(input("Enter the number to reverse"))

    def reverse(self, number, length):
        if length == 1:
            return number
        else:
            return ((number % 10) * 10 ** int(length - 1)) + (
                self.reverse(int(number / 10), length - 1)
            )

    def run(self):
        number = self.getNumber()
        print(
            f"The reverse of the number is {self.reverse(number, len(str(number)))}"
        )
