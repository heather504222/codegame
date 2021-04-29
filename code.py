x = 0

while x < 3 :
	code = input('請輸入密碼:')
	if code == 'a12345':
		print('密碼正確!')
		break
	else:
		x = x + 1
		if x < 3:
			print('密碼錯誤，你還剩下',3-x ,'次機會')
		else:
			print('掰掰')
