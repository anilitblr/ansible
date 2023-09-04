# Lesson 8 - Using Roles and Collections

- [Lesson 8 - Using Roles and Collections](#lesson-8---using-roles-and-collections)
    - [8.1 Understanding Collections](#81-understanding-collections)
      - [Understanding Collections](#understanding-collections)
      - [Understanding Collection Naming](#understanding-collection-naming)
    - [8.2 Understanding Roles](#82-understanding-roles)
      - [Understanding Roles](#understanding-roles)
      - [Understanding Task Execution Order](#understanding-task-execution-order)
    - [8.3 Working with Galaxy](#83-working-with-galaxy)
      - [Understanding Galaxy](#understanding-galaxy)
    - [8.4 Using Collections](#84-using-collections)
      - [Using Collections in Playbooks](#using-collections-in-playbooks)
      - [Using Collections](#using-collections)
      - [Getting Collections Information](#getting-collections-information)
      - [Listing Collections](#listing-collections)
      - [Demo: Using Ansible Collections](#demo-using-ansible-collections)
    - [8.5 Using Collections from Automation Hub](#85-using-collections-from-automation-hub)
      - [Using Collection Sources](#using-collection-sources)
      - [Using Collections from Automation Hub](#using-collections-from-automation-hub)
      - [Using Collections from Automation Hub](#using-collections-from-automation-hub-1)
    - [8.6 Creating your own Roles](#86-creating-your-own-roles)
    - [Lesson 8 Lab Working with Roles and Collections](#lesson-8-lab-working-with-roles-and-collections)
    - [Lesson 8 Lab Solution Working with Roles and Collections](#lesson-8-lab-solution-working-with-roles-and-collections)

### 8.1 Understanding Collections

#### Understanding Collections

- Collections are a new way to bundle Ansible contents to make it more manageable.
- Collections can have different sources, including Ansible community and Red Hat partners.
- Collections may contain the following.
  - **modules** that provide the Ansible core functionality.
  - **roles** than can be included in playbooks for common task execution.
  - **plugins** that extend the Python code on the Ansible control host.

#### Understanding Collection Naming

- Collections have a Fully Qualified Collection Name (FQCN), such as **ansible.netcommon**.
- Within this SQCN, plugins, modules etc, are addressed with their own name, such as **ansible.netcommon.cli_command**
- Before collections, you would address just a module name such as **user**, now you address this module as **ansible.builtin.user**
- So using collections involves a lot more typing.
- No! Just start with a **collections** setting in the play header and list all collections you're going to use.
```bash
ansible --version # Make sure installed version is 2.12.1
cd collections/
vim enforce-selinux.yml
ansible-playbook enforce-selinux.yml

vim enforce-selinux-simplified.yml
ansible-playbook enforce-selinux-simplified.yml
```

### 8.2 Understanding Roles

#### Understanding Roles

- Roles are community-provided resources that make working with Ansible easier.
- They provide standardized solutions for common tasks.
- Instead of fidning out yourself, you can use community-provided roles in your playbooks.
- Just add the site-specific configuration using variables in the playbook, and run everything else from the roles.
- Custom roles can also be provided.

#### Understanding Task Execution Order

- Tasks in roles are normally executed before other tasks in the playbook.
- Use **pre_tasks** to execute tasks before the role.
- Handlers that are triggered by **pre_tasks** are also executed before the role.
```bash
cd roles
vim nginx-role.yml;
ansible-galaxy --help
ansible-galaxy role install geerlingguy.nginx
ansible-playbook nginx-role.yml
```

### 8.3 Working with Galaxy

#### Understanding Galaxy

- galaxy.ansible.com is the community website that provides access to roles and collectins.
- While using galaxy, you can find the required commands to install roles and collections easily.
- **ansible-galaxy** is the command line interface that allows you to work with Galaxy.
- Use **ansible-galaxy collection** it manage collections.
- Use **ansible-galaxy role** to manage roles.
```bash
ansible-galaxy role -h;
ansible-galaxy role list;
cd /home/ansible/.ansible/roles/
cd geerlingguy.nginx/
ls;
tree;
cd tasks
vim main.yml
```

### 8.4 Using Collections

#### Using Collections in Playbooks

- In the play header, the **collections** keyword can be used.
- It takes a list of collections as it argument.
- After using the **collections** keyword, the collection itself can be addressed the old way: **selinux** instead of **ansible.posix.selinux**
- See **enforce-selinux-simplified.yml** for an example.
- See **enforce-selinux.yml** for an alternative example

#### Using Collections

- In Ansible 2.9, collections are NOT a default part of Ansible.
- To use them, they need to be installed from Ansible Galaxy.
- To install multiple collections, consider using a requirements file.
- **ansible-galaxy collection install -r requirements.yml**
- See **collections/requirements.yml** for an example
- In Ansible 2.10 and later, collections are installed by default.

#### Getting Collections Information

- Ansible 2.10 and later contain better collection integration.
  - Collection names can easily be found using **ansible-doc; ansible-doc -l | grep aws**
- Ansible 2.9 shows only collections that have been installed.
  - Collections are not listed with **ansible-doc -l**
  - Collection documentation is available while addressing collection components directly.

#### Listing Collections

- Use **ansible-galaxy collection list** (2.10 or later) to show a  complete list of collections.
- To verify the contents of the collection, access it's physical location and investigate the directory structure.

#### Demo: Using Ansible Collections

```bash
# Install posix from the collections.
ansible-galaxy collection install ansible.posix;

# Install posix from the tartall on version 2.9.
wget https://galaxy.ansible.com/download/ansible-posix-1.5.4.tar.gz
cd ~/Downloads
ls ~/.ansible/collections/ansible_collections/
cp ansible-posix-1.5.4.tar.gz ~/.ansible/collections/ansible_collections/ 
cd ~/.ansible/collections/ansible_collections/
tar xvf ansible-posix-1.5.4.tar.gz
mkdir -p ansible/posix
mv * ansible/posix
cd ansible/posix
tree

# See posix docs.
ansible-doc ansible.posix.selinux;
ansible-doc ansible.posix.acl;
```

### 8.5 Using Collections from Automation Hub

#### Using Collection Sources

- Community collections are provided through Ansible Galaxy.
- Subscription-only collections are through https://cloud.redhat.com/ansible/automation-hub
  - Automation Hub contains collections from Red Hat, but also partner collections.
  - Go to **https://cloud.redhat.com/ansible/automation-hub/token** to get an authentication token that is needed for using collections; this token needs to be stored in the ansible.cfg file.

#### Using Collections from Automation Hub

- Get a token: **https://cloud.redhat.com/ansible/automation-hub/token**
- Select **Automation Hub > Connect to Hub > Load token** and copy the token.
```bash
# Edit ansible.cfg to include the galaxy server and token.
vim ansible.cfg 

# update the below content to the file.
[galaxy_server.automation.hub]
url=https://cloud.redhat.com/api/automation-hub/
auth_url=https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token
token=xxxxxxxxx

[galaxy_server.release.galaxy]
url=https://galaxy.ansible.com
token=xxxxxxxxx

save and close the file.
```

#### Using Collections from Automation Hub

- To install collections from Automation Hub, create a requirements.yml file.
```yaml
collections:
# - name: junipernetworks.junos
# source: https://galaxy.ansible.com
- name: f5networks.f5_modules
  source: https://cloud.redhat.com/api/automation-hub/  
```
- Install, using the requirements.yml file.
```bash
ansible-galaxy collection install -r collections/requirements.yml
```
- Use **ansible-galaxy collections -l** to show a list of currently installed collections.
```bash
cd collections/ 
vim requirements.yml
ansible-galaxy collection install -r collections/requirements.yml
ansible-doc -l | grep openshift;
```

### 8.6 Creating your own Roles

```bash
cd roles
ls roles
cd roles
# Initiate a role.
ansible-galaxy role init myrole
tree myrole;
cd motd
ls
vim meta/main.yml; # Set `min_ansible_version: 2.8`
vim tasks/main.yml;
vim template/motd.j2
vim defaults/main.yml
vim motd-role.yml
ansible-playbook motd-role.yml
ansible ansible2 -a "cat /etc/newmotd"
vim pretasks.yml
```

### Lesson 8 Lab Working with Roles and Collections

- Write a playbook that uses the Nginx role to install Nginx on all RHEL family hosts. Make sure that before using the role, the following is done.
  - If installed and running, Apache is removed.
  - Perform an update of all packages.
- After running the role, remove the yum package cache.

### Lesson 8 Lab Solution Working with Roles and Collections

```bash
cd roles
ansible-galaxy role list;
vim lab8.yml
ansible-playbook lab8.yml
ansible-playbook --help
ansible-playbook lab8.yml --list-tasks;
ansible-playbook lab8.yml --start-at-task file
```
