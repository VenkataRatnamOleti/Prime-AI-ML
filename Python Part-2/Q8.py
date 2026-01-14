def calculator(a,b,operation):
    match operation:
        case '+': return a+b
        case '-': return a-b
        case '*': return a*b
        case '/': return a/b

print(calculator(5,10,'/'))