# Lesson 9 - Ansible Best Practices and Optimization

- [Lesson 9 - Ansible Best Practices and Optimization](#lesson-9---ansible-best-practices-and-optimization)
    - [9.1 Using Includes and Imports](#91-using-includes-and-imports)
      - [Using Includes adn Imports](#using-includes-adn-imports)
    - [9.2 Configuring Security](#92-configuring-security)
      - [Securing Connections](#securing-connections)
      - [Making Secure Connections](#making-secure-connections)
      - [Securing sudo Access](#securing-sudo-access)
      - [Demo: Securing Ansible Management](#demo-securing-ansible-management)
    - [9.3 Using Tags](#93-using-tags)
      - [Understanding Tags](#understanding-tags)
    - [9.4 Using Delegation](#94-using-delegation)
      - [Understanding Delegation](#understanding-delegation)
      - [Understanding Delegation Requirements](#understanding-delegation-requirements)
      - [Using Delegation to Copy Files Between Hosts](#using-delegation-to-copy-files-between-hosts)
    - [9.5 Managing Parallelism](#95-managing-parallelism)
      - [Understanding Parallelism](#understanding-parallelism)
    - [9.6 Efficiently Copying Files](#96-efficiently-copying-files)
      - [Copying Files](#copying-files)
    - [9.7 Optimizing SSH](#97-optimizing-ssh)
      - [Optimizing SSH](#optimizing-ssh)
      - [Configuring sudo for Pipelining](#configuring-sudo-for-pipelining)
    - [9.8 Case Study: Optimizing Ansible](#98-case-study-optimizing-ansible)
    - [Lesson 9 Lab Optimizing Ansible](#lesson-9-lab-optimizing-ansible)
    - [Lesson 9 Lab Solution Optimizing Ansible](#lesson-9-lab-solution-optimizing-ansible)

### 9.1 Using Includes and Imports

#### Using Includes adn Imports

- If playbooks grow larger, it is common to use modularity by using includes and imports.
- Includes and imports can happen for roles, plays as well as tasks.
- A include is a dynamic process; Ansible processes the contents of the included files at the moment that this include is reached.
- An import is a static process; Ansible preprocesses the imported file contents before the actual play is started.
```bash
cd includes/
vim includes.yml
vim install-and-setup.yml;
vim ../optimization/includes-and-imports.yaml
```

### 9.2 Configuring Security

#### Securing Connections

- Commonly used but insecure.
  - passphrase-less SSH keys to connect to remote hosts.
  - **become = true** as a standard setting.
  - passwordless privilege escalation.
- More secure but not convenient.
  - **-b -K** when needed
  - **-k** instead of SSH keys.

#### Making Secure Connections

- Do NOT configure passwordless solutions as a standard.
- Securing SSH connections.
  - Use **ssh-keygen** to generate an SSH key that is protected with a password.
  - Use **eval ssh-agent $SHELL** to start the SSH agent after login.
  - Use **ssh-add ~/.ssh/id_rsa** to add your identity to the agent.
  - Verify using **ssh-add -l**
- Consider automating by putting all in **~/.bash_profile**
  - You will be prompted for the key password at first use.
  - Next, the password is cached for the remaining duration of your session.
  ```shell-script
  if [ -z "$SSH_AUTH_SOCK"]; then
        eval `ssh-agent -s`
        ssh-add
  fi
  ```

#### Securing sudo Access

- Do NOT use the **NOPASSWD** option in /etc/sudoers
- Instead, increase the **timestamp** option in /etc/sudoers to decrease the frequency that you will have to enter a password.
  - **Defaults timestamp_type=global,timestamp_timeout=60**
  - **timestamp_global** keeps an authentication token for passwordless privelege escalation, no matter which terminal a user is coming from.
  - **timestamp_timeout=60** keeps the token for 60 minutes.
- These options are needed on ALL managed servers.
  - Consider using **line_in_file** to get them there.
- On first contact, use **-K** to prompt for privilege escalation password.
- In all subsequent commands, omit the **-K** option until you see an error.
- After token expiration, use **-K** again to refresh the token.

#### Demo: Securing Ansible Management

- On control machine, use **ssh-keygen** and set a password for the Ansible user.
- **eval ssh-agent /bin/bash**
- **ssh-add ~/.ssh/id_rsa**
- Use **ssh-copy-id** to copy the new public key to managed hosts.
- Create a playbook that uses **lineinfile** to replace the **Default** section in /etc/sudoers on all managed hosts.
  - **regexp: '^Defaults'**
  - **line: 'Defaults timestamp_type=global,timestamp_timeout=60'**
  - **validate: /usr/sbin/visudo -cf %s**
- Run the playbook with the **-k -K** options
- Use **ansible all -a 'ls /root' -b -K** and enter the sudo password when prompted.
- Run again: **ansible all -a 'ls /root' -b** without any further options.
```bash
ssh-keygen
eval ssh-agent /bin/bash
ssh-add ~/.ssh/id_rsa
ssh-add -l
ssh-copy-id ansible1  
ssh-copy-id ansible2
ssh ansible1 whoami
cd playbooks/
vim makemesecure.yml
absible-playbook makemesecure.yml -K -b
ansible all -a 'ls /root' -b -K
ansible all -a 'ls /root' -b
```

### 9.3 Using Tags

#### Understanding Tags

- a **tag** is a label that can be used in a playbook to identify specific playbook elements.
- Using tages allows you to run specific parts of the playbook only.
- Tags are useful in playbook development to skip parts that have proved to be working all right.
```bash
vim kube-cluster-setup.yaml
ansible-playbook --help | grep tag
ansible-playbook kube-cluster-setup.yaml --list-tags -e kubehost=localhost
ansible-playbook -t installrole kube-cluster-setup.yaml -e kubehost=localhost
ansible-playbook --help | grep task
```

### 9.4 Using Delegation

#### Understanding Delegation

- Delegation is used to run tasks on another host.
- Use **delegate_to** as a task property to run that task on a different host.
- It allows you to run an individual task on a different host, without any need to start a new play that addresses these hosts specifically.
- See **optimization/delegation.yaml**
```bash
cd optimization
vim delegation.yaml
ansible-playbook delegation.yaml
```

#### Understanding Delegation Requirements

- Delegation hosts need to meet the same Requirements as regular control hosts.
  - Python is installed.
  - SSH access to managed hosts is enabled.
  - Host name to IP address resolving works.
- The **delegate_to** host must exist in inventory

#### Using Delegation to Copy Files Between Hosts

- A common use case for delegation is to copy files between hosts.
- See **optimization/copy-files.yaml**
```bash
cd optimization
vim copy-files.yaml
ansible-playbook -vvv copy-files.yaml # Note: it will through an error, install `rsync` and try again or use copy module instead synchronize module.
```

### 9.5 Managing Parallelism

#### Understanding Parallelism

- The first task in a play is executed on all managed hosts before moving over to the next task.
- By default, this happens on 5 hosts simultaneously.
- This is because task execution creates workload, as well as network load.
- If the control host as well as the network can handle it, you can increase the number of concurrent tasks.
- Use **forks=nn** of **-f nn**
- Be careful increasing this parameter if processing is happening on the control node.
- Consider using a callback plugin (covered in lesson 11) to measure the impact of increasing the number of forks.

### 9.6 Efficiently Copying Files

#### Copying Files

- The **copy** module can take a long time when dealing with large amounts of files.
- Consider using the **synchronize** module, it uses **rsync** in the background which is mor eefficient.
- For **synchronize** to work, ensure that rsync is installed on the managed nodes.
```bash
cd optimization
vim synchronize.yaml;
ansible-playbook synchronize.yaml
ansible all -a 'ls /var/www/html'
```

### 9.7 Optimizing SSH

#### Optimizing SSH

- Ansible uses SSH to manage hosts.
- Establishing a new SSH session takes a lot of time.
- To make SSH connections more efficient, three SSH features can be used.
  - **ControlMaster** allows multiple simultaneous SSH sessions with a remote host using one network connection.
  - **ControlPersist** keeps a connection open for xx seconds.
  - **pipelining** allows more commands to use a simultaneous SSH connection.
- Use an **[ssh_connection]** section in the Ansible config file to specify how to use these options.
  ```bash
  [ssh_connection]
  ssh_args = -o ControlMaster=auto -o ControlPersist=120s
  pipelining = true
  ```

#### Configuring sudo for Pipelining

- When Pipelining is enabled, the **requiretty** sudo option must be disabled.
- **requiretty** is a sudo security option, that prevents sudo commands that are not started from a TTY.
- To verify this option is disabled, use **visudo** and look for the following.
  - **Defaults !requiretty**
```bash
cd task_control/
vim ansible.cfg
ansible ansible1 -a 'grep efault /etc/sudoers'
ansible-doc lineinfile
vim tunesudo.yaml
time ansible-playbook tunesudo.yaml
time ansible-playbook tunesudo.yaml # Should take less time to execute playbook.
```

### 9.8 Case Study: Optimizing Ansible

```bash
time ansible-playbook tunesudo.yaml
time ansible-playbook -vvv tunesudo.yaml
ansible all -m copy "src=/etc/hosts dest=/etc/hosts"
time ansible-playbook -vvv tunesudo.yaml
```

### Lesson 9 Lab Optimizing Ansible

- In a dedicated project directory, create an Ansible configuration that is tuned for security. Write a playbook that changes the sudo configuration on all managed hosts, allowing you to use optimized SSH parameters (set on the control node), and which requires you to enter a privilege escalation password once every two hours.
- Configure SSH in such a way that passphrase protected keys are used.

### Lesson 9 Lab Solution Optimizing Ansible

```bash
cd lesson9
vim secureme.yaml;
ansible-playbook secureme.yaml -u root -k
ansible all -a 'ls /root'
ansible all -a 'ls /root' -K
ansible all -a 'ls /root'

ssh-keygen;
ssh-copy-id ansible1
ssh-copy-id ansible2
ssh ansible1
exit
ssh ansible2
exit
eval ssh-agent /bin/bash
ssh-add ~/.ssh/id_rsa
ansible all -a 'ls /root'
```
