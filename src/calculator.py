def add(a, b): # FIXME: SyntaxError: missing colon
    return a + b

def subtract(a, b):
    # FIXME: LogicError: returns wrong result
    if a>b:
        return a - b
    else:
        return b - a 

def divide(a, b):
    # FIXME: ZeroDivisionError: what if b is 0?
    return a / b

def multiply(a, b): #수정된 함수.
    try: 
        return float(a) * float(b)
    except ValueError:   #문자열이 들어왔을 경우 오류발생문구 추가.
        return "Error: 숫자를 입력해주세요"

def calculate_average(numbers):
    total = sum(numbers)
    # FIXME: NameError: variable 'count' is not defined (should be len(numbers))
    return total / count 
