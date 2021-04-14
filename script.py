import os
os.system("sudo pip3 install ansible")
os.system("sudo mkdir /etc/ansible")
os.system("sudo mv ansible.cfg /etc/ansible/")
os.system("sudo yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm -y")
os.system("sudo yum install sshpass -y")
