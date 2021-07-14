class Problem2:
    def __init__(self) -> None:
        pass
    def input_(self):
        try:
            self.length=float(input("Please the length"))
            self.width=float(input("Please the width"))
        except:
            print("Input error")
    def calculate_print(self):
        print("{:.2f}".format(self.length*self.width))
homework=Problem2()
homework.input_()
homework.calculate_print()