#  for 문

# for (int i = 0; i <10; i++)
# for i in iterable_object:

for i in range(5):
    print(i, end=" ")
print()

a = range(5)
print(a.start, a.stop, a.step) # 기본값 0 없음 1

# 1 ~ 5
for i in range(1,6):
    print(i, end=" ")
print()

#  0 ~ 10 짝수만
for i in range(0,11,2):
    print(i, end=" ")
print()

# 5~1
for i in range(5,0,-1):
    print(i, end=" ")
print()

# 1 ~ 10 합
tot = 0
for i in range(1,11):
    tot += i
else:
    print(tot)

print(sum(range(1,11)))
print(type(range(1)))

s = "hi12!@한글韓字אפשひらがなガタカナ⭐"
for c in s:
    print(c, end=" ")
print()

print(len(s))

# 구구단
for i in range(2,10):
    for j in range(1,10):
        print(f"{i} * {j} = {i*j:<2d}",end="  ")
    print()







