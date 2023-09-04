# Lesson 6 - Using Conditionals

- [Lesson 6 - Using Conditionals](#lesson-6---using-conditionals)
    - [6.1 Conditionals Overview](#61-conditionals-overview)
    - [6.2 Using Handlers for Conditional Task Execution](#62-using-handlers-for-conditional-task-execution)
      - [Understanding handlers](#understanding-handlers)
    - [6.3 Using when to Run Tasks Based on Specific Conditions](#63-using-when-to-run-tasks-based-on-specific-conditions)
      - [Using Conditions](#using-conditions)
      - [Examples](#examples)
    - [6.4 Using register to Work with Task Results](#64-using-register-to-work-with-task-results)
      - [Understanding register](#understanding-register)
    - [6.5 Using Blocks](#65-using-blocks)
      - [Understanding Ansbile Blocks](#understanding-ansbile-blocks)
    - [6.6 Using loop to Process a List of Items](#66-using-loop-to-process-a-list-of-items)
      - [Understanding loop](#understanding-loop)
      - [Using Variables to Define a Loop](#using-variables-to-define-a-loop)
      - [Using Arrays in Loops](#using-arrays-in-loops)
      - [Understanding loops vs. items](#understanding-loops-vs-items)
    - [6.7 Managing Failure with the fail Module](#67-managing-failure-with-the-fail-module)
      - [Understanding Failure Handling](#understanding-failure-handling)
      - [Defining Failure States](#defining-failure-states)
      - [Using the fail Module](#using-the-fail-module)
    - [6.8 Using the assert Module](#68-using-the-assert-module)
    - [Lesson 6 Lab Using when to Make the command Module Idempotent](#lesson-6-lab-using-when-to-make-the-command-module-idempotent)
    - [Lesson 6 Lab Solution Using when to Make the command Module Idempotent](#lesson-6-lab-solution-using-when-to-make-the-command-module-idempotent)

### 6.1 Conditionals Overview

- **handlers** are tasks that only run if triggered by a task that has changed something.
- **items** can be used to iterate over a list.
- **when** is used for conditional task execution.
- **blocks** can be used to implement **if-then-else** like statements.
- **register** is a useful aid to record the result of a task in a variable.
- **fail** is a module that is used to perform a specific task on failure.

### 6.2 Using Handlers for Conditional Task Execution

#### Understanding handlers

- A handler is a task that is only executed when triggered by a task that has changed something.
- Handlers are executed after all tasks in a play.
- If any task fails after the task that has called the handler, handlers are not executed.
- Use **force_handlers** to change that behavior.
```bash
cd task_control/
vim handlers.yml;
ansible-playbook handlers.yml;
ansible all -m file -a "name=/var/www/html/index.html state=absent"
ansible-playbook handlers.yml;
```

### 6.3 Using when to Run Tasks Based on Specific Conditions

#### Using Conditions

- **when** statements are used to run a task conditionally.
- Playbook variables, registered variables, and facts can be used in conditions and make sure that tasks only run if specific conditiions are ture.
- For instance, check if a task has run successfully, a certain amount of memory is available, a file exists, etc.
- Using facts is very common in **when** statements.

#### Examples

- ansible_machine == "x86_64"
- ansible_distribution_major_version == "8"
- ansible_memfree_mb == 2014
- ansible_memfree_mb < 256
- ansible_memfree_mb > 256
- ansible_memfree_mb <= 256
- ansible_memfree_mb != 512
- my_variable is defined
- my_variable
- ansible_distribution in supported_distros
```bash
cd task_control
vim distro.yml
ansible-playbook distro.yml;
vim quicktest.yml;
ansible-playbook quicktest.yml;
```

### 6.4 Using register to Work with Task Results

#### Understanding register

- **register** is used to store the output of a command, and address it as a variable.
- You can next use the result of the command in a conditional or in a loop.
```bash
cd task_control
vim command-output-test.yml
ansible-playbook command-output-test.yml
ansible ansible1 a "vgs" # Find the volume group and update it in the command-output-test.yml
ansible-playbook command-output-test.yml

vim register_command.yml
ansible-playbook register_command.yml
```

### 6.5 Using Blocks

#### Understanding Ansbile Blocks

- A block is a logical group of tasks.
- Blocks are used to control how tasks are executed.
- One block can, for instance, be enabled using a single **when**
- Blocks can also be used in error condition handling.
  - Use **block** to define the main tasks to run.
  - Use **rescue** to define tasks that run if tasks defined in the **block** fail.
  - Use **always** to define tasks that will run, regardless the success or failure of the **block** and **rescue** tasks.
- Notice that items cannot be used on blocks.
```bash
cd task_control
vim blocks.yml
ansible-playbook blocks.yml;
vim blocks2.yml
ansible-playbook blocks2.yml;
```

### 6.6 Using loop to Process a List of Items

#### Understanding loop

- Ansible offers different solutions to implement iterations.
- Items are easy to use.
  - Define a list of items.
  - In the task, use **loop** (previously: **with_items**) to proccess the itesm.
  ```yaml
  tasks:
  - name: remove files
    file:
      name: "{{ item }}"
      state: absent
    loop:
      - file1
      - file2
  ```

#### Using Variables to Define a Loop

- The list that **loop** is using can be defined by a variable.
```yaml
vars:
  my_services:
    - httpd
    - vsftpd
tasks:
  - name: start some services
    service:
      name: "{{ item }}"
      state: started
    loop: "{{ my_services }}"
```

#### Using Arrays in Loops

- Each item in a **loop** can be a array with multiple keys in each arrary item.
```yaml
---
- name: create users using a loop
  hosts: all
  tasks:
  - name: create users
    user:
      name: "{{ item.name }}"
      state: present
      groups: "{{ item.groups }}"
    loop:
      - name: anil
        groups: wheel
      - name: kumar
        groups: users  
```

#### Understanding loops vs. items

- The **loop** keyword is the current keyword.
- In previous versions of Ansible, the **with_\*** keyword was used for the same purpose.
- The **loop** syntas is preferred, but **with_X** is still supported as well.
  - **with_items:** equivalent to the **loop** keyword.
  - **with_file:** the **item** contains a file, which contents is used to loop through.
  - **with_sequence:** generates a list of values based on a numeric dwquence.
- Most of the **with_X** statements can now be replaced with filters (covered in lesson 10)
```bash
cd task_control
vim loopservices.yml ;
ansible-playbook loopservices.yml;

vim loopusers.yml;
ansible-playbook loopusers.yml;

vim install_and_run.yml;
ansible-playbook install_and_run.yml;
```

### 6.7 Managing Failure with the fail Module

#### Understanding Failure Handling

- Ansible looks at the exit status of a task to determine whether it has failed.
- This may lead to failures occuring when nothing really is going wrong.
- When any task fails, Ansible aborts the rest of the play on that host and continues with the next host.
- Different solutions can be used to change that behavior.
- Use **ignore_errors** in a task to ignore failures.
- Use **force_handlers** to force a handler that has been triggered to run, even if (another) task fails.

#### Defining Failure States

- As Ansible only looks at the exit status of a failed task, it may think a task was successful where that is not the case.
- To be more specific, use **failed_when** to specify what to look for in command output to recognize a failure.

#### Using the fail Module

- The **failed_when** keyword can be used in a task to identify when a task has failed.
- The **fail** module can be used to print a message that informs why a task has failed.
- To use **failed_when** or **fail**, the result of the command must be registered, and the registered variable output must be analyzed.
- When using the **fail** module, the failing task must have **ignore_errors** set to yes.
```bash
cd task_control
vim failure.yml
ansible-playbook failure.yml

vim failure2.yml
ansible-playbook failure2.yml
```

### 6.8 Using the assert Module

- The **assert** module can be used to show a message on success and on failure.
- It's a bit like the **fail** module, but with more advanced options.
```bash
cd task_control
vim assertsize-wrong.yml
ansible-playbook assertsize-wrong.yml;
vim assertsize.yml
ansible-playbook assertsize.yml;
```

### Lesson 6 Lab Using when to Make the command Module Idempotent

- Idempotency is a great thing is Ansible. It ensures that running a playbook always gives the same result, no matter the current state of the managed asset. You have previously learned that the **command** module, as well as related modules like **shell** and **raw** are not idempotent by nature. However, if you are using **register** in a smart way you can use even these modules in an idempotent way.
- In this lab, write a playbook that creates a user using the **command** module in such a way that the playbook is idempotent.

### Lesson 6 Lab Solution Using when to Make the command Module Idempotent

```bash
vim lab6.yml
ansible-playbook lab6.yml
```
