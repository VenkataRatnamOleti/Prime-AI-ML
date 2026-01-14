def is_prime(n):
    if n<0: return False
    for i in range(2,n):
        if not n%i: return False
    return True


print(is_prime(4))