#마지막문제
#a=int(input())
#b=list(map(int,input().split()))
#total=0
#for i in b:
#    total=total+i/max(b)*100
#print(total/a)
#class2 1번문제
# x,y,w,h=map(int,input().split())
# data=[x,y,w-x,h-y]
# print(min(data))
#문제2번
# while True:
#     a,b,c=map(int,input().split())
#     if a==0 and b==0 and c==0:
#         break
#     else:
#         print('right'if a*a+b*b==c*c or b*b+c*c==a*a or a*a+c*c==b*b else'wrong')
#문제3번
#a=int(input())
# for i in range(a):
#     x,y,z=map(int,input().split())
#     if z%x==0:
#         print(str(x)+'0'+str(int(z/x))if len(str(int(z/x)))==1 else str(x)+str(int(z/x)))
#     else:
#         print(str(z%x)+'0'+str(int(z/x+1))if len(str(int(z/x+1)))==1 else str(z%x)+str(int(z/x+1)))
#문제4번
#문제5번 문제를 잘 읽자
# a=int(input())
# count=1
# endnum=1
# if a==1:
#     print(1)
# else:    
#     while True:
#         endnum=count*6+endnum
#         if endnum>=a:
#             print(count+1)
#             break
#         elif 1000000000<a:
#             break
#         else:
#             count=count+1
#문제6번
# num,m=map(int,input().split())
# temp=list(map(int,input().split()))
# total=[]
# for i in range(num):
#     for j in range(num):
#         for k in range(num):
#             if temp[i]!=temp[j] and temp[j]!=temp[k] and temp[i]!=temp[k] and m>=temp[i]+temp[j]+temp[k]:
#                 total.append(temp[i]+temp[j]+temp[k])
#             else:
#                 continue
#             print(temp[i]+temp[j]+temp[k])
# print(max(total))
#문제7번
# a=input()
# s=input()
# total=0
# for i in range(len(s)):
#     total=total + (ord(s[i])-96)*pow(31,i)
# print(total%1234567891)
#문제8번
# while True:
#     s=input()
#     if s=='0':
#         break
#     else:
#         print('yes'if s[::]==s[::-1] else 'no')
#문제9번