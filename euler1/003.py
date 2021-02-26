def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

if __name__ == "__main__":
    n=int(input('Enter the number: \n'))

    print(largest_prime_factor(n))