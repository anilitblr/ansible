# Lesson 19: Managing Kubernetes with Ansible

- [Lesson 19: Managing Kubernetes with Ansible](#lesson-19-managing-kubernetes-with-ansible)
    - [19.1 Understanding Requirements for Managing Kubernetes](#191-understanding-requirements-for-managing-kubernetes)
      - [Understanding Requirements](#understanding-requirements)
    - [19.2 Preparing the Kubernetes Setup](#192-preparing-the-kubernetes-setup)
    - [19.3 Writing a Playbook to Create a Kubernetes Cluster](#193-writing-a-playbook-to-create-a-kubernetes-cluster)
      - [Understanding Setup Tasks](#understanding-setup-tasks)
    - [19.4 Running the Playbook to Create a Kubernetes Cluster](#194-running-the-playbook-to-create-a-kubernetes-cluster)
    - [19.5 Managing Kubernetes Resources](#195-managing-kubernetes-resources)
      - [Managing Kubernetes Resources](#managing-kubernetes-resources)
    - [Lesson 19 Lab Automating Kubernetes Application Deployment with Ansible](#lesson-19-lab-automating-kubernetes-application-deployment-with-ansible)
    - [Lesson 19 Lab Solution Automating Kubernetes Application Deployment with Ansible queue](#lesson-19-lab-solution-automating-kubernetes-application-deployment-with-ansible-queue)

### 19.1 Understanding Requirements for Managing Kubernetes

#### Understanding Requirements

- Install Python-supporting modules: **pip3 install kubernetes; pip3 install openshift**
- Install the collection from Galaxy: **ansible-galaxy collection install kubernetes.core**
- Make sure a Kubernetes client is available on the Ansible Control node.
- It is recommended to use Ubuntu as the Kubernetes cluster node(s)
```bash
cd kubernetes
- Go through this doc SetupGuideAiO.pdf for more details.
```

### 19.2 Preparing the Kubernetes Setup

- Explain about k8s setup.

### 19.3 Writing a Playbook to Create a Kubernetes Cluster

#### Understanding Setup Tasks

- On the Ansible Controller.
  - Ensure the Python components are installed with pip.
  - After setting up the cluster, configure the kube client.
- On the cluster node.
  - Set up the container layer.
  - Install the Kubernetes tools.
  - Build the cluster.
- Once completed, verify using **kubectl get all** from the Ansible control node.
- **ansible-playbook kube-cluster-setup.yaml -e kubehost=kube-host-name** 
```bash
cd kubernetes
vim kube-cluster-setup.yaml
ansible-playbook kube-cluster-setup.yaml -e kubehost=kube-host-name
```
### 19.4 Running the Playbook to Create a Kubernetes Cluster

```bash
cd kubernetes
vim kube-cluster-setup.yaml
ansible-playbook kube-cluster-setup.yaml -e kubehost=kubuntu -K
kubectl get pods -A
```

### 19.5 Managing Kubernetes Resources

#### Managing Kubernetes Resources

- After setting up the cluster node(s), first create Kubernetes infrastructure components and next start running deployments and/or Pods.
- Use Ansible Collections to do so.
```bash
cd kubernetes
vim create-pod.yaml
ansible-playbook create-pod.yaml
kubectl get all
```

### Lesson 19 Lab Automating Kubernetes Application Deployment with Ansible

- Write a playbook to install a one-node Kubernetes cluster a and run it.
- Write a playbook to run a Pod that starts an Nginx application.

### Lesson 19 Lab Solution Automating Kubernetes Application Deployment with Ansible queue

```bash
cd kubernetes
ansible-doc k8s
vim create-new-pod.yaml
ansible-playbook create-new-pod.yaml
kubectl get all
kubectl get endpoints
ansible-doc -l | grep k8s
```
