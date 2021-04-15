# :sparkles: Ansible-Setup :sparkles:

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

#

 <!--social media icon-->
<div align="center">
 
**If you're facing any issue in this setup, you can reach out me through the following handles**
 
[![Open Source Love](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/hackcoderr)
[![Linkedin Badge](https://img.shields.io/badge/-Sachin%20Kumar-blue?style=social&logo=Linkedin&logoColor=blue&link=https://www.linkedin.com/in/hackcoderr/)](https://www.linkedin.com/in/hackcoderr/) [![Twitter Badge](http://img.shields.io/badge/-@hackcoderr-1ca0f1?style=social&logo=twitter&logoColor=blue&link=https://twitter.com/hackcoderr)](https://twitter.com/hackcoderr) [![GitHub followers](https://img.shields.io/github/followers/hackcoderr?label=Follow&style=social)](https://github.com/hackcoderr/?tab=follow)
[![Instagram Badge](https://img.shields.io/badge/-hackcoderr-blue?style=social&logo=Instagram&link=https://www.instagram.com/hackcoderr/)](https://www.instagram.com/hackcoderr/) 
![Visitor Badge](https://visitor-badge.laobi.icu/badge?page_id=hackcoderr.hackcoderr)

</div>  

</br>
