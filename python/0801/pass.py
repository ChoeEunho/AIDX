scores = [99,85,96,92]

total = 0
underSubject = 0
average = 0

for score in scores:
    if score < 40:
        underSubject += 1
    total += score

print('40점 미만 과목 수 :',underSubject)
average = total/len(scores)
print('평균점수 : ', average)

if underSubject > 0 or average < 60:
    print('공단에 기부를 해줘서 너무 감사합니다.')
else:
    print("축하합니다.")