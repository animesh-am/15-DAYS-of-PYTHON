P, r, t = input("Enter the principal amount, rate of interest and year: ").split()
a = float(P) * (1 + float(r) / 100) ** float(t)
ci = float(a) - float(P)
print(ci)
