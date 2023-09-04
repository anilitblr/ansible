# Lesson 3 - Using Ansible Playbook

- [Lesson 3 - Using Ansible Playbook](#lesson-3---using-ansible-playbook)
    - [3.1 Understanding Playbook Structure](#31-understanding-playbook-structure)
      - [Understanding Playbook Elements](#understanding-playbook-elements)
      - [Understanding YAML](#understanding-yaml)
      - [Understanding Playbook elements](#understanding-playbook-elements-1)
    - [3.2 Writing and Running your First Playbook](#32-writing-and-running-your-first-playbook)
      - [Running Playbook](#running-playbook)
      - [Exploring an Example Playbook](#exploring-an-example-playbook)
      - [Exploring Multi-play Playbooks](#exploring-multi-play-playbooks)
    - [3.3 Understanding Task Execution and Errors](#33-understanding-task-execution-and-errors)
      - [Understanding Playbook Errors](#understanding-playbook-errors)
      - [Undoing Playbook Modifications](#undoing-playbook-modifications)
    - [Lesson 3 Lab Using a Playbook to Automate Web Server Setup](#lesson-3-lab-using-a-playbook-to-automate-web-server-setup)
    - [Lesson 3 Lab Solution Using a Playbook to Automate Web Server Setup](#lesson-3-lab-solution-using-a-playbook-to-automate-web-server-setup)

### 3.1 Understanding Playbook Structure

- Playbooks are used to run multiple tasks in order on multiple hosts.
- Playbooks are the way to to to define dependency relations between tasks.
- Playbooks can also be used to implement conditional structures, where tasks are only executed if sepecific conditions are ture.

#### Understanding Playbook Elements

- In a plyabook, one or more plays are defined.
- Each play has a header that defines different properites, including the hosts on which it has to run.
- In a play, one ore more tasks are defined.
- Playbooks are written in YAML which makes it easy to define relatins between parent and child elements.

#### Understanding YAML

- In YAML, identation is used to identify the relation between parent and child objects, which are specified as key: value pairs.
- Data elements at the same level in the hiererchy must have the same indentation.
- Items that are children (properties) are indented more than the partents.
- If a specific module argument can have multiple values, these values typically start with a hyphen.
- Indentation happens using spaces. Using tabs is nto allowed.
- Configure **vi** for indentation by adding the following to **~/.vimrc**
```bash
vi ~/.vimrc

autocmd FileType yaml setlocal ai ts=2 sw=2 et
```

#### Understanding Playbook elements

- The relations are defined using indentation.
- Task properties are defined using key: value pairs.
- Most keys can have one string value.
- Some keys have a list (array) value.
- When a list value is defined, each item is identified using a hypen.
```bash
cd playbooks/basics/
vi example.yml;
ansible-playbook sample.yml;
```

### 3.2 Writing and Running your First Playbook

#### Running Playbook

- To run a playbook, the **ansible-playbook** command is used.
- Syntax check is not needed, you will be alerted if anthing is wrong with your playbook.
- Use **-v** up to four times for increased verbosity messages.
- No output log is written, read STDOUT of messages about success or failure ofthe playbooks.

#### Exploring an Example Playbook

- Have a look at **install_and_start_httpd.yaml**
```bash
cd playbooks/basics/
vi install_and_start_httpd.yaml;
ansible-playbook install_and_start_httpd.yaml;
```
- Run the playbook **ansible-playbook install_and_start_httpd.yaml** and observe the output.
- On playbook execution many things happen.
  - Fact gathering.
  - Task execution.
  - Play Recap.
- Notice that a good playbook is written to be idempotent.

#### Exploring Multi-play Playbooks

- A playbook can define one or more plays.
- Defining multi-play playbooks makes sense in the following cases.
  - To write the playbook in a modular way.
  - To limit the number of tasks that run in one play.
  - To run some tasks on one host, while others are running on another host.
- Have a look at **run_and_test_httpd.yaml** and run it.
```bash
vim run_and_test_httpd.yaml;
ansible-playbook run_and_test_httpd.yaml;
ansible-doc firewalld;
```

### 3.3 Understanding Task Execution and Errors

#### Understanding Playbook Errors

- A play contains a series of tasks.
- Task dependencies in general are very important.
- If a task fails to run on a specific host, further execution of tasks in the failing play is aborted on that host.
- Use **ignore_errors: True** to continue execution anyway.

#### Undoing Playbook Modifications

- There is no easy way to undo modifiactions that have been applied by a playbook.
- This is because of the complex dependency relations that may exist between playbooks.
- The only way to undo a playbook, is by writing a playbook that is doing the opposite actions in reversed order.
```bash
cd playbooks/basics/
vim failingtask.yaml;
ansible-playbook failingtask.yaml;
ansible-playbook failingtask.yaml;
```

### Lesson 3 Lab Using a Playbook to Automate Web Server Setup

- Write a playbook that meets the following requirements. Use **ansible-doc** for additional information if needed.
  - Install, start and enable the **vsftpd** service on all managed nodes.
  - Open the **firewalld** firewall to allow access to this service.
- Run the playbook, and observe working of the playbook.
- Run the playbook one more time, and again, observer the working of the playbook.

### Lesson 3 Lab Solution Using a Playbook to Automate Web Server Setup

```bash
cd playbooks/basics/
vim lesson3.yaml
ansible-playbook lesson3.yaml;
```
