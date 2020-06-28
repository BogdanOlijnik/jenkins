#! /usr/bin/python3

import argparse
import sys
import os

parser = argparse.ArgumentParser(
    description='Parser to install programs on dockers')
parser.add_argument('--ip', dest="ipAddress", default=None,
                    type=str, help="ip to remote dockers", required=False)
parser.add_argument('--port', dest="port", default=None,
                    type=str, help="port to remote dockers", required=False)
parser.add_argument('--tasks', dest="tasks", default=None,
                    type=str, help="tasks for remote dockers", required=False)
args = parser.parse_args()
ip = args.ipAddress
port = args.port
tasks = args.tasks


def main(ip, port, tasks):
    file = 'playbook.yml'
    text = '''--- 
- hosts: docker
  become: yes
  become_method: sudo
  roles: '''
    with open(file, 'w') as f:
        f.write(text)
    listOfTasks = tasks.split(",")
    with open(file, 'a') as f:
        for i in listOfTasks:
            f.write("\n    - {}".format(i))

    file2 = 'inventory'
    text2 = "[docker]"
    ports = port.split(",")
    with open(file2, 'w') as f2:
        f2.write(text2)
    count = 0
    with open(file2, 'a') as f2:
        for n in ports:
            count = count + 1
            f2.write(
                "\ndocker{} ansible_host={} ansible_port={}".format(count, ip, n))
    os.system(
        "ansible-playbook -v -i inventory playbook.yml")


main(ip, port, tasks)


# [docker]
# docker1 ansible_host=192.168.1.14 ansible_port=5555
# docker2 ansible_host=192.168.1.14 ansible_port=5556
# docker3 ansible_host=192.168.1.14 ansible_port=5557
# docker4 ansible_host=192.168.1.14 ansible_port=5558
# docker5 ansible_host=192.168.1.14 ansible_port=5559
