#python program to download any image from the internet using web crawler

import random
#import urllib.request package which lets us download any data from the internet
import urllib.request

def download_web_image(url):
	'''a function to download any image from internet'''
	
	#give the image any random number name
	name = random.randint(1,1000)
	full_name = str(name) + '.jpg'
	
	#to use anything from the library urllib.request use its name
	urllib.request.urlretrieve(url, full_name)
	#url is the parameter and url of image and parameter full_name is the name given to image to save it
	
download_web_image('https://s3-us-east-2.amazonaws.com/tattoo-media/wp-content/uploads/2018/01/05114625/11116.jpg')
