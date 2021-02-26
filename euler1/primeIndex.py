def main(position):
    # generate prime numbers
    primes = [2]
    next_prime = 2
    while len(primes) <= position-1:
        for i in range(1, next_prime, 1):
            if next_prime % i == 0:
                next_prime += 1
                # i=1
            else:
                continue
        primes.append(next_prime)
    print(primes)
    return f'The {index}th prime position is {primes[index-1]}'


if __name__ == '__main__':
    index = int(input('Enter the index: \n'))
    print(main(index))
