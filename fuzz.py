import random

def divide(v1, v2):
    if v2 == 0:
        raise ValueError("Cannot divide by zero")
    return v1 / v2

def getItem(data, index):
    if index >= len(data) or index < 0:
        raise IndexError("Index out of bounds")
    return data[index]

def absValue(number):
    return abs(number)

def sumList(numbers):
    total = 0
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise ValueError("All items in the list must be numbers")
        total += num
    return total

def isUpperCase(char):
    if not isinstance(char, str) or len(char) != 1:
        raise ValueError("Input must be a single character")
    return char.isupper()

def fuzzValues(val1, val2):
    return divide(val1, val2)

def simpleFuzzer1():
    ls_ = ['123', 'True', 'False', [], None, '/', '2e34r']
    for x in ls_:
        print(x)
        try:
            mod_x = float(x) + random.random() if isinstance(x, (int, float)) else float(x)
            fuzzValues(float(x), mod_x)
        except Exception as e:
            print(f"Error: {e}")

def simpleFuzzer2():
    data = [1, 2, 3]
    index = 4
    print(data)
    print(index)
    try:
        getItem(data, index)
    except Exception as e:
        print(f"Error: {e}")

def simpleFuzzer3():
    value = -4
    print(value)
    try:
        absValue(value)
    except Exception as e:
        print(f"Error: {e}")

def simpleFuzzer4():
    data = ["1", 2, 3]
    print(data)
    try:
        sumList(data)
    except Exception as e:
        print(f"Error: {e}")

def simpleFuzzer5():
    char = 'A'  # Corrected to test single characters only
    print(char)
    try:
        isUpperCase(char)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    simpleFuzzer1()
    simpleFuzzer2()
    simpleFuzzer3()
    simpleFuzzer4()
    simpleFuzzer5()
