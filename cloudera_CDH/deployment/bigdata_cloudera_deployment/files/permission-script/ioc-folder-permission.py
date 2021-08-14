import os
import yaml
import argparse

ioc_permission_command = []

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
ioc_folder_user_permission = ioc_section["folder_permission"]["permission"]

command = str(ioc_folder_user_permission) + ' ' + '/' + os.path.join(root_folder_name,ioc_folder_name)
ioc_permission_command.append(command)


for sub_folder_info in ioc_section["sub_folders"]:
    sub_folder_name = sub_folder_info["name"]
    sub_folder_permission = sub_folder_info["folder_permission"]["permission"]

    command = str(sub_folder_permission) + ' ' + '/' + os.path.join(root_folder_name, ioc_folder_name,sub_folder_name)
    ioc_permission_command.append(command)

for tenant in tenant_section:
    tenant_folder_name = tenant["tenant_name"]
    tenant_user_permission = tenant["folder_permission"]["permission"]

    command = str(tenant_user_permission) + ' ' + '/' + os.path.join(root_folder_name,ioc_folder_name,ioc_output_folder_name,ioc_tenant_prefix + tenant_folder_name)
    ioc_permission_command.append(command)


print(ioc_permission_command)
file.close()

