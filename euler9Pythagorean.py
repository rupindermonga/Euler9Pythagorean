# finding out Pythogorean triplets

def FindPytha(n):
    for a in range(1,n):
        for b in range(1,n-a):
            c = n - a - b
            if c**2 == a**2 + b**2:
                return a, b, c
    
final = FindPytha(1000)
print(final)