#!/bin/bash


while getopts "p:o:u:n:i:" temp
do
    case $temp in
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

################## Storing all Replica-Servers in an array  #############################

REPLICA_SERVER[0]="ec2-54-85-32-37.compute-1.amazonaws.com"
REPLICA_SERVER[1]="ec2-54-193-70-31.us-west-1.compute.amazonaws.com"
REPLICA_SERVER[2]="ec2-52-38-67-246.us-west-2.compute.amazonaws.com"
REPLICA_SERVER[3]="ec2-52-51-20-200.eu-west-1.compute.amazonaws.com"
REPLICA_SERVER[4]="ec2-52-29-65-165.eu-central-1.compute.amazonaws.com"
REPLICA_SERVER[5]="ec2-52-196-70-227.ap-northeast-1.compute.amazonaws.com"
REPLICA_SERVER[6]="ec2-54-169-117-213.ap-southeast-1.compute.amazonaws.com"
REPLICA_SERVER[7]="ec2-52-63-206-143.ap-southeast-2.compute.amazonaws.com"
REPLICA_SERVER[8]="ec2-54-233-185-94.sa-east-1.compute.amazonaws.com"

################# Termianting all codes running on HTTP Replica-Server  #####################
################# Removing the folder HTTP_hemenway  ##################

for replica in "${REPLICA_SERVER[@]}"
do
#    echo "Stopping http files on replica: " $var
    ssh -i $KEY $uname@$replica 'killall python > /dev/null 2>&1'
    ssh -i $KEY $uname@$replica 'rm -rf ~/HTTP_hemenway'

done


################# Termianting all jobs running on DNS Server -> cs5700cdnproject.ccs.neu.edu ####################
################# Removing the folder DNS_hemenway #####################

DNS=cs5700cdnproject.ccs.neu.edu
# echo "Closing dns files on: " $DNS
ssh -i $KEY $uname@$DNS 'killall python > /dev/null 2>&1'
ssh -i $KEY $uname@$DNS 'rm -rf ~/DNS_hemenway'





