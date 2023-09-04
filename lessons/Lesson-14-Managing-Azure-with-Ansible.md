# Lesson 14 - Managing Azure with Ansible

- [Lesson 14 - Managing Azure with Ansible](#lesson-14---managing-azure-with-ansible)
    - [14.1 Understanding Requirements for Managing Azure](#141-understanding-requirements-for-managing-azure)
      - [Requirements for Managing Azure](#requirements-for-managing-azure)
      - [Registering Azure Credentials](#registering-azure-credentials)
      - [Managing Azure from Tower](#managing-azure-from-tower)
    - [14.2 Using Playbooks to Manage Azure](#142-using-playbooks-to-manage-azure)
      - [Managing Azure with Ansible](#managing-azure-with-ansible)
    - [Lesson 14 Lab Managing Azure](#lesson-14-lab-managing-azure)
    - [Lesson 14 Lab Solution Managing Azure](#lesson-14-lab-solution-managing-azure)

### 14.1 Understanding Requirements for Managing Azure

#### Requirements for Managing Azure

- On Azure: register an application with Azure AD and create a service principal / Azure Active Directory user.
- See also https://docs.ansible.com/ansible/latest/scenario_guides/guide_azure.html
- Up to Ansible 2.9: On Ansible Controller: use **sudo pip3 install 'ansible[azure]'**
- Ansible 2.10 and later: On Ansible Controller, use **ansible-galaxy collection install azure.azcollection** 

#### Registering Azure Credentials

- To access Azure with Ansible using a Service Principal, you need to set 4 variables.
- Make sure to treat them securely as these give access to create unlimited resources on Azure.
  - AZURE_CLIENT_ID
  - AZURE_SECRET
  - AZURE_SUBSCRIPTION_ID
  - AZURE_TENANT
- Store these in a file in $HOME/.azure/credentials
```ini
[default]
subscription_id=xxxxxxxxxx
client_id=xxxxxxxxxx
secret=xxxxxxxxxx
tenant=xxxxxxxxxx 
```

#### Managing Azure from Tower

- Set Inventory to Localhost.
- Set Credentials to Azure RM.
- Set Project to Git repo containing your playbooks.
- Create a Template using all of these (change credentials type to Azure)
- Run it.

### 14.2 Using Playbooks to Manage Azure

#### Managing Azure with Ansible

- Use **localhost** as host.
- Notice that some Azure modules are not idempotent.
```bash
cd azure/

# Provide sample playbooks
vim create-azure-stuff-old.yaml
ansible-playbook create-azure-stuff-old.yaml
ansible-playbook --help
ansible-playbook --start-at-task "Create virtual machine" create-azure-stuff-old.yaml
ansible-doc -l | grep ^azure_rm

# As you will notice while processing, order does matter.
vim remove-azure-stuff-old.yaml
ansible-playbooks remove-azure-stuff-old.yaml
``` 

### Lesson 14 Lab Managing Azure

- Remove all resources from the Azure environment you have just created.

### Lesson 14 Lab Solution Managing Azure

```bash
# As you will notice while processing, order does matter.
vim remove-azure-stuff-old.yaml
ansible-playbooks remove-azure-stuff-old.yaml
```
