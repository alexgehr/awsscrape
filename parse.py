from lxml import html
import requests
import sys

localdata=""
data={}
text="""Example python parse.py t2.micro memory \nUsage: python parse.py <Api Name> <object>\nValid Objects are \nname\napiname\nmemory\ncomputeunits\nvcpus\necu-per-vcpu\nstorage\narchitecture\nnetworkperf\nebs-max-bandwith\nebs-throughput\nebs-iops\nmaxips\nenhanced-networking\nvpc-only\nlinux-virtualization\n """
url='http://www.ec2instances.info/?region=eu-central-1'

if len(sys.argv) == 3:
    try:
        handler=open('index.html','r')
        for line in handler:
            localdata+=line
        content=html.fromstring(localdata)
        handler.close
    except IOError:
        print "file not found downloading..."
        try:
            handler=open('index.html','w')
            page=requests.get(url)
            content=html.fromstring(page.content)
            handler.write(page.content)
            handler.close
        except:
            raise


    tmp="""//table[@class="table table-bordered table-hover table-condensed"]/tbody/tr[@id="%s"]"""
    path = tmp % sys.argv[1]
    table=content.xpath(path)
    for tr in table:
        for td in tr.getchildren():
            for hit in td.values():
                data[hit]=td.text
            for span in td.getchildren():
                data[hit]=span.text
    if 'apiname' in data.keys():
        if sys.argv[2].strip() not in data.keys():
            print "Object "+sys.argv[2]+" not available"
            print text
        else:
#            print data[sys.argv[2]]
            if type(data[sys.argv[2]]) == str: 
               print data[sys.argv[2]].strip()
 
    else:
        print "Instance type "+sys.argv[1] +" is not found" 
else:    
    print text
