'''this program finds the resolution the the jpeg(joint photographic experts group)
image passed'''

def jpeg_res(filename):
	'''function to find the resolution of an image'''
	
	#open image for reading in binary mode.
	with open(filename,'rb') as img_file:
		
		#height of image(in 2 bytes) is at 164th position.
		img_file.seek(163)
		#read the 2 bytes
		a = img_file.read(2)
		#calculate height
		height = (a[0]<<8)+a[1]
		#next 2 bytes is width
		a = img_file.read(2)
		#calculate width
		width = (a[0]<<8)+a[1]
		
	print("THE RESOLUTION OF IMAGE IS",width,'X',height)

jpeg_res('wings.jpg')
