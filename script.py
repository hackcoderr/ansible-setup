import os,subprocess

os.system("sudo pip3 install ansible boto3 boto")
os.system("sudo mkdir /etc/ansible")
os.system("sudo mkdir -p /etc/ansible/hosts")
os.system("sudo mv ec2.py ec2.ini ansible.cfg ip.txt /etc/ansible/")
os.system("sudo chmod +x /etc/ansible/ec2.py")
os.system("sudo chmod +x /etc/ansible/ec2.ini")

operating_system = subprocess.getoutput('hostnamectl').split('\n')[6].split(':')[1]
#print(operating_system)

if 'Redhat' in operating_system or ':Amazon' in operating_system or 'Centos' in operating_system:
        os.system("sudo yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm -y")
        os.system("sudo yum install sshpass -y")
elif 'Ubuntu' in operating_system:
        os.system("sudo apt-get update -y")
        os.system("sudo apt-install openssh-server -y")
        os.system("sudo systemctl enable ssh -y")
        os.system("sudo apt-get install sshpass -y")
