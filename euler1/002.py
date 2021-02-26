def main(max,nums):
    i=len(nums)-1
    sum,next=0,0
    evens=list()
    while True:
        next=nums[i]+nums[i-1]
        if next <= max:
            nums.append(next)
            i+=1
        else:
            break
        
    for item in nums:
        if item%2 ==0:
            evens.append(item)
    for j in evens:
        sum+=j

    print(nums)
    print(evens)
    print(sum)




if __name__=='__main__':
    max=int(input('Max value: \n'))
    nums=[0,1]
    main(max,nums)