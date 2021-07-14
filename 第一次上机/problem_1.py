class Problem1:
    def __init__(self) -> None:
        pass
    def input_(self):
        self.equation=input("Please the equation")
    def calculate_print(self):
        try:
            print(eval(self.equation))
        except:
            print("input error")
homework=Problem1()
homework.input_()
homework.calculate_print()