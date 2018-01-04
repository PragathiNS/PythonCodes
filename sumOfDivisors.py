# Find the sum of all divisors of a given integer

# Guaranteed constraints: 1 ≤ n ≤ 15.

def sumOfDivisors(n):
    sum = 0
    if n >= 1 and n <= 15:
        for i in range(1, n+1):
            if n % i == 0:
                sum = sum + i
    return sum
    
print (sumOfDivisors(12))
