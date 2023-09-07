data = {}
answer = []

def fibo(n):
    if n <= 1:
        return n   
    if n in data.keys():
        return data[n]
    else:
        num = fibo(n - 1) + fibo(n - 2)
        data.update({n : num})
    print(data[n])
    return data[n]

print(answer)
fibo(10)