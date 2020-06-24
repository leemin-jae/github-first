

# from sys import stdin, stdout 
# a, b, c, d = [int(x) for x in stdin.readline().rstrip().split()] 
# stdout.write(str(a*b*c*d) + "\n")

#------------------------------------------------------------------------------------------------------------------------------------------
# import sys
# input = sys.stdin.readline

# a = input()
# b = input()

# print(int(a)*int(b))

#------------------------------------------------------------------------------------------------------------------------------------------
# import sys
# input = sys.stdin.readline

# a,b = input().split()
# print(int(a)*int(b))


#------------------------------------------------------------------------------------------------------------------------------------------
# import sys
# input = sys.stdin.readline


# A, B, C = [int(x) for x in input().rstrip().split()] 
#A,B,C = input().split()
# A = int(A)
# B = int(B)
# C  = int(C)
# print((A+B)%C)
# print(((A%C) + (B%C))%C)
# print((A*B)%C)
# print(((A%C) * (B%C))%C)

#------------------------------------------------------------------------------------------------------------------------------------------

# import sys
# input = sys.stdin.readline


# a = int(input())
# b = int(input())

# print(a*(b%10))
# print(a*((b%100)//10))
# print(a*(b//100))
# print(a*b)

#------------------------------------------------------------------------------------------------------------------------------------------


# import sys
# input = sys.stdin.readline

# a,b = [int(x) for x in input().rstrip().split()] 

# if a > b:
#     print(">")
# elif a < b:
#     print("<")
# else:
#     print("==")

#------------------------------------------------------------------------------------------------------------------------------------------


# import sys
# input = sys.stdin.readline

# #a = [int(x) for x in input().rstrip().split()] 
# a = int(input())
# b = int(input())

# if a*b > 0:
#     if a > 0:
#         print("1")
#     else:
#         print("3")
# else:
#     if a > 0:
#         print("4")
#     else:
#         print("2")

#------------------------------------------------
# import sys
# input = sys.stdin.readline

# a,b = [int(x) for x in input().rstrip().split()]

# if b - 45 <0:
#     if a > 0:
#         print("{} {}".format(a-1,15+b))
#     else:
#         print("23 {}".format(15+b))
# else:
#     print("{} {}".format(a, b-45))

#------------------------------------------------

# import sys
# input = sys.stdin.readline

# a = int(input())
# num = []

# for i in range(a):
#     b,c = [int(x) for x in input().split()]
#     num.append(b+c)

# for i in range(a):
#     print("Case #1: {}".format(num[i]))

#------------------------------------------------


# bur = 9999
# dr = 9999
# for i in range(5):
#     h = int(input())
#     if i < 3:
#         if(bur > h):
#             bur = h
#     else:
#         if(dr > h):
#             dr =  h
# print(dr +bur -50)

#------------------------------------------------
# a = int(input())

# for i in range(2*a-1):
#     if(i < a):
#         for j in range(i):
#             print(" ", end = "")
#         for k in reversed(range(2*(a-i)-1)):
#             print("*", end="")
#         print()
#     else:
#         for z in reversed(range(2*a-1 -i -1)):
#             print(" ", end = "")
#         for k in range(2*(i-a)+3):
#             print("*", end="")
#         print()

#---------------------------------------------------------

# a = 5

# for i in range(5):
#     print(" "*i + "*"*(2*(5-i)-1))
# for j in range(3,-1,-1):
#     print("/"*j + "*"*(2*(5-j)-1))

#______________-------------------------------------------

# a = int(input())
# for k in range(2*a):
#     if k%2 == 0:
#         for i in range(a):
#             if(i%2 == 0):
#                 print("*",end="")
#             else:
#                 print(" ",end="")
#         print()
#     else:
#         for i in range(a):
#             if(i%2 == 0):
#                 print(" ",end="")
#             else:
#                 print("*",end="")
#         print()


# N = int(input())
# even = N//2
# odd = N - N//2

# for i in range(N):
#     print("* " * odd)
#     print(" *" * even)

#----------------------------------------------------------------------------------
# a = int(input())

# for m in range(a):	
# 	j = 0
# 	l = input()
# 	k = [0 for i in range(len(l))]
# 	for i in range(len(l)):
# 		if(l[i] == "O"):
# 			k[i] = j + 1
# 		j = k[i]
		
# 	print(sum(k))
		