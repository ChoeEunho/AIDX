listEx01 = list(range(10))
print(listEx01)

str1 = "This is a SampleString"
phoneNum = "010-9556-6177"


str2 = str1.split()
print(str1)
print(str2)
print("{}는 {}개의 단어로 구성되어 있습니다".format(str1, len(str2)))

str3 = phoneNum.split('-')
print(str3)