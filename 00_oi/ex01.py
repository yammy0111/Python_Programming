# 입출력
a = input()
print(a, end="")
print(type(a))
print(a, type(a))
print(a, type(a), sep=", ")

a = int(a)
print(a, type(a))

a = int(input())
print(a, type(a))

b = float(input())
print(b, type(b))

# 정수 2개 입력
a = int(input())
b = int(input())
print(a,b)

a = input().split()
print(a, type(a))

a = map(int,input().split())
print(a, type(a))

a,b,c = map(int,input().split())
print(a, b, c)

a = list(map(int,input().split()))
print(a, type(a))