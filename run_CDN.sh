#!/bin/bash

######################## Passing the arguments to respective variables #######################

while getopts "p:o:u:n:i:" options
do
    case $options in
        p)
            PORT=$OPTARG
            ;;
        o) 
            ORIGIN=$OPTARG
            ;;
        u)
            uname=$OPTARG
            ;;
        n)
            DOMAIN=$OPTARG
            ;;
        i)
            KEY=$OPTARG
            ;;
        ?)
            echo "unkonw argument"
        exit 1
        ;;
    esac
done

#echo $PORT
#echo $ORIGIN
#echo $uname
#echo $DOMAIN
#echo $KEY

######################## Storing all Replica-Servers in an array ################################

REPLICA_SERVER[0]="ec2-54-85-32-37.compute-1.amazonaws.com"
REPLICA_SERVER[1]="ec2-54-193-70-31.us-west-1.compute.amazonaws.com"
REPLICA_SERVER[2]="ec2-52-38-67-246.us-west-2.compute.amazonaws.com"
REPLICA_SERVER[3]="ec2-52-51-20-200.eu-west-1.compute.amazonaws.com"
REPLICA_SERVER[4]="ec2-52-29-65-165.eu-central-1.compute.amazonaws.com"
REPLICA_SERVER[5]="ec2-52-196-70-227.ap-northeast-1.compute.amazonaws.com"
REPLICA_SERVER[6]="ec2-54-169-117-213.ap-southeast-1.compute.amazonaws.com"
REPLICA_SERVER[7]="ec2-52-63-206-143.ap-southeast-2.compute.amazonaws.com"
REPLICA_SERVER[8]="ec2-54-233-185-94.sa-east-1.compute.amazonaws.com"

######################## Start the run of HTTP files on all Replica-Servers ######################

for var in "${REPLICA_SERVER[@]}"
do
#    echo "Running http files on replica: " $var
    #ssh -i $KEY -n -f $uname@$var "sh -c 'cd ~/HTTP_hemenway/; nohup python http_caldelay.py > /dev/null 2>&1 &'"
    ssh -i $KEY -n -f $uname@$var "sh -c 'cd ~/HTTP_hemenway/; nohup ./httpserver -p $PORT -o $ORIGIN > /dev/null 2>&1 &'"

done

####################### Start the run of dns file on DNS Server ################################

DNS=cs5700cdnproject.ccs.neu.edu
# echo "Running dns files on: " $DNS
ssh -i $KEY -n -f $uname@$DNS "sh -c 'cd ~/DNS_hemenway/; nohup ./dnsserver -p $PORT -n $DOMAIN > /dev/null 2>&1 &'"
