import random

print("☆★☆★ 로또 번호 자동 생성기 ☆★☆★")
print("------------------------------------")
print("게임 수를 입력하세요")

num = input("게임 수 >")

print("------------------------------------")

for item in range(0,int(num)):
    lotto = random.sample(range(1,46),6)
    lotto.sort()
    print(lotto)
