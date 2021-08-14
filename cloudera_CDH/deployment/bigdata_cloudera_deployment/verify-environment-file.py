import yaml
ip_list = []
hostname_list = []

def checkIfDuplicates(listOfElems):
    ''' Check if given list contains any duplicates '''
    for elem in listOfElems:
        if listOfElems.count(elem) > 1:
            return True
    return False

###  Read cloudera_enviroment file ###

with open(r'./cloudera_environment.yml') as file:
        cloudera_environment = yaml.load(file)

        ###  update IP and Hostname inside a list  ###

        for item in cloudera_environment['server_details']:
            #print(item['ip'])
            ip_list.append(item['ip'])
           #print (ip_list)

        for item in cloudera_environment['server_details']:
            #print(item['hostname'])
            hostname_list.append(item['hostname'])
            #print (hostname_list)


        ###  update IP and Hostname of postgres,cloudera managment & Yum repository inside a list  ###


ip_list.append(cloudera_environment['cloudera_managment_server']['ip'])
ip_list.append(cloudera_environment['postgres_server']['ip'])
ip_list.append(cloudera_environment['yum_repository']['ip'])
hostname_list.append(cloudera_environment['cloudera_managment_server']['hostname'])
hostname_list.append(cloudera_environment['postgres_server']['hostname'])
hostname_list.append(cloudera_environment['yum_repository']['hostname'])


#print(ip_list)
#print(hostname_list)

        #print(cloudera_environment['cloudera_managment_server']['ip'])


result_ip = checkIfDuplicates(ip_list)

if result_ip:
    print('There is IP duplication under server list located in Cloudera-environment.yaml file')
else:
    print("")



result_hostname = checkIfDuplicates(hostname_list)

if result_hostname:
    print('There is Hostname duplication under server list located in Cloudera-environment.yaml file')
else:
    print("")

