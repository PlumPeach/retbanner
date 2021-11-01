#!/usr/bin/python
from socket import *
import optparse
from termcolor import colored


def retBanner(ip,port):
	setdefaulttimeout(1)
	try:
		sock=socket()
		sock.connect((ip,port))
		banner=sock.recv(1024)
		banner=banner.decode('utf-8')
		return banner

	except:
		print(colored('[-]Port %d is closed '%port,'red'))
		sock.close()

def name_resolver(ip,port):
	tgtName=''
	setdefaulttimeout(1)
	tgtip=gethostbyname(ip)
	try:
		tgtName=gethostbyaddr(ip)
	except:
		print(colored('[*]Cannot resolve hostname for: '+tgtip,'yellow'))
	
	if tgtName!='':
		print(colored('[+]Hostname: '+tgtName[0],'yellow'))
	if tgtip!='':
		print(colored('[+]Ip Address: '+tgtip,'yellow'))


def main():
	parser=optparse.OptionParser('Usage of program'+' -H <target Host>  -P <Tagrget port> ')
	parser.add_option('-H', dest='ip',type='string',help='Specify the host')
	parser.add_option('-P',dest='port',type='int',help='Specify target port')
	(options,args)=parser.parse_args()
	ip=options.ip
	port=options.port
	if(ip==None or port==None):
		print(parser.usage)
		exit(0)
	banner=str(retBanner(ip,port))
	if(banner):
		print(colored('[*] '+ip+'/%d: '%port+banner,'green'))

	name_resolver(ip,port)



if __name__=='__main__':
	main()


