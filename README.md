# awsparse
(ag)
Parses Data from  "http://www.ec2instances.info/?region=eu-central-1"

This Python script will parse Data from ec2instances.info 

requires lxml 


Example: python parse.py t2.micro memory 

Usage: python parse.py ApiName object

Valid objects are  
name  
apiname 
memory 
computerunits 
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


