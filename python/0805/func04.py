import os

def add():
	print('덧셈 결과 : ', inputNumber1 + inputNumber2)
def sub():
        print('뺄셈 결과 : ', inputNumber1 - inputNumber2)
def mul():
        print('곱셈 결과 : ', inputNumber1 * inputNumber2)
def div():
        print('나눗셈 결과 : ', inputNumber1 / inputNumber2)

while True:
	input('아무키나 누르세요')
	os.system('clear')

	selectOperator = int(input('연산자를 선택하세요 1.덧셈, 2.뺄셈, 3. 곱셈, 4. 나눗셈, 5.exit'))
	if(selectOperator == 5):
		break
	inputNumber1 = float(input('숫자를 입력하세요'))
	inputNumber2 = float(input('숫자를 입력하세요'))
	if(selectOperator == 1):
		add()
	elif(selectOperator == 2):
        	sub()
	elif(selectOperator == 3):
        	mul()
	elif(selectOperator == 4):
        	div()
	elif(selectOperator == 5):
        	break
	else:
		print('연산자 다시 선택')
