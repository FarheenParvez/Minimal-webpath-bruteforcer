import requests
import urllib
from urllib.request import urlopen
from urllib.error import HTTPError
import urllib.request
import urllib3
http = urllib3.PoolManager()


def check_url(new_url):
	
	try:
		connection = urllib.request.urlopen(new_url)
		return connection.getcode()          
		connection.close()
	except HTTPError as e:
		return e.getcode()					
	
def main():

	status_codes=[]  
	final_url=[]   

	
	url=input("Enter a URL of format (https://.../) :")

	no = int(input("Enter the no of successful status codes :"))

	
	for i in range(0,no):
		status_codes.append(int(input("Enter next no :")))

	#parsing the file
	with open('file.txt','r') as file: 
   
   	       
		for word in file:

			new_url=url+word
			status = check_url(new_url)

			for i in status_codes:
				if status == i:				
					final_url.append(new_url)		
	
	

	print("List of valid URL's-->")
	for i in final_url:
		print(i)

if __name__ == '__main__':
	main()
