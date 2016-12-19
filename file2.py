#input program

import sys
def func1():
	global varTitle
	varTile = " "
	
def func2():
	global varArtist
	varArist = " "
	

def titart():

	print("How do you want to search")

	print("Enter A for by Song Title only")

	print("Enter B for by Artist only")

	print("Enter C for by Song Title and Artist together")

	sort =input("Enter search Type A, B, C.  ")
	
	if (sort != 'A' and sort != "a" and sort != 'B' and sort != 'b' and sort != 'C' and sort !='c'):

		print("You must enter a valid sort type! ")
		
	else:

		print(sort)

		#var1 = (" ")

		#var2 = (" ")
		
		if(sort == 'A' or sort == 'a'):
								
			var1 =input("Enter Song Title a ")
			#input(var1)
			#var1 = var1 + 'a'

		elif(sort == 'B' or sort == 'b'):
								
			var2 =input("Enter Artist Name b ")
			#input(var2)
			#var2 = var2 + 'b'
		else:
								
			var1 =input("Enter Song Title c ")
			#input(var1)
			#var1 = var1 + 'c'

			var2 =input("Enter Artist Name c ")
			#input(var2)
			#var2 = var2 + 'c'
			
		print(var1 + ' 58')

		print(var2 + ' 60')
		#print (globals ())
		#func1()
		#global varTitle
		varTile = input(var1 + ' 64')
	if (varTitle != 'on the road 64'):d
		print(varTitle)
	else:
		#func2()
		#global varArtist
		varArist = input(var2 + ' 68')
		
		#func1()
		#varTitle = var1
		#func2()		
		#varArtist = var2
			
		print(varTitle + ' 76')

		print(varArtist + ' 77')	
			

titart()

#print(var1)

#print(var2)


#print(varTitle)

#print(varArtist)