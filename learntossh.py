#!/usr/bin/python3

import paramiko
import os

def commandissue(command_to_issue,sshsession):
    ssh_stdin,ssh_stdout,ssh_stderr=sshsession.exec_command(command_to_issue)
    return ssh_stdout.read()

def main():
    sshsession=paramiko.SSHClient()

    sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    mykey=paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")
    sshsession.connect(hostname="10.10.2.3", username="bender", pkey=mykey)

    mycommands=["touch sshworked.txt","touch create.txt","touch file3.txt","ls"]

    for i1 in mycommands:
        print(commandissue(i1,sshsession))

main()
        
