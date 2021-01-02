def fib(a,b,n,sum):
    while a<=n:
        print(a, end=' ')
        a,b=b, a+b
        sum=sum+a
    print(f'The sum is: {sum}')

if __name__ == "__main__":
    a,b,sum=0,1,0
    n=int(input('Enter value n: '))
    fib(a,b,n,sum)

# sum=0
# n=int(input("Your number: "))
# for i in range(n):
#     sum=sum+i
# print(sum)