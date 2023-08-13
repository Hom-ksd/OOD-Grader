class StackCalc:
    def __init__(self) -> None:
        self.stack = []
        self.is_error = False
        self.error_data = ""
        
    def POP(self):
        if self.stack :
            self.stack.pop()
        else :
            pass

    def DUP(self):
        if self.stack :
            data = self.stack[-1]
            self.stack.append(data)
        else :
            pass

    def PSH(self,data):
        self.stack.append(data)

    def run(self,data):
        list_data = data.split()
        for arg in list_data:
            if arg == '+':
                if len(self.stack) >= 2:
                    data1 = self.stack.pop()
                    data2 = self.stack.pop()
                    self.PSH(data1 + data2)
            elif arg == '-':
                if len(self.stack) >= 2:
                    data1 = self.stack.pop()
                    data2 = self.stack.pop()
                    self.PSH(data1 - data2)
            elif arg == '*':
                if len(self.stack) >= 2:
                    data1 = self.stack.pop()
                    data2 = self.stack.pop()
                    self.PSH(data1 * data2)
            elif arg == '/':
                if len(self.stack) >= 2:
                    data1 = self.stack.pop()
                    data2 = self.stack.pop()
                    self.PSH(data1 / data2)
            elif arg == 'POP':
                self.POP()
            elif arg == 'DUP':
                self.DUP()
            elif (arg >= '0' and arg <= '9'):
                self.PSH(int(arg))
            else:
                self.is_error = True
                self.error_data = arg
                break


    def getValue(self):
        if not self.is_error:
            if self.stack:
                if self.stack[-1] - int(self.stack[-1]) != 0:
                    return self.stack[-1]
                else:
                    return int(self.stack[-1])
            else:
                return 0
        else:
            return f"Invalid instruction: {self.error_data}"

print("* Stack Calculator *")
arg = input("Enter arguments : ")
machine = StackCalc()
machine.run(arg)
print(machine.getValue())