def fib(n, dic = {}):
    if n in dic:
        return dic.get(n)
    if n == 2 or n == 1:
        return 1
    dic[n] = fib(n-1, dic)+fib(n-2, dic)
    return dic.get(n)
    
n = input("Enter a Number : ")

n = int(n)

print("Fibonacci of {} is".format(n), fib(n))
