# Lesson 2 - Using Ad-hoc Commands

- [Lesson 2 - Using Ad-hoc Commands](#lesson-2---using-ad-hoc-commands)
    - [2.1 Ad-hoc Commands versus Playbooks](#21-ad-hoc-commands-versus-playbooks)
      - [When to Use Ad-hoc Commands](#when-to-use-ad-hoc-commands)
      - [Understanding Ansbile Modules](#understanding-ansbile-modules)
      - [Running Ad-hoc Commands](#running-ad-hoc-commands)
    - [2.2 Exploring Essential Ansible Modules](#22-exploring-essential-ansible-modules)
      - [Understanding Module Names](#understanding-module-names)
      - [Listing Modules](#listing-modules)
      - [Exploring Some Essential Modules](#exploring-some-essential-modules)
      - [Best Practice](#best-practice)
      - [Demo: Performing Tasks Using Modules](#demo-performing-tasks-using-modules)
    - [2.3 Using Module Documentation](#23-using-module-documentation)
      - [Using ansible-doc](#using-ansible-doc)
    - [2.4 Using Ansible in an Idempotent way](#24-using-ansible-in-an-idempotent-way)
      - [Understanding Idempotency](#understanding-idempotency)
      - [Demo: Exploring Idempotency](#demo-exploring-idempotency)
    - [Lesson 2 Lab Using Ad-hoc Commands](#lesson-2-lab-using-ad-hoc-commands)
    - [Lesson 2 Lab Solution Using Ad-hoc Commands](#lesson-2-lab-solution-using-ad-hoc-commands)

### 2.1 Ad-hoc Commands versus Playbooks

#### When to Use Ad-hoc Commands

- In an ad-hoc command, Ansible modules are used to perform tasks on managed hosts.
- Ad-hoc commands are perfect for running one task on a managed host.
  - Initial host setup.
  - Checking configuration on hosts.
- Ad-hoc commands are also perfect to learn how easy Ansible really is.
- Playbooks are the way to implement more ocmplex tasks where dependency relatios have to be manged.

#### Understanding Ansbile Modules

- An Ansible module is a python script that will be executed on the manged host.
- More than 3000 modules are available in Ansible.
- Modules can be offered as such (pre Ansible 2.10) or as a prt of a collection (Ansible 2.10 and later)

#### Running Ad-hoc Commands

- Use the ansible command to run ad-hoc commands.
- While running the **ansible** command, an inventory must be present, and you must specify which host to address.
- You'll also use the **-m** option to address a specific module, and **-a** for module arguments.
```bash
ansible -i inventory windows -m ansible.windows.wim_ping
ansible -i inventory all -m ansible.builtin.command -a id
ansible -i inventory all -m ansible.builtin.command -a reboot
ansible -i inventory all -m ansible.builtin.command -a uptime;
ansible rocky1 -m ansible.builtin.user -a "name=student state=present"
ansible rocky1 -m user -a "name=student state=present"
```

### 2.2 Exploring Essential Ansible Modules

#### Understanding Module Names

- Before Ansible 2.0, modules were referred to just by their name.
  - **ansible all -m command -a reboot**
- Since Ansible 2.10, modules are a part of Ansible collections
  - **ansible all -m ansible.builtin.command a reboot**
- Collections allow for better management of large amounts of modules.
- For compatibility reasons, the old module names can still be used.

#### Listing Modules

- Pre-2.10: **ansible-doc -l**
- 2.10 and later: **ansible-doc -t module -l**

#### Exploring Some Essential Modules

- **ansible.builtin.command** is the default module and runs arbitrary commands on the managed noded, but not through a shell.
- **ansible.builtin.shell** is an alternative to **command**, and should be used when shell items like pipes and redirects are required.
- **ansible.builtin.raw** runs the command without the need for Python being present on the managed nodes.
- **ansible.builtin.package** is a generic module for managing packages.
- **ansible.builtin.user** allows for user management.

#### Best Practice

- Always use the most specific module you can find.
- Using generic modules often leads to problems as these don't do well in situations where the desired state already exists.
- This is referred to as idempotency: meaning that if the current state already matches the desired state, the module will still work as expected and won't fail.

#### Demo: Performing Tasks Using Modules

- Use **ansible ansible1 -m command -a "rpm -qa | grep python"**
- Observe the command output, did it work?
- Use **ansible ansible1 -m shell -a "rpm -qq | grep python"**
- Did you see any difference.
- Use **ansible all -m copy -a 'content="Hello World" dest=/etc/motd'**
- Verify it worked **ansible all -a "cat /etc/motd"**
- Use **ansible all -m package -a "name=nmap state=latest"**
- Use **ansible rocky -m service -a "name=httpd state=started enabled=yes"**
- Did that work?

### 2.3 Using Module Documentation

#### Using ansible-doc

- Module documentation is in **ansible-doc**
- Use **ansible-doc -t module -l** to show a list of all modules.
- Use **ansible-doc modulename** for a detailed description of the module and its options.
- Notice the example section that exists at the end of the documentation for each of the modules.
```bash
ansible-doc -t module -l;
ansible-doc -t module -l | wc;
ansible-doc aci_filter;
```

### 2.4 Using Ansible in an Idempotent way

#### Understanding Idempotency

- Idempotence is a property of operations in mathematics and computer science whereby they can be applied multiple times without changing the result.
- In Ansible it means that a module should run successfully, where it makes no difference if the current state already meets the desired state or not.
- Mnay Ansible modules are idempotent by nature, but some are not.
- Avoid using **command, shell or raw** as they are not idempotnet by nature.

#### Demo: Exploring Idempotency

- As user **ansbile** on **control**, make sure you are in the directory that has inventory as ansible.cfg files.
- **ansible all -m ping**
- **ansible all -m user -a "name=student"**
- Observe command output.
- **ansible all -m command -a "useradd student1"**
- **ansible all -m user -a "name=student1 state=absent"**

### Lesson 2 Lab Using Ad-hoc Commands

- Use Ad-hoc commands to request Ansbile facts for your Windows server.
- Use Ad-hoc commands to create a user **student** on your Windows server.

### Lesson 2 Lab Solution Using Ad-hoc Commands

```bash
ansbile-doc -l | grep ^win;
cd playbooks/windows/
ansible win -m win_product_facts
ansible-doc win_user;
ansible win -m win_user -a "name=student password=p@ssw0rd123"
```
