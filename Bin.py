# Write a python code for convert Decimal Number to Binary Number in O(n) times


def DectoBin(dec):
	if dec >= 1:
		DectoBin(dec//2)
		print(dec%2,end='')

dec = int(input("Enter any number = "))
DectoBin(dec)
