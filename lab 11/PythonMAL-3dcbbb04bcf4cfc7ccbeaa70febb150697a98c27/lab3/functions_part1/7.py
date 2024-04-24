def has__33(nums):
    check = 0
    for i in nums:
        if i == 3:
            check+=1
        else:
            check = 0
        if check == 2:
            return True
    return False
print(has__33([1,7,3,5]))