#! /usr/bin/python3

import argparse
import sys
import os
from jinja2 import Environment, FileSystemLoader

parser = argparse.ArgumentParser(
    description='Parser to install programs on dockers')
parser.add_argument('--ip', dest="ipAddress", default=None,
                    type=str, help="ip to remote dockers", required=False)
parser.add_argument('--port', dest="port", default=None,
                    type=str, help="port to remote dockers", required=False)
parser.add_argument('--tasks', dest="tasks", default=None,
                    type=str, help="tasks for remote dockers", required=False)
args = parser.parse_args()
ip_addr = args.ipAddress
port = args.port
tasks = args.tasks


def main(ip_addr, port, tasks):
    listOfTasks = tasks.split(",")
    ports = port.split(",")
    ip = []
    for i in ports:
        ip.append("{}:{}".format(ip_addr, i))
    print(ip)

    tempFile = 'playbook.yml.j2'
    file_loader = FileSystemLoader(".")
    env = Environment(loader=file_loader)
    test = True

    template = env.get_template(tempFile)
    output = template.render(dockerHost=ip, something=listOfTasks)
    with open("playbook.yml", "w") as f:
        f.write(output)

    # with open(file, 'a') as f:
    #     for i in listOfTasks:
    #         f.write("\n    - {}".format(i))


    # with open(file2, 'w') as f2:
    #     f2.write(text2)
    # listOfTasks = tasks.split(",")
    # with open(file2, 'a') as f2:
    #     for i in listOfTasks:
    #         f.write("\n    - {}".format(i))
main(ip_addr, port, tasks)
