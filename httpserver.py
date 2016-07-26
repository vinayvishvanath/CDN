#!/usr/bin/python
import os.path
#from os import curdir, sep
import sys
import urllib2
import socket
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from cStringIO import StringIO
s5 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)recv_data = s5.recv(1024)print recv_data#delay_cmd = "scamper -c 'ping -c 1' -i " + client_ip + " | awk 'NR ==2 {print $7}' | cut -d '=' -f 2"
#xyz= "pwd"
dir=os.popen('pwd').readlines()
dir=dir[0]
print 'directory',dir


try:
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(('8.8.8.8',0))
	source_ip = s.getsockname()[0]
	print "Source_IP",source_ip
except socket.error, msg:
		print "SOCKET ERROR:", msg[1]
		sys.exit()


port_number= int(sys.argv[2])
print 'Port_Number',port_number
if port_number not in range(0,65535):
		print 'Enter valid port number'
		sys.exit()
org_server=sys.argv[4]
if org_server != 'ec2-54-88-98-7.compute-1.amazonaws.com':
	print 'Enter correct name of origin server'
	sys.exit()


class request_handler(BaseHTTPRequestHandler):
	#print "INSIDE THE CLASS"
	def do_GET(self):
		print 'PATH', self.path
		#self.path=='/'
		#self.path=self.path[1:]
		#self.path=self.path[:-1]
		print "SELF PATH",self.path
		try:
			self.path='http://'+org_server+':8080'+self.path
			print "SELF PATH 8080",self.path
			get_request = urllib2.urlopen(self.path).read()
			response = StringIO(get_request)
			self.send_response(200)
			self.send_header('Content-type','text/html')
			self.end_headers()
			self.wfile.write(get_request)
		except IOError:
			self.send_error(404,'Page not found:')


try:
	web_server = HTTPServer(('', int(port_number)), request_handler)
	#print 'SERVER IS RUNNING'	
	#print 'Starting server'
	print 'Use keyboard interrupt to stop the server: <CTRC-C>'
	web_server.serve_forever()
	#print 'Use keyboard interrupt to stop the server: <CTRC-C>'
except:
	#print 'use <CTRL-c> to stop'
	web_server.socket.close()
	#print 'use <CTRC-C> to stop'





		
			
			
			
		
