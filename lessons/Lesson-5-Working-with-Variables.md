# Lesson 5 - Working with Variables

- [Lesson 5 - Working with Variables](#lesson-5---working-with-variables)
    - [5.1 Separating Code from Site-Specific Configuration](#51-separating-code-from-site-specific-configuration)
      - [DevOps Best Practices](#devops-best-practices)
    - [5.2 Using Variables in a Playbook](#52-using-variables-in-a-playbook)
      - [Using Variables in a Playbook](#using-variables-in-a-playbook)
    - [5.3 Understanding Where to Define your Variables](#53-understanding-where-to-define-your-variables)
      - [Defining Variables](#defining-variables)
      - [Defining Variables in Plays](#defining-variables-in-plays)
      - [Using set\_fact](#using-set_fact)
      - [Using vars\_prompt](#using-vars_prompt)
      - [Using Inventory and Host Variables](#using-inventory-and-host-variables)
    - [5.4 Using Ansible Facts](#54-using-ansible-facts)
      - [Understanding Ansible Facts](#understanding-ansible-facts)
    - [5.5 Understanding Different Notations for Facts and Variables](#55-understanding-different-notations-for-facts-and-variables)
      - [Understanding Facts and Variables Notation](#understanding-facts-and-variables-notation)
    - [5.6 Speeding up Fact Collection](#56-speeding-up-fact-collection)
      - [Troubleshooting Slow Fact Collection](#troubleshooting-slow-fact-collection)
    - [5.7 Using Multi-valued Variables](#57-using-multi-valued-variables)
      - [Dictionaries ersus Arrays](#dictionaries-ersus-arrays)
      - [Understanding Array and Dictionary](#understanding-array-and-dictionary)
      - [Understanding Dictionary (Hash)](#understanding-dictionary-hash)
      - [Using Dictionary](#using-dictionary)
      - [Using Array (list)](#using-array-list)
      - [Recognizing Lists and Dictionaries](#recognizing-lists-and-dictionaries)
    - [5.8 Using Magic Variables](#58-using-magic-variables)
      - [Understanding Magic Variables](#understanding-magic-variables)
      - [Using Magic variables](#using-magic-variables)
    - [5.9 Using Register](#59-using-register)
    - [5.10 Using Vault to Store Sensitive Information](#510-using-vault-to-store-sensitive-information)
      - [Dealing with Sensitive Data](#dealing-with-sensitive-data)
      - [Demo: Using Encrypted Files](#demo-using-encrypted-files)
    - [Lesson 5 Lab Making Playbooks Flexible with Variables](#lesson-5-lab-making-playbooks-flexible-with-variables)
    - [Lesson 5 Lab Solution Making Playbooks Flexible with Variables](#lesson-5-lab-solution-making-playbooks-flexible-with-variables)

### 5.1 Separating Code from Site-Specific Configuration

#### DevOps Best Practices

- Ansible is all about configuration as code.
- While developing flexible code, you should separate Site-Specific information from the code, which should be static.
- Developing dynamic code allows you to use your code on any site.
- To provide site-specific code, variables can be used.
- Apart from variables, Ansible provides facts.
- Facts are system properties that are dynamically discovered and can be used as variables.
- Separating site-specific information from static code is also referred to as decoupling.

### 5.2 Using Variables in a Playbook

#### Using Variables in a Playbook

- Variables can be defined in different ways.
- You can set them in playbooks directly, but that is bad practice as the site-specific information in that case is not separated from the code.
- While referring to a variable, you need to use double braces.
  - The variable is {{ myvariable }}
- If a value starts with a variable, the variable needs to be between double quotes and double curly braces.
  - msg: "{{ myvariable }} is set"
- If used in a when statement (discussed later) the curly braces are omitted.
```bash
cd basics
vim variables_example.yaml
ansible-playbook variables_example.yaml
ansible-playbook variables_example.yaml -e user=anil
```

### 5.3 Understanding Where to Define your Variables

#### Defining Variables

- There are different ways to define variables.
  - In the play header using **vars**
  - In the play header using an include with **var_files**
  - Using the **set_fact** module in a play.
  - On the command line, using the **-e key=value** option.
  - As inventory variables.
  - As host or host_group variables.
  - Using **vars_prompt** to request values from the user while running the playbook.
- Ansible facts are discovered variables containing system properties.
- Ansible Vault can be used to encrypt sensitive values like variables.

#### Defining Variables in Plays

- To define variables in plays, include a **vars:** section in the header of the play where the variables are needed.
- Variables defined in plays are valide only within that specific play, and don't have a playbook scope.
- Use **vars_files:** to specify a list of files that include variables you want to include.
- To override variables specified in this way, use the -e key=value command line opetion to sepcify variables.
```bash
cd basics
vim vars_file.yaml
vim myvars.yaml
ansible-playbook vars_file.yaml;
```

#### Using set_fact

- **set_fact** is a module that can be used anywhere in a play to set a variable.
- Variables set this way apply as a fact to the host on which it is set.
- The benefit of **set_fact** is that it allows you to dynamically set variables that are based on the result of any task in the playbook.
- Also, variables set with **set_fact** have a playbook scope.
```bash
vim set-fact.yaml
ansible-playbook set-fact.yaml;
```

#### Using vars_prompt

- Use **vars_prompt** in a play header to prompt users for a variable value.
- By default, the variable is flagged as "private", which means the user doen't see anything while entering the variable.
- Use **private: no** in **vars_prompt** to change this behavior.
```bash
vim vars_prompt.yaml
ansible-playbook vars_prompt.yaml
```

#### Using Inventory and Host Variables

- Inventory hand host variables are used to set a variable as a property for a specific host.
- To use host variables, create a file in a directory **host_vars** that has the name of the host.
- To define host group variables, create a file in a directory **group_vars** that has the name of a host groups.
- In these files, define the host or host group variables.
```bash
cd basics
mkdir group_vars
echo "user: student" > group_vars/rocky
ansible-playbook create-user.yaml;
```

### 5.4 Using Ansible Facts

#### Understanding Ansible Facts

- Ansible facts are system variables that contain information about the managed system.
- Each playbook starts with an implicit task to gather facts.
- To use fact fathering from an ad-hoc command, use the **setup** module.
- Additional modules for fact gathering are available, like **package_facts**
- To disable fact gathering, use **gather_facts: no** in the play header.
- Have a look at **gather_facts.yaml** to see how it works.
```bash
ansible ansible1 -m setup > ansible1_facts.txt
less  ansible1_facts.txt
vim gather_facts.yaml
ansible-playbook gather_facts.yaml;
```

### 5.5 Understanding Different Notations for Facts and Variables

#### Understanding Facts and Variables Notation

- Facts are stored in a multi-valued variable with the name **ansible_facts**, which is organized as a dictionary.
- To address sepcific values in this dictionary, two formats can be used.
  - **ansible_facts['default_ipv4']['address']**
  - **ansible_facts.default_ipv4.address**
- Of these two, the first one is preferred.
- On old versions of Ansible, facts were stored as individual variables (injected variables): **ansible_default_ipv4** instead of **ansible_facts['default_ipv4']**
- Some modules only support the old way of referring to facts.
```bash
cd basics
vim old_facts.yaml
ansible-playbook old_facts.yaml
ansible-playbook new_facts.yaml
```

### 5.6 Speeding up Fact Collection

#### Troubleshooting Slow Fact Collection

- If fact collections is slow because you are working against lots of hosts, you can use a fact cache.
- In less 11.6 you will learn how to set up a fact cache.
- If you are experiencing slow fact gathering, ensure that host name resolution is set up on all hosts.
- Ensure that each managed hosts has an /etc/hosts file that allows for name resolution between all managed hosts.
```bash
cd basics
vim new_facts.yaml
ansible all -a "cat /etc/hosts"
time ansible-playbook new_facts.yaml;
ansible all -m copy -a "src=/etc/hosts dest=/etc/hosts"
time ansible-playbook new_facts.yaml;
```   

### 5.7 Using Multi-valued Variables

#### Dictionaries ersus Arrays

- Dictionaries and arrays in Ansbile are based on Python dictionaries and arrays.
- An arry (list) is an ordered list of values, where each value can be addressed individully.
  - List = ["one", "two", "three"]
  - print(List[0])
- A dictionary (hash) is an unordered collection of values, which is stored as a key-value pair.
  - Dics = {1: "one", 2: "two", 3: "three"}
  - print(Dict)
- Notice that a dictionary can be presented in a list.

#### Understanding Array and Dictionary

- Multi-valued variables can be used in playbooks.
- When using a multi-valued variable, it can be written as an array (list), or as a dictionary (hash).
- Each of these has their own specific use cases.
  - Dictionaries are used in Ansible facts.
  - Arrays are common for multi-vaalued variables and easily support loops.
  - Loops are not supported on dictionaries directly, only indirectly by using the **dict2items** filter or by using **with_dict** (deprecated)
    - See Ansible Docs **Iterating over a dictionary**

#### Understanding Dictionary (Hash)

- Dictionaries can be written in two ways.
```yaml
---
users:
  anil:
    username: anil
    shell: /bin/bash
  kumar:
    username: kumar
    shell: /bin/sh
```

- Or as 
```yaml
---
users:
  anil:{username: "anil", shell: "/bin/bash"}
  kumar:{username: "kumar", shell: "/bin/bash"}
```

#### Using Dictionary

- To address items in a dictionary, you can use two notations.
  - variable_name['key'], as in users['anil']['shell']
  - variable_name.key, as in users.anil.shell
- Dictionaries are used in facts, use arrays in conditionals.
- Notice that dictionaries can be a part of a list, which is used in Ansible facts.

#### Using Array (list)

- Array provide a list of items, where each item can be addresses separately.
```yaml
---
users:
- username: anil
  shell: /bin/bash
- username: kumar
  shell: /bin/sh
```
- Individual items in the array can be adressed, using the {{ var_name[0] }} notation.
- Use arrarys for looping, not dictionaries.
- To access all variables, you can use **with_items** or **loop**

#### Recognizing Lists and Dictionaries

- In output like facts, a  list is alwyas written between **[]**
- Dictionaries are written between **{}**
- And if the output is just showing **""** it is a string.
- Check **ansible_mounts** in the facts, which actually presents a list of dictionaries.
```bash
cd basics
vim ubuntu_facts.txt
cd arrays/
vim vars/users-dictionary
vim vars/users-list
vim multi-dictionary.yml
vim multi-list.yml
ansible-playbook multi-list.yml
ansible-playbook multi-dictionary.yml
```

### 5.8 Using Magic Variables

#### Understanding Magic Variables

- Magic variable are special reserved system variables.
  - hostvars
  - groups
  - group_names
  - inventory_hostname
  - inventory_hostname_short
  - and more

#### Using Magic variables

- **hostvars** can be used to address facts or inventory variables from other hosts: **{{ hostvars['ansible2']['ansible_fats']['distribution'] }}**
- **groups** can be used to list all hosts in an inventory group: **{% for host in groups['webservers'] %}** ...
- **group_names** has all inventory groups a host is in: **{ % if 'webservers' in group_names % }**
- **inventory_hostname** or **inventory_hostname_short** can be used to address a host as an alternative to **ansible_hostname** when fact-tathering is disabled.

### 5.9 Using Register

- **register** can be used to store the result of a task in a variable.
- It provides an awesome way to perfrom specific tasks only upon success or failure of another task.
- Have a look at **register.yaml**
```bash
vim register.yaml;
ansible-playbook register.yaml;
```

### 5.10 Using Vault to Store Sensitive Information

#### Dealing with Sensitive Data

- Some modules require sensitive data to be precessed.
- This may include webkeys, passwords, and more.
- To process sensitive data in a secure way, Ansible Vault can be used.
- Ansible Vault is used to encrypt and decrypt files.
- To manage this process, the **ansible-vault** command is used.

#### Demo: Using Encrypted Files

- **ansible-vault --help**
- **ansible-vault create secret.yaml**
  - username: anil
  - pwhash: password
- **vim create-user.yaml**
```yaml
---
- name: create a user
  hosts: all
  vars_files:
    - secret.yaml
  tasks:
    - name: creating user
      user:
        name: "{{ username }}"
        password: "{{ pwhash }}"
```
- **ansible-playbook --ask-vault-pass create-users.yaml**
- **ansible all -a "cat /etc/shadow"**
- **echo password > vault-pass**
- **ansible-playbook --vault-password-file=vault-pass create-users.yaml**

### Lesson 5 Lab Making Playbooks Flexible with Variables

- Create an inventory file that defines a host group webservers, as well as a group dbservers.
- Create the file **group_vars/webservers** with the following contents.
  - web_package: httpd
  - web_service: httpd
- Create a simple playbook that uses the **debug** module to show the current value of the variable **web_package** and **web_service** 

### Lesson 5 Lab Solution Making Playbooks Flexible with Variables

- - Create an inventory file that defines a host group webservers, as well as a group dbservers.
```bash
cd basicsvim inventory

[dbservers]

[webservers]
ansible1
ansible2
```

- Create the file **group_vars/webservers** with the following contents.
  - web_package: httpd
  - web_service: httpd
```bash
mkdir group_vars
vim group_vars/webservers

web_package: httpd
web_service: httpd
```

- Create a simple playbook that uses the **debug** module to show the current value of the variable **web_package** and **web_service** 
- vim lab5.yaml
```yaml
---
- name: demo lab5
  hosts: webservers
  tasks:
  - debug: 
      msg: using {{ web_package }} and {{ web_service}}
```

- Execute the playbook.
```bash
ansible-playbook lab5.yaml;
```
