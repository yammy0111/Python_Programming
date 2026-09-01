# 반복문 : while문 for문

# while문
# 1~10 출력
i = 0
while i<10:
    i += 1
    print(i) 
    # if i == 5:
    #     break
else:
    print("End")

nums = [1, 2, 5, 2, 9]
target = 2
i = 0
found = False
while i<len(nums):
    if nums[i] == target:
        print(f"target {target} found in [{i}] index")
        # break
        found = True
    i += 1
if not found:
    print(f"target {target} not found")

# else:
#     print(f"target {target} not found")

#  1~10까지의 합
#  sum = 55
start = 1
i = start
end = 10
tot = 0

while i <= end:
    tot += i
    i += 1
print(tot)

i = start - 1
tot = 0
while i < end:
    i += 1
    if i % 2 == 1:
        continue
    tot += i
print(tot)
