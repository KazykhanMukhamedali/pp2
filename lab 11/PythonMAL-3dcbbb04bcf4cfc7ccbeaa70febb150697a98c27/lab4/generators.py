# #1
def gen():
   a = int(input('Enter a number: '))
   squares = (i ** 2 for i in range(a))
   for square in squares:
      print(square)

gen()

#2
# def gen2():
#     a = int(input('Enter a number: '))
#     zap = (i for i in range(a))
#     for chis in zap:
#         print(chis)

# gen2()

# def gen3():
#     val = 0
#     n = int(input())
#     while val!=n:
#         if val%2==0:
#             yield val
#         val+=1

# gen3()
#3
# def gen3():
#     val = 0
#     n = int(input())
#     while val!=n:
#         if val%3==0 or val%4==0:
#             yield val
#         val+=1
# gen3()
# #4
# def gen4(a,b):
#     while a!=b:
#         yield a**2
#         a+=1
# prikols = gen4(5,10)
# for prikol in prikols:
#     print(prikol)
# #5
# def gen5():
#     N=5
#     while N!=0:
#         yield N
#         N-=1
#     print(N)
# gen0 = gen5()
# for i in gen0:
#     print(i)
