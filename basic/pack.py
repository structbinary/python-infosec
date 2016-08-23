import package_demo

result = package_demo.calculator(20,10)
print("The sum is %d") %result.add()
print("The multiplication is %d") %result.multiply()
print("The division is %d") %result.div()

try:
    a = 0/0
except Exception as e:
    print e
else:
    print("default statement")
finally:
    print("the last statement")