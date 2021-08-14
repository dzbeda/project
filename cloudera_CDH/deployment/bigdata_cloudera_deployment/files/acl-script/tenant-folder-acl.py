import os
import yaml
import argparse

tenant_acl_commands = []

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
    repository_folder_name =  repository["repository_name"]
    if repository_folder_name == "raw":
        tenant_prefix = raw_tenant_prefix
    else:
        tenant_prefix = curated_tenant_prefix

    for sensor in sensor_section:
        sensor_folder_name = sensor["sensor_name"]

        for stream in sensor["streams"]:
            stream_folder_name = stream["stream_name"]

            for tenant in tenant_section:
                tenant_folder_name = tenant["tenant_name"]


                for acl_user_info in tenant.get("acl_users") or []:
                    acl_user = acl_user_info ["user"]
                    acl_user_permission = acl_user_info["permission"]

                    command = 'user' + ':' + acl_user + ':' + acl_user_permission + ' ' + '/' + os.path.join(root_folder_name, repository_folder_name,sensor_prefix + sensor_folder_name + stream_prefix + stream_folder_name,tenant_prefix + tenant_folder_name)
                    tenant_acl_commands.append(command)


                for acl_group_info in tenant.get("acl_groups") or []:
                    acl_group = acl_group_info["group"]
                    acl_group_permission = acl_group_info["permission"]

                    command = 'group' + ':' + acl_group + ':' + acl_group_permission + ' ' + '/' + os.path.join(root_folder_name, repository_folder_name,sensor_prefix + sensor_folder_name + stream_prefix + stream_folder_name,tenant_prefix + tenant_folder_name)
                    tenant_acl_commands.append(command)

#print(len(tenant_acl_commands))
print(tenant_acl_commands)
file.close()



