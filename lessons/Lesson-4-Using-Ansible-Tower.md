# Lesson 4 - Using Ansible Tower

- [Lesson 4 - Using Ansible Tower](#lesson-4---using-ansible-tower)
    - [4.1 Understanding Ansible Tower, Automation Platform and AWX](#41-understanding-ansible-tower-automation-platform-and-awx)
      - [Understanding Ansible Automation Platform](#understanding-ansible-automation-platform)
    - [4.2 Installing Ansible Tower](#42-installing-ansible-tower)
      - [Tower Installation Requirements](#tower-installation-requirements)
      - [Installing Ansible Tower](#installing-ansible-tower)
    - [4.3 Understanding Ansible Tower Main Components](#43-understanding-ansible-tower-main-components)
      - [Managing Machines with Tower](#managing-machines-with-tower)
      - [Understanding Tower Main Components](#understanding-tower-main-components)
    - [4.4 Setting up Ansible Tower to Manage Assets](#44-setting-up-ansible-tower-to-manage-assets)
      - [Understanding the Tower Workflow](#understanding-the-tower-workflow)
    - [4.5 Configuring Ansible Tower to Manage Windows](#45-configuring-ansible-tower-to-manage-windows)
      - [Managing Windows with Ansible Tower](#managing-windows-with-ansible-tower)
      - [Understanding Windows Become](#understanding-windows-become)
      - [Managing Windows with Ansible Tower](#managing-windows-with-ansible-tower-1)
    - [Lesson 4 Lab Setting up Ansible Tower to Manage Assets in Ansible](#lesson-4-lab-setting-up-ansible-tower-to-manage-assets-in-ansible)
    - [Lesson 4 Lab Solution Setting up Ansible Tower to Manage Assets in Ansible](#lesson-4-lab-solution-setting-up-ansible-tower-to-manage-assets-in-ansible)

### 4.1 Understanding Ansible Tower, Automation Platform and AWX

- Ansible Tower is a Red Hat web-based platform that manages Ansible from a web interface.
- Ansible Tower adds some features that are not integrated in Ansible Engine, the command line version of Ansible.
  - Role-Based Access Control.
  - Caching of passwords.
  - Workflow designer.
- AWX is the open-source upstream of Ansible Tower

#### Understanding Ansible Automation Platform

- Ansible Automation Platform is a Red Hat solution that bundles different Ansible Components.
  - Ansible Engine: the command line version of Ansible.
  - Ansible Tower: the web-based Ansible management interface.
  - Content Collections: packages that bundle modules, roles and more.
  - Automation Hub: a platform that hosts certified collections for Ansible.
  - Automation Analytics: integrated Red Hat insights for advanced Ansible management and analysis.
- https://console.redhat.com

### 4.2 Installing Ansible Tower

#### Tower Installation Requirements

- Free evaluation licenses are available from Red Hat.
  - Download the tar-ball.
  - Request an evaluation license or use your Red Hat developer subscription (developers.redhat.com).
- The Ansible Tower (AWX) machine
  - 8 (4) GB RAM
  - 4 (2) vCPUs
  - 40 (20) GB disk space
  - Red Hat Enterprise Linux or CentOS Stream

#### Installing Ansible Tower

- **wget https://releases.ansible.com/ansible-tower/setup/ansible-tower-setup-latest.tar.gz**
- Extract the evaluation version tar-ball.
- Modify all password fields in the inventory file.
- **sudo ./setup.sh**
- Will take about 15 minutes to complete.
- Log in to the web UI: https://localhost
- Log in with your Red Hat credentials or provide the credentials file.

```bash
wget https://releases.ansible.com/ansible-tower/setup/ansible-tower-setup-latest.tar.gz
tar xvf ansible-tower-setup-latest.tar.gz
cd ansible-*
vim inventory # Update the password every where as `password`
sudo ./setup.sh
# Navigate to https://localhost
un: admin
pw: password
```

### 4.3 Understanding Ansible Tower Main Components

#### Managing Machines with Tower

- To reach out to managed machines with Tower, things are not really different from managing machines with Ansible Engine from the command line.
- Identifying the managed machines.
  - On the Tower, setup /etc/hosts name resolving (or DNS)
- On the managed machines
  - Ensure sshd is running and accepts incoming connections (firewall)
  - Need a user account with sudo privileges
  - Need to set up password / SSH keys

#### Understanding Tower Main Components

- Organization: a collection of managed devices.
- Users: administrative users that can be granted access to specifi tasks.
- Inventories: managed servers. Can be created statically or dynamically
  - Click **Settings > License** check **Host Remaining**
- Credentials: credentials that are used to log in to a managed machines. Think of user with sudo privileges.
- Project: a collection of playbooks obtained from a certain location (such as GitHub)
- Template: the job definition with all of its parameters. Must be launched or scheduled.

### 4.4 Setting up Ansible Tower to Manage Assets

#### Understanding the Tower Workflow

- (optional) Define an Organization.
- Create an Inventory.
- Configure Credentials.
- Set up a Project.
- Define a Job Template.
- Run the Job.
   
```bash
ansible tower -m copy -a "src=/etc/hosts dest=/etc/hosts"
ansible tower -a "cat /etc/hosts'
# Log in to Ansible Tower Machine.
su - anisble
ssh-keygen;
enter;
enter;
ssh-copy-id ansible1
ssh-copy-id ansible2
```

- Naviage to **https://localhost**
  - username: admin
  - passowrd: password
- Use develoerps login credentails to login to the Ansible Tower Dashboard.
- **Inventories** 
  - DETAILS 
    - click on **Plus**
    - Choose **inventory**
    - NAME: **my-inventory**
  - HOSTS
    - Click on **Plus**
    - HOST NAME: **ansible1.example.com**
    - Click **SAVE**
    - Repeat above steps to add **ansible2.example.com** 
- **Credentails**
  - DETAILS
    - NAME: **my-credentials**
    - ORGANIZATION: **Default**
    - CREDENTIAL TYPE: choose pagination **3** 
      - Choose **Machine**
      - Choose **SELECT**
  - TYPE DETAILS
    - USERNAME: **ansible**
    - PASSWORD: **password**
    - PRIVILEGE ESCALATION METHOD: **sudo**  
    - PRIVILEGE ESCALATION USERNAME: **root**
    - PRIVILEGE ESCALATION PASSWORD: **password**
    - Choose **SAVE**
- **Projects** 
  - Choose **Plus** icon
  - NAME: my-project
  - ORGANIZATION: **Default**
  - SCM TYPE: Git
    - SCM URL: https://github.com/anilitblr/tower
    - Choose **SAVE**
- **Templates**
- Choose **Plus** icon
- Choose **Job Template**
  - NAME: **my-template**
  - JOB TYPE: **Run**
  - INVENTORY: **my-inventory**
    - Choose **SELECT**
  - PROJECT: **my-project**
    - Choose **SELECT**
  - PLAYBOOK: Choose **vsftpd.yml**
  - CREDENTIALS: **my-credentials**
    - Choose **SELECT** 
  - OPTIONS: Choose **ENABLE PRIVILEGE ESCALATION**
  - Choose **SAVE**
  - Choose **LAUNCH**

### 4.5 Configuring Ansible Tower to Manage Windows

#### Managing Windows with Ansible Tower

- Ansible Tower can be used to manage many assets, including Windows.
- There are no credentials though that allow you to specify that **winrm** needs to be used as the remote connection mechanism.
- To manage Windows, you create a Windows specific inventory, with Variables set on that inventory.
  - ansible_connection: winrm
  - ansible_port: 5986
  - ansible_winrm_server_cert_validation: ignore
  - optional: ansible_winrm_transport: credssp

#### Understanding Windows Become

- To manage Linux, you need privilege escalation.
- To manage Windows, you need to have a user with Administrator privileges.
- If tasks are executed using such a user account, privilege escalation does not have to be disabled.

#### Managing Windows with Ansible Tower

- Next make sure that Windows is in a manageable state, as described in lesson 1.
- Create machine credentials to log in as the Windows based ansible user, using a password (NOT an SSH key)
- Next, you will be able to run playbook against Windows.
- - **Inventories** 
  - DETAILS 
    - click on **Plus**
    - Choose **inventory**
    - NAME: **winventory**
    - Click **SAVE**
  - HOSTS
    - Click on **Plus**
    - HOST NAME: **windows.example.com**
    - Click **SAVE**
  - GROUPS
    - Click on **Plus** 
    - NAME: win
    - Click **SAVE**
  - HOSTS
    - Click on **Plus** 
    - Choose **windows.example.com**
    - Choose **SAVE**
  - HOSTS
  - Update following variable under **VARIABLES**
    ```bash
    ansible_connection: winrm
    ansible_winrm_server_cert_validation: ignore
    ```  
- **Credentails**
  - DETAILS
    - NAME: **win-credentials**
    - ORGANIZATION: **Default**
    - CREDENTIAL TYPE: choose pagination **3** 
      - Choose **Machine**
      - Choose **SELECT**
  - TYPE DETAILS
    - USERNAME: **ansible**
    - PASSWORD: **password**
    - Choose **SAVE**
- **Projects** 
  - Choose **Plus** icon
  - NAME: my-project
  - ORGANIZATION: **Default**
  - SCM TYPE: Git
    - SCM URL: https://github.com/anilitblr/tower
    - Choose **SAVE**
- **Templates**
- Choose **Plus** icon
- Choose **Job Template**
  - NAME: **win-template**
  - JOB TYPE: **Run**
  - INVENTORY: **winventory**
    - Choose **SELECT**
  - PROJECT: **my-project**
    - Choose **SELECT**
  - PLAYBOOK: Choose **playbook.yml**
  - CREDENTIALS: **win-credentials**
    - Choose **SELECT** 
  - Choose **SAVE**
  - Choose **LAUNCH**

### Lesson 4 Lab Setting up Ansible Tower to Manage Assets in Ansible

- Install Ansible Tower on RHEL 8.
- Add a new CentOS 7 based virtual machine and configure it so that Ansible Tower can manage it.
- Set up Tower to use the course Git repository at http://github.com/anilitblr/tower
- Use Ansible Tower to run the **run_and_test_httpd.yaml** playbook on the new CentOS host.

### Lesson 4 Lab Solution Setting up Ansible Tower to Manage Assets in Ansible

- Follow the above docs to complete the lab.
