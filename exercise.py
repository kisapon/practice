class Calculation:
    def __init__(self):
        self.calculationLine = " "
    def SetCalculationLine(self):
        input_line = input("Введите новую строку: ")
        self.calculationLine = input_line
    def SetLastSymbolCalculationLine(self):
        symbol = input("Введите символ: ")
        self.calculationLine += symbol
    def GetCalculationLine(self):
        print("Строка:", self.calculationLine)
    def GetLastSymbol(self):
        print(self.calculationLine[-1])
    def DeleteLastSymbol(self):
        print(self.calculationLine[:-1])


