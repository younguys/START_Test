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