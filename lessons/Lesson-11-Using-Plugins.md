# Lesson 11 - Using Plugins

- [Lesson 11 - Using Plugins](#lesson-11---using-plugins)
    - [11.1 Understanding Plugins and Filters](#111-understanding-plugins-and-filters)
      - [Understanding Plugins](#understanding-plugins)
      - [Understanding Plugin Types](#understanding-plugin-types)
    - [11.2 Exploring Lookup Plugins](#112-exploring-lookup-plugins)
      - [Exploring Lookup Plugins](#exploring-lookup-plugins)
      - [Using Lookup Plugins](#using-lookup-plugins)
      - [Useful Lookup Plugin Overview](#useful-lookup-plugin-overview)
      - [Using the file Lookup Plugin](#using-the-file-lookup-plugin)
    - [11.3 Using Common Lookup Plugins](#113-using-common-lookup-plugins)
      - [Using env and template](#using-env-and-template)
      - [Using pipe and lines](#using-pipe-and-lines)
      - [Using url](#using-url)
    - [11.4 Using the fileglob Lookup Plugin](#114-using-the-fileglob-lookup-plugin)
      - [Understanding the fileglob Lookup Plugin](#understanding-the-fileglob-lookup-plugin)
      - [Using fileglob with Wildcards](#using-fileglob-with-wildcards)
    - [11.5 Using Callback and Timer Plugins](#115-using-callback-and-timer-plugins)
      - [Using Callback Plugins](#using-callback-plugins)
      - [Using cgroup\_perf\_recap](#using-cgroup_perf_recap)
      - [Demo: Using cgroup\_perf\_recap](#demo-using-cgroup_perf_recap)
      - [Using Specific Callback Plugins](#using-specific-callback-plugins)
      - [Demo: Using Timer Callback Plugins](#demo-using-timer-callback-plugins)
    - [11.6 Using Plugin-Based Inventory](#116-using-plugin-based-inventory)
      - [Using Plugin-Based Inventory](#using-plugin-based-inventory)
      - [Using the ini Plugin](#using-the-ini-plugin)
      - [Using the YAML Plugin](#using-the-yaml-plugin)
      - [Converting ini Inventory](#converting-ini-inventory)
      - [Understanding Inventory Sources](#understanding-inventory-sources)
    - [11.7 Configuring Fact Caching](#117-configuring-fact-caching)
      - [Using Fact Caching](#using-fact-caching)
      - [Demo: Configuring the redis Plugin](#demo-configuring-the-redis-plugin)
      - [Using a Fact Cache](#using-a-fact-cache)
      - [Fact Caching Caveats](#fact-caching-caveats)
    - [11.8 Creating Random Passwords](#118-creating-random-passwords)
      - [Using the password Lookup Plugin](#using-the-password-lookup-plugin)
    - [Lesson 11 Lab Configuring Fact Caching](#lesson-11-lab-configuring-fact-caching)
    - [Lesson 11 Lab Solution Configuring Fact Caching](#lesson-11-lab-solution-configuring-fact-caching)

### 11.1 Understanding Plugins and Filters

#### Understanding Plugins

- Plugins are pieces of code that augment Ansible's core functionality.
- default plugins are provided, and custom plugins can be added easily.
- To use plugins, you need to activate them in ansible.cfg.
- A filter is a program that allows you to modify data.
- Filters are typically used to change variables before using them.

#### Understanding Plugin Types

- Plugins are provided to add different types of functionality.
  - Filter plugins: used to modify text.
  - Cache plugins: plugins that allow caching of facts.
  - Inventory plugins: plugins that allow different types of dynamic inventory.
  - Lookup plugins: a very wide range of plugins that allows fetching data externally.
  - Callback plugins: plugins that are used to collect usage ifformation about Ansible.
- And more: see https://docs.ansible.com/ansible/latest/plugins/plugins.html for a complete list.
```bash
ansible-doc -t help
ansible-doc -t cache -l
ansible-doc -t callback -l
ansible-doc -t lookup -l
```

### 11.2 Exploring Lookup Plugins

#### Exploring Lookup Plugins

- Lookup plugins are created to use data from external sources like files and environment variables.
- Many lookup plugins are provided.
- Use **ansible-doc -t lookup -l** for a complete list.
- Use **ansible-doc -t lookup plugin-name** for documentation of a specific plugin.

#### Using Lookup Plugins

- Lookup plugins can be called in two ways: **lookup** and **query**
  - **lookup** is used to read file content into a variable
  - **query** is used to read the file content into a variable, where file contents is stored as a list.

#### Useful Lookup Plugin Overview

- **file:** reads content of files from the control node.
- **template:** processes the contents of a template.
  - {{ lookup('template', 'mytemplate.j2') }}
- **env:** uses an environment variable that is set on the control node.
  - {{ lookup( 'env', 'DB_PASSWORD' ) }}
- **url:** gets the contents from a URL.
  - {{ lookup('url', 'http://example.com') }} 
- **pipe**: returns the output of a command that is executed on the control host.
  - {{ query('pipe', 'ls files') }}
- **k8s**: fetches a Kubernetes object.
  - {{ lookup('k8s', kind='Deployment', namespace='default') }}

#### Using the file Lookup Plugin

- The following example uses the **file** lookup plugin to read the contents of the file /etc/passwd into the variable myusers.
```yaml
---
vars:
  myusers: "{{ lookup('file', '/etc/passwd') }}"
```
- The file plugin can take multiple filenames as its argument, where each file contents will be separated by a comma.
```yaml
---
vars:
  myfiles: "{{ lookup('file', '/etc/passwd', '/etc/motd') }}"
```
- Use query to store the file contents in a list:
```yaml
---
vars:
  myfiles: "{{ lookup('file', '/etc/passwd', '/etc/motd') }}"
```
- See **readkeys.yaml** for an example
```bash
cd plugins
vim readkeys.yaml
ansible-playbook readkeys.yaml
```

### 11.3 Using Common Lookup Plugins

#### Using env and template

- The **env** lookup plugin is used to set a variable based on the value of a shell variable on the managed host.
- Combined with the **default** filter this has nice potential to automatically modify content based on local settings.
- In particular, when combined with the **template** lookup plugin it can be useful.
- Notice that the **template** lookup plugin is not the same as the **template** module: the **template** plugin is used to generte text that can be used in modules like **copy** 
- See **setlanguage.yaml**
```bash
cd plugins
vim setlanguage.yaml
ansible-playbook setlanguage.yaml
``` 

#### Using pipe and lines

- The **pipe** and **lines** lookup plugins are used to return output from a command that has been used on the control node.
- **pipe** shows raw (unformatted output)
- **lines** splits the output in lines that can be treated as a list.
- See **lines.yaml** for an example.
  - Tip: In the example file, change "lines" to "pipe" and observe the difference.
```bash
cd plugins
vim lines.yaml
ansible-playbook lines.yaml
```

#### Using url

- The **url** lookup plugin can be used to fetch content from a URL.
- The main benefit is that this allows you to use data returned as values in variables.
- Notice that for more generic use, the **uri** module can be used.
- See **url.yaml** for an example.
```bash
cd plugins
vim url.yaml
ansible-playbook url.yaml
vim users.txt
vim makeusers1.yaml
ansible-playbook makeusers1.yaml
ansible-playbook makeusers2.yaml
ansible ansible2 -a "tail /etc/shadow"
```

### 11.4 Using the fileglob Lookup Plugin

#### Understanding the fileglob Lookup Plugin

- The **fileglob** lookup plugin can be used to iterate over a list of files according to a globbing pattern.
- When used as {{ lookup('fileglob', '*') }} it will provide a string of comma-separated values for all files in the output.
- To force the lookup plugin to return a list of values instead of a string of comma-separated values, use the **query** keyword instead of **lookup**
  - **{{ query('fileglob', '*') }}**
  - In the output, you see that it's a list because the data is encapsulated by brackets.
```bash
cd plugins
vim fileglobstring.yaml
ansible-playbook fileglobstring.yaml
vim filegloblist.yaml
ansible-playbook filegloblist.yaml
```

#### Using fileglob with Wildcards

- The Ansible **copy** module doesn't support wildcards.
- Use the **fileglob** filter in a loop if you want wildcard functionality.
- Notice that this is not recommended for copying many files, as for every single file the **copy** module will be called.
```bash
touch ~/testfiles/file{1..100}.txt
vim wildcardcopy1.yaml
ansible-playbook wildcardcopy1.yaml

vim wildcardcopy2.yaml
ansible-playbook wildcardcopy2.yaml
```

### 11.5 Using Callback and Timer Plugins

#### Using Callback Plugins

- Callback plugins extend Ansible by modifying how it responds to events.
- To do their work, callback plugins modify the output of the ansible commands.
- Use **ansible-doc -t callback -l** for a complete list.
- Use **ansible-doc -t callback <plugin>** for more information on how to use a specific plugin.
- Specific plugins can be enabled in ansible.cfg, using **callback_whitelist**
  - **callback_whitelist=timer, profile_tasks, cgroup_perf_recap**

#### Using cgroup_perf_recap

- **cgroup_pref_recap** allows you to monitor detailed resource usage when running a playbook.
- Use it to measure impact after changing the forks parameter.
- **cgroup_perf_recap** is based on Cgroups functionality.
- Cgroups allow for system performance tuning and monitoring.
- Currently, **cgroup_perf_recap** needs Cgroups v1 support.
- To change back to Cgroup v1 (verified on Fedora)
  - Edit /etc/default/grub and add systemd.unified_cgroup_hierarchy=0 to the end of the line that loads the kernel.
  - Use **sudo grub2-mkconfig -o /boot/grub2/grub.cfg** rewrite Grub config.

#### Demo: Using cgroup_perf_recap

```bash
# Ensure the following is in ansible.cfg
[defaults]
callback_whitelist=cgroup_perf_recap

[callback_cgroup_perf_recap]
control_group=ansible_profile

# Create the dedicated Cgroup:
sudo cgcreate -a ansible:ansible -t ansible:ansible -g cpuacct,memory,pids:ansible_profile # Replace ansible:ansible with the user:group that runs the playbook
vim cgcreate.yaml
ansible-playbook cgcreate.yaml

# Run the playbook as an argument to the cgexec command.
cgexec -g cpuacct,memory,pids:ansible_profile ansible-playbook cgcreate.yaml
```

#### Using Specific Callback Plugins

- **timer** shows the duration of playbook execution.
- **profile_tasks** shows start time of each tasks, as well as how much time spent.
- **profile_roles** does the same for roles.

#### Demo: Using Timer Callback Plugins

```bash
# Comment other cgroup lines.
# Edit ansible.cfg to include reqired plugins.
[defaults]
callback_whitelist=timer,profile_tasks,profile_roles

# Run the playbook to see detailed usage information about all tasks.
ansible-playbook cgcreate.yaml
```

### 11.6 Using Plugin-Based Inventory

#### Using Plugin-Based Inventory

- Inventory can be written in ini format (old) as well as YAML format (new).
- Inventory since Ansible 2.4 is managed through plugins, the ansible.cfg lists which plugins are used in the [inventory] section.
- Using plugins allows Ansible to support new Inventory format by just providing a new plugin.
  - ini plugin supports old-style invenotory format.
  - script plugin supports old-style dynamic inventory.
  - yaml plugin supports new style YAML format.
- Using plugins is preferred over using dynamic inventory scripts.
```bash
cd plugins
sudo vim /etc/ansible/ansible.cfg
- search for #inventory_plugins
```

#### Using the ini Plugin

```ini
# ini-based inventory example.
[webservers]
server1.example.com
server2.example.com

[dbservers]
server3.example.com
server4.example.com

[allservers:children]
webservers
dbservers
```

#### Using the YAML Plugin

```yaml
# YAML-based inventory example.
allservers:
  children:
    webservers:
      server1.example.com
      server2.example.com
    dbservers:
      server3.example.com
      server4.example.com
```
```bash
ansible-doc -t inventory -l;
ansible-doc -t inventory ini
ansible-doc -t inventory yaml
ansible-doc -t inventory k8s
```

#### Converting ini Inventory

```bash
cd windows
vim inventory

# Use below command to convert ini-based inventory to YAML-based inventory.
ansible-inventory
ansible-inventory --yaml -i inventory --list --output inventory.yaml

# demo.
ansible-inventory --yaml -i ~/ansible/windows/inventory --list --ouput winventory.yaml
```
- Important: when the ini-based inventory contains variables, these may be messed up after conversion. You will need to manually fix this.
- To avoid this, use the recommended approach of putting your vairables in group_vars/and host_vars/

#### Understanding Inventory Sources

- Inventory is plugin-based.
- Use **ansible-doc -t inventory -l** for a complete list.
- The **[inventory] enable_plugins** option in ansible.cfg determines which plugins are enabled.
  - **enable_plugins = host_list, script, auto, yaml, ini, toml**
  - Notice that legacy inventory scritps are still supported using the script plugin.
- Additional inventory plugins can be added in project-based or generic ansible.cfg

### 11.7 Configuring Fact Caching

#### Using Fact Caching

- After fact gathering, facts are kept in memory and stay there for the duration of playbook execution.
- Plugins can be used to enable fact caching.
- When using a plugin, facts should be gathered manually or as a scheduled job that is executed after expiration of the fact cache.
- Next, all playbooks can run without fact gathering and access facts from the fact cache.

#### Demo: Configuring the redis Plugin

- Redis is an in-memory database that can be used to cache data. Install it on the controller node.

```bash
ansible-doc -t cache -l;
ansible-doc -t cache redis;
sudo dnf install -y redis;
sudo systemctl enable --now redis;
sudo pip3 install redis;
```
- Use ansible.cfg to specify plugin use.
```bash
vim ansible.cfg
fact_caching = redis
fact_caching_timeout = 3600
fact_caching_connection = localhost:6379:0
```

#### Using a Fact Cache

```bash
cd factcache/
./checkcache.py
# Command to populate the fact cache.
ansible all -m setup
./checkcache.py
ansible-playbook checkfacts.yaml
```

#### Fact Caching Caveats

- Once the fact cache expires, all playbooks that require facts and have **gather_facts: False** will fail.
- Run a scheduled job to refresh the fact cache automatically.
- To ensure a playbook does NOT use cache (but gathers facts instead) use **ansible-playbook whatever.yaml --flush-cache**

### 11.8 Creating Random Passwords

#### Using the password Lookup Plugin

- The **password** Lookup Plugin can be used to generate random passwords and store these passwords in a local file.
- Notice that strictly, the **password** plugin generates a random string, using it as a password makes it a password.
- Use it to define a variable: mypassword: "{{ lookup('password', 'credentials/' + item + ' length=6') }}"
  - This defines a directory with the name credentials, with a file that matches the username so that the password can be handed out to the user later.
- After defining the variable, use it as a password by applying the **password_hash** filter.
- See **userswithpassword.yaml** for an example.
- Use **cleanupusers.yaml** to clean up the users that were just created.
```bash
cd plugins
vim userswithpassword.yaml
cat users.txt
ansible-playbook userswithpassword.yaml
vim cleanupusers.yaml
ansible-playbook cleanupusers.yaml
```

### Lesson 11 Lab Configuring Fact Caching

- Configure a redis-based fact cache.

### Lesson 11 Lab Solution Configuring Fact Caching

```bash
mkdir lesson11lab
vim ansible.cfg
sudo dnf install -y redis;
sudo systemctl status redis;
sudo pip3 install redis
ansible all -m setup;
ansible all -m setup -K;
vim cachecheck.yaml
ansible-playbook cachecheck.yaml -K
```
