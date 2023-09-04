# Lesson 17 - Managing Network Devices with Ansible

- [Lesson 17 - Managing Network Devices with Ansible](#lesson-17---managing-network-devices-with-ansible)
    - [17.1 Understanding Network Device Management](#171-understanding-network-device-management)
      - [Managing Network Devices](#managing-network-devices)
      - [How Network Automation is Different](#how-network-automation-is-different)
      - [Understanding Network Device Modules](#understanding-network-device-modules)
      - [Taking the Next Steps](#taking-the-next-steps)
    - [17.2 Setting Up Cisco SMB Devices](#172-setting-up-cisco-smb-devices)
      - [Introducing the Devices](#introducing-the-devices)
      - [Cisco Switches for Dummies](#cisco-switches-for-dummies)
      - [Demo: Configuring the Switch](#demo-configuring-the-switch)
      - [Demo: Configuring SSH Access to a Cisco Switch](#demo-configuring-ssh-access-to-a-cisco-switch)
      - [Configuring the SSH Client](#configuring-the-ssh-client)
    - [17.3 Configuring Cisco SMB Devices with Ansible](#173-configuring-cisco-smb-devices-with-ansible)
      - [Tuning Device Connection Settings](#tuning-device-connection-settings)
      - [Preparing Host Software](#preparing-host-software)
      - [Understanding Available Modules](#understanding-available-modules)
      - [Creating the Switch Inventory](#creating-the-switch-inventory)
      - [Demo: Managing Cisco Devices](#demo-managing-cisco-devices)
    - [17.4 Using Generic Modules for Network Device Management](#174-using-generic-modules-for-network-device-management)
      - [Understanding netcommon](#understanding-netcommon)
    - [Lesson 17 Lab Automating Switch Setup with Ansible](#lesson-17-lab-automating-switch-setup-with-ansible)
    - [Lesson 17 Lab Solution Automating Switch Setup with Ansible](#lesson-17-lab-solution-automating-switch-setup-with-ansible)

### 17.1 Understanding Network Device Management

#### Managing Network Devices

- To manage network devices, you need modules.
- Modules exist for many network devices, but not all, see https://www.ansible.com/integrations/networks for an overview.
- Network devices need to be identified in inventory.
- Using dynamic inventory is usggested.
- Connecting to network devices works on SSH in many cases, sometimes you will need a different connection protocol.
- For more information: see "Network Automation" in docs.ansible.com

#### How Network Automation is Different

- Modules are executed on the control node.
- Number of forks shouldn't be set higher than 5.
- If a backup of configuration files is defined, this backup is also stored on the control node.
- Multiple communication protocols are available.
  - ansible_connection: local -> provider specific protocol.
  - ansible_connection: network_cli -> CLI over SSH
  - ansible_connection: netconf -> XML over SSH
  - ansible_connection: httpapi -> API over HTTP/HTTPS
- Connection type is determined by teh device you want to manage.

#### Understanding Network Device Modules

- Modules to manage network devices are developed in a consistent way.
  - Name starts with the platform.
  - Next, there is the specific function, like **facts**, **ping** and many more.
  - The number of modules for a platform heavily depends on support by the platform vendor: many for Cisco IOS, not as many for other platforms.

#### Taking the Next Steps

- For managing network devices, different modules are available for specific platforms.
- To automate setting up common tasks, multiple roles and collections are provided as well.
- See **https://galaxy.ansible.com** for an overview of roles and collections.

### 17.2 Setting Up Cisco SMB Devices

#### Introducing the Devices

- Cisco SG250-8 and SG350-8 are affordable switches for testing.
- They provide full Cisco IOS functionality but introduce some additional challenges.
  - SSH Access is Paramiko-based, and that requires additional configuration.
  - Use **community.ciscosmb** to manage them.
    - **ansible-galaxy collection install community.ciscosmb**
  - Some **ios_** modules will work, but SMB devices may lack support for specific functionality.
- Ansible developers have never aimed at these types of switches, which makes configuration challenging.

#### Cisco Switches for Dummies

- Google for default admin and password, often admin and cisco not guaranteed.
- Connect the switch directly to a Linux machine using a network cable (no switch).
- Use **tcpdump -i eth0** to discover network traffic. The switch should reveal its IP Address.
- Use **nmap -sn 192.168.1.0/24** to discover nodes on the network.
- Connect using SSH, but change default SSH access: **ssh -oKexAlgorithms=+diffie-hellman-group1-sha1 -c aes128-ctr 192.168.1.10** and log in to shell.

#### Demo: Configuring the Switch

- From and SSH interface.
  - configure
  - int vlan 1
  - ip address 192.168.1.250 255.255.255.0
- At this point you've lost connection as you just changed the IP address. Reconnect from another tty.
  - exit
  - show ip interface
  - copy run start
  - reload
- You have now configured the switch with its default config.

#### Demo: Configuring SSH Access to a Cisco Switch

- Ensure SSH access is enabled at the Cisco switch (use Web UI)
  - Check **Status and Statistics > System Summary**
  - Set: IP Configuration > Security > TCP/IP Services
- ssh admin@switch-ip # This will also store the device SSH identiry.
  - show interface status
  - show ip interface
  - configure
  - ip ssh password-auth
  - ip ssh pubkey-auth
  - exit
  - copy run start
  - exit

#### Configuring the SSH Client

- For user Ansible, configure SSH config in **.ssh/config** with the following entries for each switch you want to manage.
```bash
Host 192.168.1.250
KexAlgorithms +diffie-hellman-group1-sha1
Ciphers aes128-ctr
```
- Notice that this is for IP hosts, not for inventory hosts.
- At this point, you should have SSH access to the switch.

### 17.3 Configuring Cisco SMB Devices with Ansible

#### Tuning Device Connection Settings

- SSH is the common way to connect to devices.
- To connect to devices efficiently, the SSH feature ControlPersist is enabled by default.
- ControlPersist keeps connections to servers open as a socket, so that Ansible can avoid reconnecting to hosts at each tasks.
- Include the following in ansible.cfg
```ini
[persistent_connection]
command_timeout = 180
connect_timeout = 100
connect_retry_timeout = 100
```

#### Preparing Host Software

- Ensure the required SMB modules are installed: **ansible-galaxy collection install community.ciscosmb**
- If managed devices are using an older SSH version, Ansible will fall back to the Python implementation of OpenSSH called Paramiko.
- Paramiko must be installed on the Ansible control node.
  - **sudo pip3 install paramiko**

#### Understanding Available Modules

- **ios_** modules are developed for heavy-duty Cisco devices.
  - **ios_** modules address lots of functionality that isn't offered by SMB devices.
- **ciscosmb** is a relatively new module that focusses on managing Cisco SMB devices.
  - still under heavy development.

#### Creating the Switch Inventory

```bash
vim inventory-smb
vim inventory-ios
```

#### Demo: Managing Cisco Devices

```bash
ansible-playbook -i inventory-smb smbfacts.yaml
ansible-playbook -i inventory-smb show-current-access-vars.yml
ansible-playbook -i inventory-smb iosbackup.yml
```

### 17.4 Using Generic Modules for Network Device Management

#### Understanding netcommon

- When managing multiple different network devices, you would need to use device-specific modules in all cases.
- Consider using the **ansible.netcommon** collection instead. 
- It uses CLI functionality agaist a wide range of different network devices.
- It uses common plugins to connect to a wide range of devices.

### Lesson 17 Lab Automating Switch Setup with Ansible

- Use a network device of your choice and manage it with Ansible in such a way that you can get an inventory from the network device.
- Make a backup of the device configuration, using the appropriate module.

### Lesson 17 Lab Solution Automating Switch Setup with Ansible

```bash
cd cisco/
ansible-doc -l | grep ^ios | less
ansible-doc ios_config
vim inventory-smb
vim lab17.yml 
ansible-playbook -i inventory-smb lab17.yml
ls backup -l
ansible-playbook -i inventory-ios lab17.yml
ls backup -l
```
