import socket
import commands
import SocketServer



PORT = 65000

##############################################################################
###### Calculate Delay is calculated using scamper and assigned to variable delay
##############################################################################

def calc_delay(client_ip):
	try:
		#print "calc_delay cip =",client_ip
		delay_cmd = "scamper -c 'ping -c 1' -i " + client_ip + " | awk 'NR ==2 {print $7}' | cut -d '=' -f 2"
		delay = commands.getoutput(delay_cmd)
		#print "Recvd delay using scamper =",delay
		return delay
	except:
		delay = 5000.0
		return delay

#############################################################################################
######  Passing the closest Replica-Server IP address with the smallest RTT to variable  cip
#############################################################################################

class OurTCPHandler(SocketServer.BaseRequestHandler):

	def handle(self):
		#print "In calculate Delay"

		cip = self.request.recv(1024).strip()
		#print "CIP =",cip
		delay = calc_delay(cip)
		#print "Delay = ",delay
		self.request.sendall(str(delay))

##########################################################
### Exception as keyboard interrupt and Ctrl - C to Quit
### Serve forever  - keeping the server running forever
##########################################################
if __name__ == "__main__":

	try:
		delayd = SocketServer.TCPServer(("", PORT), OurTCPHandler)
		print "Press Ctrl+C to quit"
		delayd.serve_forever()
	except KeyboardInterrupt:
		delayd.socket.close()
