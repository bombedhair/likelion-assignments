import random
from time import sleep

lunch = ["파스타", "피자", "비빔밥", "스시"]

while True:
    print("현재 목록: ", lunch)
    item = input("추가할 음식을 입력 해주세요: ")
    if(item == "q"):
        break
    else:
        lunch.append(item)
print(lunch)

set_lunch = set(lunch)
while True:
    print("현재 목록:", set_lunch)
    item = input("삭제할 음식을 입력 해주세요 : ")
    if(item == "q"):
        break
    else:
        set_lunch = set_lunch - set([item])

print(set_lunch, "목록에서 메뉴를 선택합니다.")
for i in range(5, 0, -1):
    print(i)
    sleep(1)
print(random.choice(list(set_lunch)))