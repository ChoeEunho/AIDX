import copy
#shollow copy & deep copy
#리스트의 이름에는 리스트의 시작 주소가 자동으로 들어가 있습니다.

a = [1, 2, 3]
b = a
print(id(a), id(b))    #id 함수는 메모리의 주소값을 구해줍니다.
a[0] = 6
print(a,b)
print(id(a), id(b))


s =[1,2,3]
t = copy.deepcopy(s)
print(s, t)
print(id(s), id(t))
s[0] = 6
print(s,t)
print(id(s), id(t))