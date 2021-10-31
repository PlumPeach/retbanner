from socket import *

def retBanner(ip,port):
	setdefaulttimeout(1)
	try:
		sock=socket()
		sock.connect((ip,port))
		banner=sock.recv(1024)
		return banner

	except:
		return


def main():
	ip='192.168.1.5'
	port=22
	banner=str(retBanner(ip,port))
	if(banner):
		print('[*] '+ip+': '+banner)


main()


age=10
x='pass' if age>=18 else 'fail'
print(x)
