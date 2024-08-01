toDoList = ["청소", '쇼핑', "토익", '운동']
print('오늘의 할일 : ', toDoList)

for i in range(len(toDoList)):
    print('끈난 일 :', toDoList.pop(0))
    if len(toDoList) != 0:
        print('남은 일 : ',toDoList)
    else:
        print('할 일 끝~~~~~!')