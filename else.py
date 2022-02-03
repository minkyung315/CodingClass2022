number = input("정수 입력 >")
number = int(number)

if number % 2 == 0:
  print("짝수입니다.") #조건이 참일 때, 즉 짝수 조건
else: #정반대인 상황에서 같은 구문을 두번 반복하지 않고 else을 이용한다.
  print("홀수 입니다.") #조건이 거짓일 때, 즉 홀수 조건