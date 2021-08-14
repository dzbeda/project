import os
import yaml
import argparse

register_analytic_create_folder = []



parser = argparse.ArgumentParser()
parser.add_argument("--file", "-f", default="../../defaults/analytic-folder-configuration.yml",help="yml configuration file and path")
args = parser.parse_args()
file_name = args.file

with open(file_name,"r") as file:
    hdfs_folder=yaml.load(file)

with open("../../cloudera_environment.yml","r") as file:
    cloudera_environment=yaml.load(file)


#Load section information
root_folder_name = cloudera_environment["hdfs_root_folder"]
anlytic_main_foder = hdfs_folder["analytic_main_folder"]
analytic_section = hdfs_folder["analytic"]

for analytics in analytic_section:
    analytic_name = analytics["analytic_name"]
    for subfolder in analytics["subfolder"]:
        folder_name = (subfolder["folder_name"])

        dirName = os.path.join(root_folder_name,anlytic_main_foder, analytic_name, folder_name)
        register_analytic_create_folder.append(dirName)


#print(len(register_create_folder))
print(register_analytic_create_folder)
file.close()
