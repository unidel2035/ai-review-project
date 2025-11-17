def add(a, b):
    result = a + b
    return result

def subtract(a, b):
    result = a - b
    return result

def multiply(a, b):
    result = a * b
    return result

def divide(a, b):
    if b == 0:
        return None
    result = a / b
    return result

# Пример с потенциальными улучшениями
def calculate_stats(numbers):
    if not numbers:
        return None
    
    total = 0
    for num in numbers:
        total += num
    
    average = total / len(numbers)
    return average
