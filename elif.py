num = int(input('0~100 안에서 숫자 하나를 입력 해주세요:'))

if num < 10:
  print('입력값은 10보다 작습니다.')
elif num > 10 and num <= 50:
  print('입력값은 10보다 크고 50과 같거나 작습니다.')
elif num > 51 and num <= 100:
	print('입력값은 51보다 크고 100과 같거나 작습니다')
else:
	print('입력값이 범위내에 포합되지 안습니다')