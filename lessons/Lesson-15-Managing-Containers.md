# Lesson 15: Managing Containers

- [Lesson 15: Managing Containers](#lesson-15-managing-containers)
    - [15.1 Understanding Requirements for Managing Docker](#151-understanding-requirements-for-managing-docker)
      - [Understanding Requirements](#understanding-requirements)
      - [High-level Overview](#high-level-overview)
    - [15.2 Using Playbooks to Manage Docker](#152-using-playbooks-to-manage-docker)
    - [15.3 Managing Podman Containers](#153-managing-podman-containers)
      - [Understanding Podman Containers](#understanding-podman-containers)
    - [Lesson 15 Lab Managing Containers](#lesson-15-lab-managing-containers)
    - [Lesson 15 Lab Solution Managing Containers](#lesson-15-lab-solution-managing-containers)

### 15.1 Understanding Requirements for Managing Docker

#### Understanding Requirements

- To manage Docker containers, the **dockerd** daemon must be installed and started.
- Next, different specific modules can be used to manage Docker containers.
- Use **ansible-doc -l | grep docker** for an overview.
- Do NOT use the **docker** modules for managing **podman** containers on RedHat.

#### High-level Overview

- Add repository to install Docker.
- Install and start the Docker daemon.
- Install Python pip module to support Docker.
- Create a container.
- Generate a list of running containers.
 
### 15.2 Using Playbooks to Manage Docker

```bash
cd docker/
vim docker_main.yaml
vim docker-ubuntu.yaml
vim docker-centos.yaml 
ansible-playbook docker_main.yaml -K
```

### 15.3 Managing Podman Containers

#### Understanding Podman Containers

- **podman** is the Red Hat Enterprise Linux 8 and later native way to run containers.
- **podman** is also available on other distributions.
- To start podman containers, ensure that the podman software package is installed.
- There is no need to run any daemon to start podman containers.
- Also, podman can run rootless containers: these do not rquire any root privileges but can run with ordinary user credentials.
```bash
cd docker/
ansible-galaxy collection install containers.podman
vim podman.yaml
ansible-playbook podman.yaml
anisble ansible2 -a "podman ps"
```

### Lesson 15 Lab Managing Containers

- Set up your favorite Linux platform as a host to run containers.
- Create a playbook that will run an nginx container.
- Have the playbook display a list of currently running containers.

### Lesson 15 Lab Solution Managing Containers

```bash
cd docker/lob
vim podman-rh.yaml
ansible-playbook runcontainer.yaml
```
