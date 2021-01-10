n = int(input())
fib = 0
next_fib = 1
for __ in range(n):
    fib, next_fib = next_fib, fib + next_fib
print(fib)
