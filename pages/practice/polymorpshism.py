
class MathOperations:
    def add(self, a, b, c=0):  # Using default parameter for overloading behavior
        return a + b + c

math_op = MathOperations()

print(math_op.add(2, 3))       # Output: 5
print(math_op.add(2, 3, 4))    # Output: 9
print(math_op.add(3,2))
