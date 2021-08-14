
with open(r'./cloudera_environment.yml') as file:
    cloudera_environment = yaml.load(file)
    #print(cloudera_environment['cloudera_managment_server']['ip'])

                                                    ###  Cloudera managment server connection paramters ###

cm_ip = (cloudera_environment['cloudera_managment_server']['ip'])
print "cloudera mamangemnt server IP: ", cm_ip
cm_username = 'admin'
cm_password = 'admin'
cm_port = '7180'
api_version = '/api/v33'
headers = {'content-type': 'application/json'}
url = 'http://'+cm_ip+':'+cm_port+''+api_version+'/'

                                                    #### update service monitor paramters  ####

unit = 'cm/service/roleConfigGroups/mgmt-SERVICEMONITOR-BASE/config'

## Set service monitor none java memory ##
none_java_memory_byte = '17179869184'

response = requests.put(url=url+unit,data= '{"items":[{ "name": "firehose_non_java_memory_bytes","value": '+none_java_memory_byte+' }]}' ,headers=headers, auth=(cm_username, cm_password))
#print(response.text)
print "service monitor none java memory was set to : ", (int(none_java_memory_byte)/1073741824),"GB"

### Set service monitor Java Heap memory ###
## Set required memory in bytes- 2G = 2147483648
java_heap_memory_byte = '2147483648'

response = requests.put(url=url+unit,data= '{"items":[{ "name": "firehose_heapsize","value": '+java_heap_memory_byte+' }]}' ,headers=headers, auth=(cm_username, cm_password))
#print(response.text)
print "service monitor  java memory was set to : ", (int(java_heap_memory_byte)/1073741824),"GB"



                                                    #### update Host monitor  ####

unit = 'cm/service/roleConfigGroups/mgmt-HOSTMONITOR-BASE/config'


## Set service host monitor none java memory ##
## Set required memory in bytes- 16G = 17179869184  / 12G = 12884901888
none_java_memory_byte = '17179869184'

response = requests.put(url=url+unit,data= '{"items":[{ "name": "firehose_non_java_memory_bytes","value": '+none_java_memory_byte+' }]}' ,headers=headers, auth=(cm_username, cm_password))
#print(response.text)
print "service host monitor none java memory was set to : ", (int(none_java_memory_byte)/1073741824),"GB"