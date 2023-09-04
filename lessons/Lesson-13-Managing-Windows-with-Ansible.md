# Lesson 13 - Managing Windows with Ansible

- [Lesson 13 - Managing Windows with Ansible](#lesson-13---managing-windows-with-ansible)
    - [13.1 Understanding Requirements for Managing Windows](#131-understanding-requirements-for-managing-windows)
      - [Understanding Requirements](#understanding-requirements)
    - [13.2 Using Playbooks to Manage Windows](#132-using-playbooks-to-manage-windows)
      - [Understanding Useful Windows Modules](#understanding-useful-windows-modules)
      - [Using Playbooks to Manage Windows](#using-playbooks-to-manage-windows)
    - [Lesson 13 Lab Managing Windows with Ansible](#lesson-13-lab-managing-windows-with-ansible)
    - [Lesson 13 Lab Solution Managing Windows with Ansible](#lesson-13-lab-solution-managing-windows-with-ansible)

### 13.1 Understanding Requirements for Managing Windows

#### Understanding Requirements

- All recent Windows versions are supported by Ansible.
- In order to manage Windows, remote management must be enabled.
- Also, you must set authentication properly.
- Consult Lesson 2 for details of how to set up Windows hosts to be managed by Ansible.
```bash
cd windows/
vim inventory
ansible win -m win_ping
```

### 13.2 Using Playbooks to Manage Windows

#### Understanding Useful Windows Modules

- **ansible.windows.win_command**: runs a command (not idempotent).
- **ansible.windows.win_shell**: runs powershell commands.
- **ansible.windows.win_package**: installs software from MSI files or executable packages.
- **ansible.windows.win_feature**: manages system roles or Windows features.
- **ansible.windows.win_update**: updates Windows.
- **ansible.windows.win_reboot**: reboots Windows.
- **ansible.windows.win_format**: formats storage devices.

#### Using Playbooks to Manage Windows

- **ansible-playbook playbook.yml**
- Verify on Windows by showing the users in the control panel.
- **ansible-playbook createad.yml**
  - Will make Administrator a domain administrator, using the same password.
```bash
cd windows/
ansible-doc -l | grep ^win
vim playbook.yml
ansible-playbook playbook.yml
vim wiebenik.yaml
ansible-playbook wiebenik.yaml
vim createad.yml
ansible-playbook createad.yml
```

### Lesson 13 Lab Managing Windows with Ansible

- Set up a recent Windows server for management with Ansible.
- Create a playbook that runs the whoami.exe command, and shows the result after running the playbook.

### Lesson 13 Lab Solution Managing Windows with Ansible

- Consult Lesson 2 for details of how to set up Windows hosts to be managed by Ansible.
```bash
cd windows/
ansible win -i inventory -m setup
vim wiebenik.yaml
ansible-playbook wiebenik.yaml
```
