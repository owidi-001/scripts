def main(numb):
    sum_of_square = 0
    sub_sum = 0

    for num in range(numb+1):
        sum_of_square += num ** 2
    # square_of_sum = (sum(range(numb))) ** 2
    for i in range(numb+1):
        sub_sum += i
    square_of_sum = sub_sum**2
    diff = square_of_sum - sum_of_square
    print(sum_of_square)
    print(square_of_sum)
    return f'The difference is {diff} for range {numb}'


if __name__ == '__main__':
    number = int(input('Enter number: \n'))
    print(main(number))
