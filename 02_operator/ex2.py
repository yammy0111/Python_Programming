# 비트 연산자
a = 5          # 0000 0101
b = 3          # 0000 0011
print(a & b)   # 0000 0001
print(a | b)   # 0000 0111
print(a ^ b)   # 0000 0110
print(a << b)  # 0001 0100 5 > 10 > 20 > 40
print(40 >> b) # 0000 0101 40 > 20 > 10 > 5
print(~a)      # 1111 1010 -> 0000 0110

# 멤버십 연산자
print("a" in "apple")
print(1 in [1,2,3])
print(2 in (1,2,3))
print(3 in {1,2,3}) # iterable 이면 다 됨

# 삼항 연산자
# int max a > b ? a : b

a, b = 2, 3
max = a if a > b else b

print("짝수" if a%2 == 0 else "홀수")

score = 85
# 90 80 70점 으로 A B C D 등급
print("A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D")