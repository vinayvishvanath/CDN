import urllib
import socket
import sys

#dict = defaultdict(list)

#ec2-54-88-98-7.compute-1.amazonaws.com
replicas =	['ec2-54-85-32-37.compute-1.amazonaws.com',
	'ec2-54-193-70-31.us-west-1.compute.amazonaws.com',
	'ec2-52-38-67-246.us-west-2.compute.amazonaws.com',
	'ec2-52-51-20-200.eu-west-1.compute.amazonaws.com',
	'ec2-52-29-65-165.eu-central-1.compute.amazonaws.com',
	'ec2-52-196-70-227.ap-northeast-1.compute.amazonaws.com', 
	'ec2-54-169-117-213.ap-southeast-1.compute.amazonaws.com',
	'ec2-52-63-206-143.ap-southeast-2.compute.amazonaws.com',
	'ec2-54-233-185-94.sa-east-1.compute.amazonaws.com']

replica =      ['54.85.32.37',
        '54.193.70.31',
        '52.38.67.246',
        '52.51.20.200',
        '52.29.65.165',
        '52.196.70.227', 
        '54.169.117.213',
        '52.63.206.143',
        '54.233.185.94']

#print replics
dict = {}
Location = []
for ip in replica:
	#print ip
#	Link = 'http://api.ipinfodb.com/v3/ip-city/?key=ddec29eecf2db148ca855a99b9be5f47d379348e734a46f9711202ddb2d3740b&ip='+sys.argv[1]
	f = urllib.urlopen('http://api.ipinfodb.com/v3/ip-city/?key=ddec29eecf2db148ca855a99b9be5f47d379348e734a46f9711202ddb2d3740b&ip=%s'%ip)
	loc =  f.read().split(';')[8:10]
	Location.append(loc)
	dict[ip] = loc
	

#print Location
print dict
