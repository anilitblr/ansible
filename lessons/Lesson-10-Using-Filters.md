# Lesson 10 - Using Filters

- [Lesson 10 - Using Filters](#lesson-10---using-filters)
    - [10.1 Understanding Filters and Variable Types](#101-understanding-filters-and-variable-types)
      - [Understanding Filters](#understanding-filters)
      - [Understanding Variable Types](#understanding-variable-types)
      - [Recognizig Variable Types](#recognizig-variable-types)
    - [10.2 Using Filters to Change Variables](#102-using-filters-to-change-variables)
      - [Processing Variables with Filters](#processing-variables-with-filters)
      - [Exploring Common Filters](#exploring-common-filters)
      - [Demo: Exploring Filters](#demo-exploring-filters)
    - [10.3 Using Filters to Work with Network Addresses](#103-using-filters-to-work-with-network-addresses)
      - [Understanding the ipaddr Filter](#understanding-the-ipaddr-filter)
    - [10.4 Using Filters in Loops](#104-using-filters-in-loops)
      - [Understanding the map filter](#understanding-the-map-filter)
      - [Understanding the flatten filter](#understanding-the-flatten-filter)
      - [Understanding the subelements filter](#understanding-the-subelements-filter)
      - [Understanding the dict2items Filter](#understanding-the-dict2items-filter)
    - [Lesson 10 Lab Using Filters](#lesson-10-lab-using-filters)
    - [Lesson 10 Lab Solution Using Filters](#lesson-10-lab-solution-using-filters)

### 10.1 Understanding Filters and Variable Types

#### Understanding Filters

- A filter is a lookup plugin that allows you to manipulate data.
- Many filters are available in Ansible.
- A part from that, Jinja2 filters can be used in Ansible.
- Filters process the value of a variable on the control host before further using it in the playbook.
- While using filters, it is important to know which variable type you're dealing with.

#### Understanding Variable Types

- String: sequence of characters - the default variable type in Ansible.
- Numbers: numeric value, treated as integer or float. When placing a number in quotes it is treated as a string.
- Booleans: true/false values (yes/no, y/n), on/off also supported).
- Dates: calendar dates.
- Null: undefined variable type.
- List of Arrays: a sorted collection of values.
- Dictionary of Hash: a collection of key/value pairs.

#### Recognizig Variable Types

- In the output of, for instance, fact gathering, different variable types can be recognized by the way in which they are written.
- String: a value between quotes: **"config_mode":"enforcing"**
- Numbers: a value that is not between quotes: **"serial": 0**
- Dates: **"date": "2023-07-23" **
- Null: undefined variable type - only occurs on undefined variables.
```bash
cd plugins
vim vartypetest.yaml
ansible-playbook vartypetest.yaml
```
- List or Arrays: a sorted collection of values.
```bash
"ansible_system_capabilities": [
    "cap_chown",
    "cap_kill"
],
```
- Dictionary or  Hash: multiple values, written between braces.
```
"ansible_selinux": {
    "config_mode":"enforcing",
    "type":"targeted"
},
```

### 10.2 Using Filters to Change Variables

#### Processing Variables with Filters

- Filters allow variables to be processed before using them in Ansible.
- Filters do not change the value of a variable, they just change how the variable is being used.
- Use {{ varname | filter }} to identify the filter to be used.
- See **int_filter.yaml** and **storage_filter.yaml** for examples.
```bash
cd filters/
vim int-filter.yaml
ansible-playbook int-filter.yaml
vim storage-filter.yaml
```

#### Exploring Common Filters

- **mandatory** fails a play if a variable does not have a value: **{{ my_var | mandatory }}**
- **default** will set a variable without value to a default value. Add the optional True to also st the variable if it has an empty string or a boolean False as its value: **{{ my_var | default(myvalue, True) }}**
- **capitalize** will capitalize a string.
- **int** will convert a variable to an integer.
- **float** converts a variable to a float.
- **+ - / *** perform basic caluclations: **{{ (vgsize | int ) -1 }}**
- **union** creates a single list based on multiple input lists.
- **random** extracts a random element from a list: **{{ [a, b, c] | random }}**
- **sort** will sort a list **{{ [4, 8, 2, 6] | sort }}**
- **password_hash:** generates a hashed password.
- **quote**: used to put command output between quotes so that it is sanitized.

#### Demo: Exploring Filters

```bash
vim assert_filter.yaml
ansible-playbook assert_filter.yaml
vim password_hash.yaml
ansible-playbook password_hash.yaml -K
```

### 10.3 Using Filters to Work with Network Addresses

#### Understanding the ipaddr Filter

- The **ipaddr** filter works on IP addresses to show specific IP address-related output.
- Before using, install the **python3-netaddr** as well as **python3-dns** package.
- It has different arguments that allow you to perform specific manipulations.
  - **address:** validates that input contains valid IP addresses.
  - **net:** validates that input values are network ranges.
  - **host:** ensures that IP addresses conform to CIDR perfix format.
  - **prefix:** returns the network address prefix.
  - and many more.
- Look for **ipaddr filter** in the documentation for a complete list.
```bash
sudo dnf install -y python3-netaddr python3-dns
vim network.yaml
ansible-playbook network.yaml
```

### 10.4 Using Filters in Loops

#### Understanding the map filter

- The **map** filter is used to lookup an attribute.
- It is useful when dealing with lists of objects where you are only interested in one specific value.
  - If for instance the **find** module is used to find files, multiple attributes are shown and **map** can be used to filter just one of them.
  - **map** can work with optional arguments, such as the **relpath** function, which is useful in displaying filenames raltive to a directory.
- Notice that **map** returns a list by default, To show the output as line, use the **join** filter as well.
```bash
cd filters/
vim filemap.yaml
ansible ansible2 -m file -a "path=/var/www/html state=directory" -K
ssh ansible2
ls /var/www/html
exit
ansible-playbook filemap.yaml
```

#### Understanding the flatten filter

- **flatten** recursively searches list items and flattens them into one list.
- This is useful when getting multiple items out of a hierarchical list.
- Have a look at **plat.yaml** for a simple example.
```bash
cd filters/
vim plat.yaml
ansible-playbook plat.yaml
```

#### Understanding the subelements filter

- The **subelements** filter allows you to create a new list based on subelements in complex data structures.
- A subelements is a list within a list, and while using subelements the top level item in the list is referred to as **item.0** and the second level item in the list as **item.1**
- See dbvars.yaml and dbuser.yaml for an example.
```bash
cd filters/
vim dbvars.yaml
vim dbuser.yaml
ansible-playbook dbuser.yaml
```

#### Understanding the dict2items Filter

- You cannot use loop over a dictionary.
- Use **dict2items** to transform a dictionary into a list and allow looping over it.
```bash
cd filters/
vim dict2items.yaml
ansible-playbook dict2items.yaml
```

### Lesson 10 Lab Using Filters

- Write a playbook that configures firewall rules. The playbook should define variables to specify what should happen in the firewall regarding specific service. Make sure you work at least with the name of the service, the state you need this service to be in, and the firewall zone in which it should be configured.
- Also make sure that if the state is not specified for a service, the defautl state "enabled" will be used, and make sure that if the zone is not specified, it will be omitted.

### Lesson 10 Lab Solution Using Filters

````bash
cd filters/
vim filtwall.yaml
ansible-playbook filtwall.yaml
```
