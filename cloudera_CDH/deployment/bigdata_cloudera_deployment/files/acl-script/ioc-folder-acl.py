import os
import yaml
import argparse

ioc_acl_commands = []

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


#main folder name
root_folder_name = root_section["folder_name"]
ioc_folder_name = ioc_section["folder_name"]
ioc_output_folder_name = ioc_section["output_folder_name"]

#Set acl for ioc main folder
for acl_user_info in ioc_section.get("acl_users") or []:
    acl_user = acl_user_info["user"]
    acl_user_permission = acl_user_info["permission"]

    command = 'user' + ':' + acl_user + ':' + acl_user_permission + ' ' + '/' + os.path.join(root_folder_name,ioc_folder_name)
    ioc_acl_commands.append(command)

for acl_group_info in ioc_section.get("acl_groups") or []:
    acl_group = acl_group_info ["group"]
    acl_group_permission = acl_group_info["permission"]

    command = 'group' + ':' + acl_group + ':' + acl_group_permission + ' ' + '/' + os.path.join(root_folder_name,ioc_folder_name)
    ioc_acl_commands.append(command)

#Set acl for ioc sub-folders

for sub_folder_info in ioc_section["sub_folders"]:
    sub_folder_name = sub_folder_info["name"]

    for acl_user_info in sub_folder_info.get("acl_users") or []:
        acl_user = acl_user_info["user"]
        acl_user_permission = acl_user_info["permission"]

        command = 'user' + ':' + acl_user + ':' + acl_user_permission + ' ' + '/' + os.path.join(root_folder_name,ioc_folder_name,sub_folder_name)
        ioc_acl_commands.append(command)

    for acl_group_info in sub_folder_info.get("acl_groups") or []:
        acl_group = acl_group_info["group"]
        acl_group_permission = acl_group_info["permission"]

        command = 'group' + ':' + acl_group + ':' + acl_group_permission + ' ' + '/' + os.path.join(root_folder_name, ioc_folder_name,sub_folder_name)
        ioc_acl_commands.append(command)

#Set acl for ioc tenants

for tenant in tenant_section:
    tenant_folder_name = tenant["tenant_name"]

    for acl_user_info in tenant.get("acl_users") or []:
        acl_user = acl_user_info["user"]
        acl_user_permission = acl_user_info["permission"]

        command = 'user' + ':' + acl_user + ':' + acl_user_permission + ' ' + '/' + os.path.join(root_folder_name, ioc_folder_name,ioc_output_folder_name,ioc_tenant_prefix + tenant_folder_name)
        ioc_acl_commands.append(command)

    for acl_group_info in tenant.get("acl_groups") or []:
        acl_group = acl_group_info["group"]
        acl_group_permission = acl_group_info["permission"]

        command = 'group' + ':' + acl_group + ':' + acl_group_permission + ' ' + '/' + os.path.join(root_folder_name, ioc_folder_name,ioc_output_folder_name,ioc_tenant_prefix + tenant_folder_name)
        ioc_acl_commands.append(command)



print(ioc_acl_commands)
file.close()