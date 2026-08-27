# 변수
a = 2
b = 3
print(a, b)

# a = 2, b = 3
# a = (2, b) = 3

a = 2; b = 3
a, b = 2, 3 # 권장
print(a, b)

# 값 swap
temp = a
a = b
b = temp
print(a, b)

a, b = b, a
print(a, b)

# 변수명 규칙 (C와 동일)
# 알파벳, 숫자, 특수문자(_)만 가능
# 숫자로 시작 불가
# 예약어 금지

# name! = "aaa"
# 2name = "aaa"
_aaa = "ad"
# class = "class"
한국어_변수 = 10
韓 = 123 # 한자
あ = 456 # 히라나나(일본어)
א = 789 # 히브리어

student_name = "이름" # snake
studentName = "이름"  # camel

MAX = 100
