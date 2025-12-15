print("\n Simple Calculator\n")
def calculate(n1, n2, op):
  if op == "+": return n1 + n2
  elif op == "-": return n1 - n2
  elif op == "*": return n1 * n2
  elif op == "/":
    return "Can't divide by zero!" if n2 == 0 else n1 / n2
  else:
    return "Unknown operation"
a = float(input("Enter first number: "))
sign = input("Enter operator (+, -, *, /): ")
b = float(input("Enter second number: "))
result = calculate(a, b, sign)
print(f"\n Result: {result}")
