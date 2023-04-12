# :sparkles: Ansible-Setup :sparkles:

**Tested on:**
 
![RHEL](https://img.shields.io/badge/Red%20Hat-EE0000?style=for-the-badge&logo=redhat&logoColor=white)
![centos](https://img.shields.io/badge/Cent%20OS-262577?style=for-the-badge&logo=CentOS&logoColor=white)
![ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
![amazon](https://img.shields.io/badge/Amazon_Linux-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)

**Structure**
```
.
├── ansible.cfg
├── keypair.pem
├── ec2.ini
├── ec2.py
└── hosts
```
## Freatures
* Installing and Configuring Ansible on multiple OS without knowing internal.
* Setting up Ansible for EC2 with Dynamic Inventory.

## Pre-requisite

* Python3
* Git

## Installation

Install ``Python3`` and ``Git`` on controller node.

```
sudo yum install python3 git -y       # for RHEL/Centos 
sudo yum install python3-pip -y
```

```
sudo apt install python3 git -y       # for ubuntu
sudo apt-get -y install python3-pip
```
 
Clone this repository and go inside it.
 
```
git clone https://github.com/hackcoderr/ansible-setup.git
cd ansible-setup/
```
  
 
Run the ``script.py`` file to install the ansible.

```
python3 script.py
```

## How to configure dynamic Inventory

Open ``ec2.ini`` file and give ``access key`` and ``secret key`` of your [AWS IAM User](https://www.techtarget.com/searchcloudcomputing/tutorial/Step-by-step-guide-on-how-to-create-an-IAM-user-in-AWS) at the bottom of ``ec2.ini`` file.

```
sudo vi /etc/ansible/ec2.ini
```


```
[credentials]

# The AWS credentials can optionally be specified here. Credentials specified
# here are ignored if the environment variable AWS_ACCESS_KEY_ID or
# AWS_PROFILE is set, or if the boto_profile property above is set.
#
# Supplying AWS credentials here is not recommended, as it introduces
# non-trivial security concerns. When going down this route, please make sure
# to set access permissions for this file correctly, e.g. handle it the same
# way as you would a private SSH key.
#
# Unlike the boto and AWS configure files, this section does not support
# profiles.
#
aws_access_key_id = AXXXXXXXXXXXXXX
aws_secret_access_key = XXXXXXXXXXXXXXXXXXX
```

## Test

Run to check your available hosts.
```
ansible all --list-hosts
```

Ping your instances through ``tags`` which running on your AWS Account.

```
ansible tag_Name_<tag_name> -m ping
# ansible tag_Name_testing_os -m ping
```

## Instructions

* Ansible configuration file location: ``/etc/ansible/ansible.cfg``

* Static Inventory file location: ``inventory=/etc/ansible/hosts``

* Dynamic Inventory file location: ``inventory=/etc/ansible/ec2.py``


* EC2 keypair location in ``ansible.cfg``. so transfer your keypair at the same location: ``private_key_file=/etc/keys/<keypair-name>.pem``


* For transferring the keypair into controller node,  use ``winscp`` software when you are working on ``Windows`` as local system and you're using in ``linux``, you can use  ``scp`` command.

After transferring keypair into controller node, you have to change the permission of key, otherwise you can face some permission issuse to access the managed node.

```
chmod 400 <keypair-name>.pem
```

## Troubleshoot
**Issue type: 1**

when default profile has keys not set.
```
 ERROR: "Forbidden", while: getting ElastiCache clusters
```
**Proposed Fix**

In my case i don't use Elasticache set the following in ``ec2.ini`` file
``'elasticache = False'`` and it completed sucessfully and listed all the instances

**Issue type: 2**

if you got this type of error, then it can be due to ansible user hasn't enough permission.
```
XXXXXXXX | UNREACHABLE! => {
    "changed": false,
    "msg": "Failed to connect to the host via ssh: Load key \"/etc/ansible/mykey.pem\": Permission denied\r\nec2-user@XXXXXXX: Permission denied (publickey,gssapi-keyex,gssapi-with-mic).",
    "unreachable": true
}
```
**Proposed Fix**

``` 
sudo ln -s /usr/local/bin/ansible /bin 
```
now run ansible command with ``sudo``.

**Encryption Issue**

```
ERROR: Ansible requires the locale encoding to be UTF-8; Detected ISO8859-1.
```

**Resolved**
```
export LC_ALL="en_US.UTF-8"
```

To permanently set the LC_ALL environment variable to en_US.UTF-8, you can add the following line to your shell's configuration file (e.g., .bashrc, .zshrc, etc.):

```
echo 'export LC_ALL="en_US.UTF-8"' >> ~/.bashrc
```
After saving the changes, you can either open a new terminal window or run the following command in the current terminal to apply the changes:
```
source ~/.bashrc
```
For more [details](https://stackoverflow.com/questions/65525716/why-do-i-get-a-locale-error-even-though-it-is-set)


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
