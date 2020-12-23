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
	
#Reversing a String using a simple for loop
word = input(print("Enter word"))
reverse_word = ""
for i in range(len(word)-1,-1,-1):
  reverse_word = reverse_word + word[i]

print(reverse_word)  
