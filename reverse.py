def reverse(s):
	if s=='':
		return s
	else:
		return s[-1]+reverse(s[:-1])

def main():
	str1=str(input('Enter a string: '))
	print(reverse(str1))

if __name__=='__main__':
	main()	