num1 = int(input("insert the first number."))
num2 = int(input("insert the second number."))
class do_math:
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2

    def add(self):
        return self.val1 + self.val2
    def multiply(self):
        return self.val1 * self.val2
    def divide(self):
        return self.val1 / self.val2
    def subtract(self):
        return self.val1 - self.val2
    
math_instance = do_math(num1,num2)
print(math_instance.add())
print(math_instance.multiply())
print(math_instance.divide())
print(math_instance.subtract())