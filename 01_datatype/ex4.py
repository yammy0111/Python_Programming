# 문자열(str)
# '', ""

a = "Python"
print(a,type(a))

print("I'll be back")
print('I\'ll be back')

# 여러 줄 문자열 *주석 아님*
a = """
Life is short
You need python
"""
print(a)

def func():
    """
    히히 함수 설명
    """
    pass

print(func.__doc__)

# 문자열 연결
print("Hello" + " Python")

# 문자열 반복
print("Hello " * 10)
print("-" * 50)

# 문자열 연산 시 주의사항
# print("Hello" + 3)
print("Hello" + str(3))

print("10"+"2")
print(int("10")+int("2"))

# 문자열 포맷팅
name = "뽀로로"
age = 23
print(f"이름: {name}, 나이: {age}")
print(f"내년 나이: {age + 1}")
print(f"{name.upper}")
print(f"{{중괄호 쓰기}}")

pi = 3.141529

print(f"{pi:.3f}")
print(f"{pi:.0f}")

num = 123456789
print(f"{num:,}")

print(f"{num:15,d}")
print(f"{num:<15,d}")

print(f"{num:015,d}")
print(f"{num:<015,d}")
