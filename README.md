# :sparkles: Ansible-Setup :sparkles:

This script is created for installing the Ansible Setup on **AWS Instance (Red Hat Enterprise Linux 8)**.

## Pre-requisite

* Python3
* Git

## Installation

* Install *Python3* and *Git* in your AWS instance.

 ```
 sudo yum install python3 git -y
 ```
 
 * Clone this directory
 
 ```
 git clone https://github.com/hackcoderr/Ansible-Setup.git
 ```
  
* Go inside *Ansible-Setup* directory.
```
cd Ansible-Setup/
```
 
* Run the *script.py* file.

```
python3 script.py
```

## Instructions

* Ansible configuration file location.
``/etc/ansible/ansible.cfg``

* Inventory file location in **ansible.cfg** 
``inventory=/etc/ansible/ip``

* Location of private key in **ansible.cfg** when you're using AWS Instance as a *Managed Node*

``private_key_file=/etc/keys/mykey.pem``

* To transfer the private key into controller node, you can use **winscp** software when you are working on **Windows** and you're using in **linux**, you can use  **scp** command.
* After transferring private key into controller node, you have to change the permission of key, otherwise you can face some permission issuse to access the managed node.
``chmod 400 private_key.pem``

**Note** : If you want to change private key and inventory file location, you can change.



you will need to install sshpass on the client server you are running your code in which is a tool that is not installed by default on most Linux distro

* if you are in Ubuntu use this command.
```
apt-get install sshpass
```
* on centOS/redhat use this install epel
```
wget https://archives.fedoraproject.org/pub/archive/epel/6/x86_64/epel-release-6-8.noarch.rpm
rpm -ivh epel-release-6-8.noarch.rpm
```

* install sshpass
```
yum --enablerepo=epel -y install sshpass
```
#

 <!--social media icon-->
<div align="center">
 
**If you're facing any issue in this setup, you can reach me out through the following handles**
 
[![Open Source Love](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/hackcoderr)
[![Linkedin Badge](https://img.shields.io/badge/-Sachin%20Kumar-blue?style=social&logo=Linkedin&logoColor=blue&link=https://www.linkedin.com/in/hackcoderr/)](https://www.linkedin.com/in/hackcoderr/) [![Twitter Badge](http://img.shields.io/badge/-@hackcoderr-1ca0f1?style=social&logo=twitter&logoColor=blue&link=https://twitter.com/hackcoderr)](https://twitter.com/hackcoderr) [![GitHub followers](https://img.shields.io/github/followers/hackcoderr?label=Follow&style=social)](https://github.com/hackcoderr/?tab=follow)
[![Instagram Badge](https://img.shields.io/badge/-hackcoderr-blue?style=social&logo=Instagram&link=https://www.instagram.com/hackcoderr/)](https://www.instagram.com/hackcoderr/) 
![Visitor Badge](https://visitor-badge.laobi.icu/badge?page_id=hackcoderr.hackcoderr)

</div>  

</br>
