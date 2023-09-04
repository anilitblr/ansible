# Lesson 18: Managing Virtual Machines with Ansible

- [Lesson 18: Managing Virtual Machines with Ansible](#lesson-18-managing-virtual-machines-with-ansible)
    - [18.1 Managing KVM Virtual machines](#181-managing-kvm-virtual-machines)
      - [Understanding teh Procedure](#understanding-teh-procedure)
    - [18.2 Understanding vSphere Management](#182-understanding-vsphere-management)
      - [Understanding Requirements](#understanding-requirements)
      - [Using TLS Certificates](#using-tls-certificates)
      - [Using Dynamic Inventory](#using-dynamic-inventory)
    - [18.3 Managing ESXi](#183-managing-esxi)
      - [Preparing the ESXi Host](#preparing-the-esxi-host)
      - [Preparing an ESXi Host for Ansible Management](#preparing-an-esxi-host-for-ansible-management)
    - [Lesson 18 Lab Managing a KVM Based Virtual Classroom with Ansible](#lesson-18-lab-managing-a-kvm-based-virtual-classroom-with-ansible)
    - [Lesson 18 Lab Solution Managing a KVM Based Virtual Classroom with Ansible](#lesson-18-lab-solution-managing-a-kvm-based-virtual-classroom-with-ansible)

### 18.1 Managing KVM Virtual machines

#### Understanding teh Procedure

- KVM virtual machines are deployed on top of the Linux internal KVM hypervisor.
- KVM virtual machines are managed by libvirtd, a daemon that must be running on the manged hosts.
- The foundation of any KVM virtual machine is twofold.
  - An XML configuration file in /etc/libvirt/qemu
  - A diks file in /var/lib/libvirt/images
- While creating a virtual machines, a fresh installation can be done, or an existing disk file can be used a template.
- The following demo shows how to use existing disk files using the virt module.

### 18.2 Understanding vSphere Management

#### Understanding Requirements

- Detailed information is in "Introduction to Ansible fo VMware" in docs.ansible.com
- Ansible modules for managing VMware are written on top of **pyVmomi**
  - Use **sudo pip3 install pyvmomi**
- **pyVmomi** is also a part of vSphere automation Python SDK, better install that as it contains support for many more VMware porducts.
  - pip3 install --upgrade git+https://github.com/vmware/vsphere-automation-sdk-python.git

#### Using TLS Certificates

- You must enable and use SSL encryption for Ansible to connect to either vCenter or ESXi.
- Certificates need to be installed on either the control node, or the delegate node.
- For specific instructions, see https://docs.ansible.com/ansible/2.9/scenario_guide/vmware_scenarios/vmware_requirements.html

#### Using Dynamic Inventory

- To manage virtual machines in a VMware environment, use the dynamic inventory plugin.
- To use it, start by including it in ansbile.cfg
```ini
[inventory]
enable_plugins = vmware_vm_plugin
```
- In this, **vmware_vm_plugin** is the name of the inventory script - see course Git repo for an example.
- Next, create a file that ends in **.vmware.yaml** in the working directory.
- After setting up dynamic inventory, use **ansbile-inventory --list -i vmware_vm_inventory.vmware.yaml**
```bash
cd vmware/
ansible-doc -l | grep ^vmw
vim create_vmw_vm.yaml
```

### 18.3 Managing ESXi

#### Preparing the ESXi Host

- VMWare modules are focussing on managing vSphere.
- Individual ESXi hosts can be managed after enabling SSH on the ESXi host.
  - Log in to the ESXi web UI.
  - Select Manage > Service > TSM_SSH
  - Click Actions > Policy > Start and Stop with Host.

#### Preparing an ESXi Host for Ansible Management

- /etc/hosts is configured to reach hosts by name.
- User ansible exists on control host.
- Root SSH access to remote hosts.
- Create **inventory** with **esxi** host name.
- **ansible all -m user -a "name=ansible" -i inventory -i -u root**
- **ansilbe all -m shell -a "echo password | passwd --stdin ansible" -i inventory -i -u root**
- **ansilbe all -m copy -a 'content="ansible ALL=(ALL) NOPASSWD: ALL" dest=/etc/sudoers.d/ansible' -i inventory -i -u root**
- **cat esxi/setup-esxi.yaml**
```bash
sudo pip3 install pyvmomi
cd esxi/
vim setup-esxi.yaml
ansible-playbook setup-esxi.yaml -k
```

### Lesson 18 Lab Managing a KVM Based Virtual Classroom with Ansible

- Write a playbook that sets up the complete KVM stack on a Linux based host, including all dependencies.
- Create a virtual machine on your virtualization host.

### Lesson 18 Lab Solution Managing a KVM Based Virtual Classroom with Ansible

```bash
cd kvm/
vim kvm-setup.yml
ansible-plabook kvm-setup.yml -K
```
