def introKor():
	print('안녕')

def introEng():
        print('Hello')

def introJap():
	print('곤니찌와')

while True:
	selectNum = int(input('where are you from? 1.한국 2.미국 3. 일본 4. exit'))

	if(selectNum == 1):
		introKor()

	elif(selectNum == 2):
		introEng()

	elif(selectNum == 3):
		introJap()
	elif(selectNum == 4):
                exit()

	else:
		introEng()
