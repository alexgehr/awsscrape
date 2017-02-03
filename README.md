# awsparse
(ag)
Parses Data from  "http://www.ec2instances.info/?region=eu-central-1"

This Python script will parse Data from ec2instances.info 

requires lxml 


Example: python parse.py t2.micro memory 

Usage: python parse.py ApiName object

Valid objects are </br> 
name </br> 
apiname </br>
memory </br>
computerunits </br>
vcpus </br>
ecu-per-vcpu </br>
storage </br>
architecture </br>
networkperf </br>
ebs-max-bandwith  </br>
ebs-throughput </br>
ebs-iops </br>
maxips </br>
enhanced-networking </br>
vpc-only </br>
linux-virtualization </br>


