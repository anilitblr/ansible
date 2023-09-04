# Lesson 7 - Managing Files

- [Lesson 7 - Managing Files](#lesson-7---managing-files)
    - [7.1 Manipulating Files](#71-manipulating-files)
      - [Manipulating Files](#manipulating-files)
      - [Using copy](#using-copy)
      - [Using synchronize](#using-synchronize)
      - [Using fetch](#using-fetch)
    - [7.2 Changing File Contents](#72-changing-file-contents)
      - [Changing File Contents](#changing-file-contents)
      - [Using copy and replace](#using-copy-and-replace)
      - [Using lineinfile and blockinfile](#using-lineinfile-and-blockinfile)
    - [7.3 Using the find Module](#73-using-the-find-module)
      - [Using the find module](#using-the-find-module)
    - [7.4 Using Templates](#74-using-templates)
      - [Understanding Templates](#understanding-templates)
    - [Lesson 7 Lab Working with Files](#lesson-7-lab-working-with-files)
    - [Lesson 7 Lab Solution Working with Files](#lesson-7-lab-solution-working-with-files)

### 7.1 Manipulating Files

#### Manipulating Files

- **ansible.builtin.copy** is used to copy files from the control host to a managed host.
- **ansible.posix.synchronize** synchronizes file contents and is more efficient.
- **ansible.builtin.fetch** will fetch a file from a managed host to the control host.

#### Using copy

- Use **ansible.builtin.copy** as an Ansible alternative to Linux copy.
- It can copy over individual files, as well as directories.
- Use **contents** to copy a line of text into a new destination file.

#### Using synchronize

- **ansible.posix.synchronize** is using the rsync command to synchronize files from the contril host to managed hosts.
- **ansible.posix.synchronize** is more efficient for copying large amounts of files than **ansible.builtin.copy**
- It does require the **rsync** software to be installed on all hosts involved.
- Use **delegate_to** to change the source host to a host different than localhost.

#### Using fetch

- **ansible.builtin.fetch** can be used to fetch a file from a managed machine and store it on the control host.
- It will store files by appending hostname/path/to/file to the fetched file.
- Use the **flat** option to override this behavior and store just the filename.

### 7.2 Changing File Contents

#### Changing File Contents

- **ansible.builtin.copy** can be used to create files with simple contents.
- **ansible.builtin.replace** is used for simple replacements.
- **ansible.builtin.lineinfile** can be used to manipulate single lines in a text file.
- **ansible.builtin.blockinfile** is useful for manipulating complete blocks of text.

#### Using copy and replace

- **ansible.builtin.copy** and **ansible.builtin.replace** can be used for simple operations.
- Use the **content** argument to the **copy** module to copy a string into a destination file.
  - **ansible all -m copy "content=hello dest=/tmp/hellofile"**
- The **replace** module allows you to replace file contents based on regular expressioin
  - Use **regexp** to identify the regular expression you want to replace.
  - Use **replace** to specify the replacement text.
  - Omit the **replace** argument if you just want to remove text.

#### Using lineinfile and blockinfile

- Use **lineinfile** to add a single line to a file.
- Use **blockinfile** to add multiple lines to a file.

```bash
cd files
vim copy.yml
ansible-plabook copy.yml;
```

### 7.3 Using the find Module

#### Using the find module

- The **find** module is used to perform opeations on multiple files.
- It is similar to the Linux **find** command.
- Use it with regular expressions, or in combintion with **lineinfile** to perform modifications on multiple files.
- When using **register** together with **find**, you can easily build a playbook to change files regardless of their exact location.
```bash
cd files
vim changeconfig.yaml
ansible-plabook changeconfig.yaml
```

### 7.4 Using Templates

#### Understanding Templates

- A template is a sample configuration file that is combined with environment variables to produce site specific configuration files.
- Templates are based on the Jinja2 templating language.
- In advanced templates, conditional structures as well as loop structures can be used.
```bash
cd templates/
vim motd.j2
vim motd.yaml
ansible-plabook motd.yaml;
ansible all -a "cat /etc/motd"
ansible ansible1 -m setup | less
ansible-plabook hosts.yaml;
ansible all -a "cat /tmp/newhosts"
```

- Ref: https://docs.ansible.com/ansible/2.9/reference_appendices/faq.html#how-do-i-loop-over-a-list-of-hosts-in-a-group-inside-of-a-template


### Lesson 7 Lab Working with Files

Write a playbook that is doing the followings.
- Installs vsftpd on all managed hosts.
- Copies the file /etc/vsftpd/vsftpd.conf from one of the managed hosts to the control host.
- Converts that file into a template, adding one line to the end of the file: # written on {{ ansible_hostname}}
- Uses the template to create a new version of the configuration file on the managed hosts.
- Ensure that vsftpd is started, enabled and accessible through the firewall.

### Lesson 7 Lab Solution Working with Files

```bash
cd files
ansible-plabook lab7.yml
ansible ansible1 -a "systemctl status vsftpd"
```
