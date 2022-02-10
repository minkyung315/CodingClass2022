#리스트는 여러가지 자료를 저장할 수 있는 자료이다.
array = [273,32,103,"Hello",True,False] #대괄호 [] 내부에 여러 종류의 자료를 넣어 선언한다.
print(array) #쉽표로 구분해서 입력하서 리스트를 생성할 수 있다.

list_a = [273,32,103,"Hello",True,False]
print(list_a[0]) #index.py 참고
print(list_a[1])
print(list_a[2])
print(list_a[1:3])

#리스트 특정 요소 변경
list_a[0] = "World"
print(list_a[0]) #0번째 글자인 273이 "World"로 변경되어 출력된다.

print(len(list_a)) #typeNlen.py 참고
#리스트 변수에 넣으면 문자열과 다르게 글자 수가 아닌 요소의 개수를 세어준다.

#특정 값이 리스트 내부에 있는지 확인하는 연산자 (in/not in)
list_b = [273,32,103,57,52]
print(273 in list_b) #리스트 내부에 들어있는 값
print(99 in list_b) #리스트 내부에 들어있지 않는 값

print(32 not in list_b) #리스트 내부에 들어있지 않는 값이지만 not in을 사용했기 때문에 참으로 작용한다.
print(315 not in list_b)