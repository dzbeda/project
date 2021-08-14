import os
import yaml
import argparse

sensor_owner_commands = []

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
for repository in repository_section:
    repository_folder_name = repository["repository_name"]
    if repository_folder_name == "raw":
        tenant_prefix = raw_tenant_prefix
    else:
        tenant_prefix = curated_tenant_prefix

        for sensor in sensor_section:
            sensor_folder_name = sensor["sensor_name"]

            for stream in sensor["streams"]:
                stream_folder_name = stream["stream_name"]
                stream_folder_user_owner = stream["folder_permission"]["user_owner"]
                stream_folder_group_owner = stream["folder_permission"]["group_owner"]


                command = stream_folder_user_owner + ':' + stream_folder_group_owner + ' ' + '/' + os.path.join(root_folder_name, repository_folder_name,sensor_prefix + sensor_folder_name + stream_prefix + stream_folder_name)
                sensor_owner_commands.append(command)

#print(len(sensor_owner_commands))
print(sensor_owner_commands)
file.close()



