# Lesson 16 - Managing AWS with Ansible

- [Lesson 16 - Managing AWS with Ansible](#lesson-16---managing-aws-with-ansible)
    - [16.1 Understanding Requirements for Managing AWS](#161-understanding-requirements-for-managing-aws)
      - [Configuring AWS Access](#configuring-aws-access)
      - [Checking Your Region](#checking-your-region)
      - [Installing boto on the Control Node](#installing-boto-on-the-control-node)
      - [Preparing Instance Access](#preparing-instance-access)
    - [16.2 Using Playbooks to Manage AWS](#162-using-playbooks-to-manage-aws)
      - [Understanding Cloud Management](#understanding-cloud-management)
      - [Configuring EC2 Vault-based Access](#configuring-ec2-vault-based-access)
      - [Provisioning Instances](#provisioning-instances)
      - [Testing Instance Access](#testing-instance-access)
      - [Managing EC2 Instances](#managing-ec2-instances)
    - [16.3 Configuring Dynamic Inventory](#163-configuring-dynamic-inventory)
      - [Configuring Dynamic Inventory](#configuring-dynamic-inventory)
      - [Sample Dynamic Inventory File](#sample-dynamic-inventory-file)
      - [Enabling the AWS EC2 Plugin](#enabling-the-aws-ec2-plugin)
    - [Lesson 16 Lab Managing AWS with Ansible](#lesson-16-lab-managing-aws-with-ansible)
    - [Lesson 16 Lab Solution Managing AWS with Ansible](#lesson-16-lab-solution-managing-aws-with-ansible)

### 16.1 Understanding Requirements for Managing AWS

#### Configuring AWS Access

- Go to aws.amazon.com
- Select IAM -> Users -> Create User
- Give the new user a name, and select "Access Key" as the access type.
- When setting up Permissions, attach the Admin access policy.
- No further configuration required, create the user and note the Access Key ID and the secret Access Key.

#### Checking Your Region

- All activity in EC2 happens in a specific region.
- The region determines which Amazon datacenters you are using.
- Sele the region in the upper left corner of https://console.aws.amazon.com and make sure your playbook match that region.

#### Installing boto on the Control Node

- To access AWS, you need to install the Python Boto libraries on the control node.
  - **sudo pip3 install boto boto3**

#### Preparing Instance Access

- To configure instance access, you need an SSH key pair.
- From the Ansible Control machine, go to EC2 dashboard -> Key pairs > Create key pair.
- Save the .pem file to .ssh in your home directory.
- Use the key pair name in your playbook: **key_name: instancekey**

### 16.2 Using Playbooks to Manage AWS

#### Understanding Cloud Management

- Ansible can be used to manage all aspects of cloud; infrstructure as well as instances in an existing infrastructure.
- In this demo we will focus on managing instances in an existing infrastructure.
- But remember that a complete could environment can be set up automatically using Ansible.

#### Configuring EC2 Vault-based Access

- Create a project directory: **mkdir -p ec2/group_vars/all**
- Create a valut encrypted file containing the AWS credentials.
  - **ansible-vault create group_vars/all/keys.yml**
    - **aws_access_key: xxxxxxxxxx**
    - **aws_secret_key: xxxxxxxxxx**
- Create a playbook according to **list-instances.yml**
  - Change region to your region if needed.
- Run the playbook, using **ansible-playbook --ask-valut-pass list.instances.yml** (may not show anything yet).
```bash
cd ec2/
ansible-vault --help
ansible-vault encryp group_vars/all/keys.yml
vim list-instances.yml
ansible-playbook --ask-vault-pass list-instances.yml
``` 

#### Provisioning Instances

- To create instances, you need an AMI instance ID.
- Get this from the EC2 console > Instances.
- Select Public Images and search for an instance (like Ubuntu 20.04)
- Notice that the result may be overwhelming.
- Create a playbook according to **ubuntu-new.yaml** and run it.
  - **ansible-playbook --ask-vault-pass ubuntu-new.yaml**
```bash
cd ec2/
vim ubuntu-new.yaml
ansible-playbook --ask-vault-pass ubuntu-new.yaml
ls /home/ansible/vaultpw
ansible-playbook --help | grep vault
ansible-playbook --ask-password-file ~/vaultpw ubuntu-new.yaml
```

#### Testing Instance Access

- Use **ansible-playbook --ask-vault-pass list-instances.yml** to list intances, including the DNS name.
- From the command line, use **ssh -i mykey.pem <ec2-public-ip-address>** to test shell access to the instance.

#### Managing EC2 Instances

- After setting up Ansible EC2 connections, may modules are available to do many things.
  - List instance facts: use **amazon.ec2.ec2_instance_info**
  - Terminate instances.
    - **aws configure; aws ec2 describe-instances --region us-west-2 | grep InstanceId** (is not Ansible but might be easier).
    - **ansible localhost -m ec2 -a "instance_id=i-1234 state=absent region=us-west-2"**
  - Manage keys: **amazon.ec2.ec2_key**
  - Manage Security Groups: **amazon.ec2.ec2_group**

### 16.3 Configuring Dynamic Inventory

#### Configuring Dynamic Inventory

- Dynamic inventory is provided as an Ansible Plugin.
- Using Python scripts as dynamic inventory is old school.
- Using AWS dynamic inventory requires you to use a YAML file that is in /opt/ansible/inventory/aws_ec2.yaml
- Don't EVER store this file in your Git repo as it contains sensitive information.
- You will next need to enable the plugin in **ansible.cfg**

#### Sample Dynamic Inventory File

```yaml
---
plugin: aws_ec2
aws_access_key: xxxxxxxxxx
aws_secret_key: xxxxxxxxxx
keyed_groups:
  - key: tags
    prefix: tag
regions:
- us-west-2
```

#### Enabling the AWS EC2 Plugin

- To use the dynamic inventory configuration, edit ansible.cfg in the project directory to enable the aws_ec2 plugin and define iventory to use.
```ini
[defaults]
inventroy=/opt/ansible/inventroy/aws_ec2.yaml

[inventory]
enable_plugins = aws_ec2
```
- Then test, using **ansbile-inventory -i /opt/ansible/inventroy/aws_ec2.yaml --list**
  - If the vault variables are in ./group_vars, you will need to add **--ask-vault-pass**
```bash
mkdir -p /opt/ansible/inventory 
sudo vim /opt/ansible/inventory/aws_ec2.yaml

# Add below content.
---
plugin: aws_ec2
aws_access_key: xxxxxxxxxx
aws_secret_key: xxxxxxxxxx
keyed_groups:
  - key: tags
    prefix: tag
regions:
- us-west-2
# Save and close the file.
ansible-doc -t inventory -l
ansible-doc -t inventory aws_ec2

vim ansible.cfg

[defaults]
inventroy=/opt/ansible/inventroy/aws_ec2.yaml

[inventory]
enable_plugins = aws_ec2

- Save and close the file.
ansbile-inventory --list --vault-password-file=~/vaultpw 
```

### Lesson 16 Lab Managing AWS with Ansible

- Remove the AWS instances that you have created earlier in this lesson.

### Lesson 16 Lab Solution Managing AWS with Ansible

```bash
cd ec2
vim remove-instances.yml
ansible-playbook --vault-password-file=~/vaultpw remove-instances.yml
ansible-playbook --vault-password-file=~/vaultpw list-instances.yml
```
