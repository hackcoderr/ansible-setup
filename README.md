# Ansible-Setup
This script is created for installing the Ansible Setup on **AWS Instance (Red Hat Enterprise Linux 8)**.

## Pre-requisite

* Python3
* Git

## Installation

* Install *Python3* and *Git* in your AWS instance.

 > _sudo yum install python3 git -y_
 
 * Clone this directory
 
 > _git clone https://github.com/hackcoderr/Ansible-Setup.git_
  
* Go inside *Ansible-Setup* directory.

> _cd Ansible-Setup/_
 
* Run the *script.py* file.

> _python3 script.py_

## Instructions

* Ansible configuration file location.
> _/etc/ansible/ansible.cfg_

* Inventory file location in **ansible.cfg** 
> _inventory=/home/ec2-user/ip.txt_

* Location of private key in **ansible.cfg** when you're using AWS Instance as a *Managed Node*
> _private_key_file=/home/ec2-user/mykey.pem_

* To transfer the private key into controller node, you can use **winscp** software when you are working on **Windows** and you're using in **linux**, you can use  **scp** command.
* After transferring private key into controller node, you have to change the permission of key, otherwise you can face some permission issuse to access the managed node.
> _chmod 400 private_key.pem_

**Note** : If you want to change private key and inventory file location, you can change.
