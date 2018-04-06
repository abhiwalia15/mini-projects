'''mad libs generator is a game that generates random numbers
and fills them into the blanks to give you your desired outputs'''

def mad_libs():
	
	#input an adjective-an adjective is a word that describes something or tells about the quality of anything.
	adjective = input("ENTER ANY ADJECTIVE : \t")
	
	#a noun is a name of something a person,placeor anything.
	noun = input("ENTER ANY NOUN : \t")
	
	#verb is a doing word like actions ,etc.
	verb = input("ENTER ANY VERB : \t")
	
	print("YOUR MATLIB -\n")
	
	matlib = "The " + adjective+' '+noun.title()+' '+verb +" over the lazy dog."
	print(matlib)
	
mad_libs()
