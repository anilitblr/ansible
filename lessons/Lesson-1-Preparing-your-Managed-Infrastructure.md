# Lesson 1 - Preparing your Managed Infrastructure

- [Lesson 1 - Preparing your Managed Infrastructure](#lesson-1---preparing-your-managed-infrastructure)
    - [1.1 Understanding Ansible](#11-understanding-ansible)
      - [Ansible and DevOps](#ansible-and-devops)
    - [1.2 Setting up the Ansible Control Node](#12-setting-up-the-ansible-control-node)
      - [Control Node Requirements](#control-node-requirements)
    - [1.3 Understanding Requirements for Managing Assets with Ansible](#13-understanding-requirements-for-managing-assets-with-ansible)
      - [Understanding Requirements](#understanding-requirements)
      - [Managed Nodes Requirements](#managed-nodes-requirements)
      - [Convenience versus Security](#convenience-versus-security)
    - [1.4 Configuring Inventory](#14-configuring-inventory)
      - [Understanding Inventory](#understanding-inventory)
    - [1.5 Understanding Ad-hoc Commands](#15-understanding-ad-hoc-commands)
      - [Understanding Ad-hoc Commands](#understanding-ad-hoc-commands)
      - [Understanding Modules Names](#understanding-modules-names)
      - [Modules for Setting up Managed Nodes](#modules-for-setting-up-managed-nodes)
    - [1.6 Understanding the Course Lab Environment](#16-understanding-the-course-lab-environment)
    - [1.7 Configuring Linux Managed Hosts with Ad-hoc Commands](#17-configuring-linux-managed-hosts-with-ad-hoc-commands)
      - [Setting up Managed Hosts](#setting-up-managed-hosts)
      - [Setting up Managed Nodes Tasks Overview](#setting-up-managed-nodes-tasks-overview)
      - [Demo: Setting up Managed Nodes](#demo-setting-up-managed-nodes)
      - [Demo: Setting up Managed Nodes](#demo-setting-up-managed-nodes-1)
    - [1.8 Setting up Privilege Escalation](#18-setting-up-privilege-escalation)
      - [Demo: Setting up Privilege Escalation](#demo-setting-up-privilege-escalation)
    - [1.9 Understanding ansible.cfg and Working with Settings](#19-understanding-ansiblecfg-and-working-with-settings)
      - [Working with Ansible Settings](#working-with-ansible-settings)
    - [1.10 Setting up Windows as a Managed Host](#110-setting-up-windows-as-a-managed-host)
      - [Setting up Windows as a Managed Host](#setting-up-windows-as-a-managed-host)
      - [Preparing a Windows Host](#preparing-a-windows-host)
      - [Configuring Authentication](#configuring-authentication)
      - [Preparing the Control Host](#preparing-the-control-host)
    - [Lesson 1 Lab Setting up an Ansible Managed Environment](#lesson-1-lab-setting-up-an-ansible-managed-environment)
    - [Lesson 1 Lab Solution Setting up an Ansible Managed Environment](#lesson-1-lab-solution-setting-up-an-ansible-managed-environment)

### 1.1 Understanding Ansible

- Ansible is a configuration management tool.
- It is used to mange configuration on a pre-deployed infrastructure.
- Stated otherwise: it is used to make sure that the current state of the managed asset meets the desired state as defined by Ansible.
- Comparable solutions are.
  - Puppet.
  - Chef.
  - SaltStack.
- Ansible stands out because it was designed with ease of use in mind.

#### Ansible and DevOps

- Ansible is a DevOps tool.
- It manages configuration as code.
- To do so, YAML playbooks are typically used.
- To guarantee consistency, the playbooks are often provided through Git.

### 1.2 Setting up the Ansible Control Node

#### Control Node Requirements

- The control node is where the Ansible software is installed.
- The Ansible software can be installed in different ways.
  - From the distribution repositories to get access to the latest stable software.
  - From the Python pip3 installer to get access to the latest and greatest.
- Notice that the latest and geratest in't always stable, which is why installing from the repositories is recommended.

```bash
# Install on RHEL 8.5
cat /etc/redhat-release
sudo dnf install epel-release; # epel: Extra packages for Enterprise Linux.
sudo dnf install -y ansible;
ansible --version;

# Install on Fedora
sudo dnf provides */pip;
sudo dnf install -y python3-pip;
sudo pip install ansible;
ansible --version;
```

### 1.3 Understanding Requirements for Managing Assets with Ansible

#### Understanding Requirements

- The Ansible control node is where the Ansible software is installed.
- Consider it an operator workstation, and not so much a server.
- Apart from the Ansible software, it needs Python and access to the Ansible playbook, typically throught Git.
- Managed nodes are assets that are manged with Ansible.
- This can be computers running Windows or Linux, cloud instances, virtual machines, containers and much more.

#### Managed Nodes Requirements

- Remote access: SSH is default specific platforms have other options.
- A dedicated user account, for convenience use the same user account throughout.
- Configured privilege escalation to install software, change configuration files and more tasks requiring administrator privilege.

#### Convenience versus Security

- For convenient management.
  - Use SSH keys for passwordless connection to remote hosts.
  - Use passwordless privilege escalation.
- For secure management
  - Use **-k** command line option to prompt for SSH password.
  - Use **-K** command line option to prompt for privilege escalation password.
- For convenient and secure management
  - Consider using Ansible Tower, which allows you to cache passwords.

### 1.4 Configuring Inventory

#### Understanding Inventory

- DNS or /etc/hosts are generic solutions that provide hostname to IP address resolving.
- Ansible also needs an inventory.
  - To identify managed hosts.
  - To define host groups to be used by Ansible.
  - To define variables (considered deprecated)
- Default inventory is in /etc/ansible/hosts
- Project-based inventory is common, and inventory files can be referred to using the **-i inventoryfilename** command line option.

### 1.5 Understanding Ad-hoc Commands

#### Understanding Ad-hoc Commands

- An Ansible ad-hoc command is a command-line-only solution to perform specific tasks.
- It is always recommended to use the most specific module you can find, as generic modules are not idempotent.
- With over 3,000 modules available, it isn't always easy to find the best possible module.

#### Understanding Modules Names

- Since Ansible 2.10, modules are a part of collections.
- To refer to module names in Ansible 2.10 and later, a Fully Qualifed Collection Name (FQCN) is used, like **ansible.builtin.command**
- In Ansible 2.9 and earlier, only the last part of this name was used.
- In this course, we'll use FQCN's as the default way to refer to modules in the slides.
- When working with Ansible 2.9 and earlier, only use the last part of the FQCN to refer to the module.
- As Red Hat at the time of writing this was using Ansible 2.9, in all code example you will find the short module names.
- See lesson 8.1 for more detailed infomation about collections.

#### Modules for Setting up Managed Nodes

- **ansible.buitin.command** is a generic module that allows you to run any command using Ansible.
- **ansible.buitin.shell** is like **ansible.buitin.command**, but uses a bash shell, which allows you to run shell features like pipes and redirects.
- **ansible.buitin.user** is a specific module for managing user accounts.
- **ansible.buitin.copy** is used to copy files.

### 1.6 Understanding the Course Lab Environment

- Control machine
  - Rocky Linux 8.5
    - Ansible 2.9
  - Fedora 35
    - Ansible 1.12.0
- Managed nodes
  - Rocky Linux 8.5 (ansible1)
  - Rocky Linux 8.5 (ansible2)
  - Ubuntu LTS
  - CentOS
  - Cloud   
    - aws
    - azure
  - ESXi
  - Cisco switch

### 1.7 Configuring Linux Managed Hosts with Ad-hoc Commands

#### Setting up Managed Hosts

- If a host meets the following minimal requirements, you can use Ansible to take care of further configuration.
  - SSH is running and reachalbe.
  - There is a user with administrative privileges.
- Ansible ad-hoc commands can be used to configure managed hosts in an easy way.

#### Setting up Managed Nodes Tasks Overview

- Ensure SSH is running on the hosts.
- Include Host Names in Inventory.
- Create the ansible user on managed nodes.
- Set a password for this user.
- Configure SSH key-based login.
  - ssh-keygen
  - ssh-copy-id
- Configure Privilege escalation

#### Demo: Setting up Managed Nodes

- Make sure you have an Ubuntu Server LTS 20.04 or later, as well as a Rocky Linux 8.5 or later node with SSH available and /etc/hosts name resolving set up.
- Create a file with the name **inventory** and the following contents.
```file
ubuntu 
ansible1
ansible2
```
- To set up Ubuntu with a user with the name **ansible**, use the following command (assuming that the Ubuntu machine has a sudo enabled user **student**)
  - **ansible -i inventory ubuntu -m user -a "name=ansible create_home=yes" -u student -b -k -K**
- Install SSH Server on Ubuntu.
  - **sudo apt-get install openssh-server**
- On control node
```bash
cd playbooks/lesson1/
vi inventory

ansible -i inventory ubuntu -m user -a "name=ansible create_home=yes" -u student -b -k -K
```

#### Demo: Setting up Managed Nodes

- To set up Rocky with a user with the name **ansible**, use the following command  (assuming that the Rocky machine has direct root access)
  - **ansible -i inventory ansible1 -m user -a "name=ansible" -u root -k**
- Next, you will need to set passwords for the user. For now, do that as follows.
  - **ansible -i inventory ubuntu -m shell -a "echo 'ansible:password' | chpasswd" -u student -b -k -K**
  - **ansible -i inventory ansible1 -m shell -a "echo password | passwd --stdin ansible" -u root -k**
- Now, using the local user ansible, create an SSH key pair and press enter on all questions asked.
  - **ssh-keygen**
- Use **ssh-copy-id** to copy the pairs to the managed nodes.
  - **ssh-copy-id ubuntu; ssh-copy-id ansible1; ssh-copy-id ansible2**
- Time for testing.
  - **ansible -i inventory all -m command -a "id" -u ansible**

### 1.8 Setting up Privilege Escalation

- To securely escalte privileges, use the **-b -K** command line options
- To conveniently escalate privileges, consider configuring passwordless sudo.
- To do so with Ansible, create a sudo configuration file locally.
- Next, use the ansible copy module to copy the configuration file to managedn nodes.

#### Demo: Setting up Privilege Escalation

```bash
echo 'ansible ALL=(ALL) NOPASSWD: ALL' > /tmp/sudoers;
sudo cp /tmp/sudoers /etc/sudoers.d/ansible;
sudo ls -l /root;
ansible rocky -i inventory -u root -k -m copy -a "src=/tmp/sudoers dest=/etc/sudoers.d/ansible";
ansible ubuntu -i inventory -u student -k -b -K -m file -a "path=/etc/sudoers.d state=directory";
ansible ubuntu -i inventory -u student -k -b -K -m copy -a "src=/tmp/sudoers dest=/etc/sudoers.d/ansible";
ansible -i inventory all -m command a "ls -l /root";
ansible -i inventory all -m command a "ls -l /root" -b;
```

### 1.9 Understanding ansible.cfg and Working with Settings

#### Working with Ansible Settings

- While managing assets with Ansible, you will need to provide different settings.
- Settings can be provided at different levels.
  - On the command line.
  - In playbooks (covered later)
  - In ansible.cfg
- A default ansible.cfg is provided in /etc/ansible/ansible.cfg
- Specific ansible.cfg files can be created in project directories.
- Settings that are made at a more specific level will always overwrite the generic settings.

```bash
vim /etc/ansible/ansible.cfg;
ansible --version;
cd playbooks
vim ansible.cfg
ansible all -m command a "ls -l /root";
```

### 1.10 Setting up Windows as a Managed Host

#### Setting up Windows as a Managed Host

- Ansible can manage all Windows versions from Windows 7 and Windoes 2008.
- In Ansible, a specific set of modules is provided to manage Windows assets.

#### Preparing a Windows Host

- Install Windows 2019 server standard (180 day eval version will do), ensure there is a Windows user with admin privileges.
- Log in as user with Administrator privileges.
- Open powershell: **winrm quickconfig**
- Set up WinRM, using the script that is provided on
  - https://docs.ansible.com/ansible/latest/user_guide/windows_setup.html
- Verify using **winrm enumerate winrm/config/Listener** and verify that http and https listeners are available.
- In Windows control panel, create Ansible user, set password and make this user an Administrator.

#### Configuring Authentication

- Windows supports different authentication protocols.
- If authentication has been configured to a strict protocol on Windows, you may have to set up Ansible accordingly.
  - Basic: only supports local accounts - do not use.
  - Certificate: only supports local accounts - do not use.
  - Kerberos: only works for AD accounts.
  - NTLM: works for local and AD accounts.
  - CredSSP: offers best support for local and AD accounts.
- Use **ansible_winrm_transport: credssp** (or anything else) if you have authentication issues.

#### Preparing the Control Host

- On Ansible control, create windows project directory with an ansible.cfg and an inventory (see playbooks/windows for example)
- Set up /etc/hosts for host name resolution to the Windows box - notice that Windows firewall disallows ping incoming.
- On Ansible control: **sudo pip3 install pywinrm**
- On Ansible control: **ansible win -i inventory -m win_ping**
  - Make sure the passwords match!
- Check facts: **ansible win -i inventory -m setup**

```bash
sudo dnf search python | grep pip;
sudo dnf install -y python3-pip;
sudo pip3 install pywinrm;
cd windows/
vim inventory
vim ansible.cfg;
ansible win -m win_ping;
```

### Lesson 1 Lab Setting up an Ansible Managed Environment

- Set up an Ansible Managed Environment, with the following itesm.
  - A control node, running the latest version of Rocky Linux.
  - One managed node, running the latest version of Rocky Linux.
  - One managed node, running the latest LTS version of Ubuntu.
  - One managed node, running the evaluation version of Windows 2019. 

### Lesson 1 Lab Solution Setting up an Ansible Managed Environment

- Follow the lesson1 docs to complete this lab.
