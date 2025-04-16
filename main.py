def get_weather(tmp: int):
    if (tmp > 20):
        return 'hot'
    return 'cold'

def divide(a: int, b: int):
    if b == 0:
        raise ValueError("It is not possible divide for zero.")
    
    return a / b

def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int( n ** 0.5 ) + 1):
        if n % i == 0:
            return False
        
    return True