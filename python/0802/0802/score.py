import statistics

scores=[]
hap = 0
for i in range(10):
    scores.append(int(input("{}번 학생 점수 입력 :".format(i+1))))
    hap += scores[i]
    avg = statistics.mean(scores)   #avg = hag / len(scores)
    maxScores = max(scores)
    minScores = min(scores)

for i in range(10):
    print("{}번 학생 점수의 성적={}".format(i+1,scores[i]))

print("성적의 합 =",hap)
print("성적의 평균 =",avg)
print("최대값 =",maxScores)
print("최소값 =",minScores)

print("특정 점수 이상의 학생 수 출력하기")
score = int(input("점수 입력하기 :"))
cnt = 0
for i in range(10):
    if scores[i] >= score:
        cnt += 1
print(scores)
print("{}점 이상의 학생은 {}명 입니다".format(score, cnt))     # print(f'{score}점 이상의 학생은 {cnt}입니다')   