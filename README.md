# awsscrape
Offline Version will download page if not already present local ...All request will be made to the local file

Parses Data from  "http://www.ec2instances.info/?region=eu-central-1"

This Python script will parse Data from ec2instances.info 

requires lxml 

Usage: python parse.py ApiName object

Example: python parse.py t2.micro memory 


Valid objects are  
name  

apiname 

memory 

computeunits 

vcpus 

ecu-per-vcpu 

storage 

architecture 

networkperf 

ebs-max-bandwith  

ebs-throughput 

ebs-iops 

maxips 

enhanced-networking 

vpc-only 

linux-virtualization 


