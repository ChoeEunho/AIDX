import random

lottoNum = []
one2fortyfive = list(range(1,46))
lottoBall = one2fortyfive.copy()


for i in range(6):
    lottoNum.append(random.choice(lottoBall))
    lottoBall.remove(lottoNum[-1])

lottoNum.sort()
print(lottoNum)


print(one2fortyfive)
print(lottoBall)