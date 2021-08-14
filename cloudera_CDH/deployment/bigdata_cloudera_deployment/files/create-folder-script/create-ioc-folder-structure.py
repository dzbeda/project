import os
import yaml
import argparse

register_ioc_create_folder = []



parser = argparse.ArgumentParser()
parser.add_argument("--file", "-f", default="../../hdfs-folder-and-permission-config.yml",help="yml configuration file and path")
args = parser.parse_args()
file_name = args.file

with open(file_name,"r") as file:
    hdfs_folder=yaml.load(file)


# Load prefix ##
ioc_tenant_prefix = hdfs_folder["ioc_tenant_prefix"]

#Load section information
root_section = hdfs_folder["root_folder"]
tenant_section = hdfs_folder["tenants_folder"]
ioc_section = hdfs_folder["ioc_folder"]


root_folder_name = root_section["folder_name"]
ioc_output_folder_name = ioc_section["output_folder_name"]
ioc_folder_name = ioc_section["folder_name"]
for sub_folder_info in ioc_section["sub_folders"]:
    sub_folder_name = sub_folder_info["name"]

    dirName = '/' + os.path.join(root_folder_name,ioc_folder_name,sub_folder_name)
    register_ioc_create_folder.append(dirName)

for tenant in tenant_section:
    tenant_folder_name = tenant["tenant_name"]

    dirName = '/' + os.path.join(root_folder_name, ioc_folder_name,ioc_output_folder_name,ioc_tenant_prefix + tenant_folder_name)
    register_ioc_create_folder.append(dirName)


#print(len(register_create_folder))
print(register_ioc_create_folder)
file.close()
