fib = [0, 1]

n_terms = int(input("Enter the number of terms: "))

for i in range(n_terms-2):
    print(fib[i])
    fib.append(fib[i] + fib[i + 1])

print(fib)
