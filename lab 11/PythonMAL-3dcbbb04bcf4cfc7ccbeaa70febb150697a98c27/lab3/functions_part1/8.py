def spy_game(nums):
    chetam = ''
    for i in nums:
        chetam+=str(i)
    if '007' in chetam:
        print(True)
    else:
        print(False)
spy_game([0,0,1,7])