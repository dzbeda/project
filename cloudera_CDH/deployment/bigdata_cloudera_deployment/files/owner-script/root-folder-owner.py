import os
import yaml
import argparse

root_owner_commands = []

parser = argparse.ArgumentParser()
parser.add_argument("--file", "-f", default="../../hdfs-folder-and-permission-config.yml",help="yml configuration file and path")
args = parser.parse_args()
file_name = args.file

with open(file_name,"r") as file:
    hdfs_folder=yaml.load(file)


# Load prefix ##
sensor_prefix = hdfs_folder["sensor_prefix"]
stream_prefix = hdfs_folder["stream_prefix"]
raw_tenant_prefix = hdfs_folder["raw_tenant_prefix"]
curated_tenant_prefix = hdfs_folder["curated_tenant_prefix"]
ioc_tenant_prefix = hdfs_folder["ioc_tenant_prefix"]

#Load section information
root_section = hdfs_folder["root_folder"]
repository_section = hdfs_folder["repository_folders"]
sensor_section = hdfs_folder["sensors_folder"]
tenant_section = hdfs_folder["tenants_folder"]

root_folder_name = root_section["folder_name"]
root_folder_user_owner = root_section["folder_permission"]["user_owner"]
root_folder_group_owner = root_section["folder_permission"]["group_owner"]

command = root_folder_user_owner + ':' + root_folder_group_owner + ' ' + '/' + os.path.join(root_folder_name)
root_owner_commands.append(command)

print(root_owner_commands)
file.close()

