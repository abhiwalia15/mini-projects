'''python program to find the SHA-1 message digest of a file'''

#import hashlib module
import hashlib

def has_file(filename):
	'''this function returns the SHA-1 of the hash of the file passed into it.'''
	
	#make a hash object
	h = hashlib.sha1()
	
	#open file for reading in binary mode
	with open(filename,'rb') as file:
		
		#loop till the end of the file
		chunk = 0
		while chunk!= b'':
			
			#read only 1024 bytes at a time
			chunk = file.read(1024)
			h.update(chunk)
			
	#return the hex representation of the digest message
	return h.hexdigest()
	
message = has_file('dick.mp3')
print(message)
