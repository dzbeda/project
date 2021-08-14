import os
import yaml
import argparse

ioc_owner_command = []

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
ioc_folder_user_owner = ioc_section["folder_permission"]["user_owner"]
ioc_folder_group_owner = ioc_section["folder_permission"]["group_owner"]

command = ioc_folder_user_owner + ':' + ioc_folder_group_owner + ' ' + '/' + os.path.join(root_folder_name, ioc_folder_name)
ioc_owner_command.append(command)


for sub_folder_info in ioc_section["sub_folders"]:
    sub_folder_name = sub_folder_info["name"]
    sub_folder_user_owner = sub_folder_info["folder_permission"]["user_owner"]
    sub_folder_group_owner = sub_folder_info["folder_permission"]["group_owner"]

    command = sub_folder_user_owner + ':' + sub_folder_group_owner + ' ' + '/' + os.path.join(root_folder_name, ioc_folder_name,sub_folder_name)
    ioc_owner_command.append(command)

for tenant in tenant_section:
    tenant_folder_name = tenant["tenant_name"]
    tenant_user_owner = sub_folder_info["folder_permission"]["user_owner"]
    tenant_group_owner = sub_folder_info["folder_permission"]["group_owner"]

    command = sub_folder_user_owner + ':' + sub_folder_group_owner + ' ' + '/' + os.path.join(root_folder_name,ioc_folder_name,ioc_output_folder_name,ioc_tenant_prefix + tenant_folder_name)
    ioc_owner_command.append(command)


print(ioc_owner_command)
file.close()

