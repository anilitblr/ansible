# Ansible

- [Ansible](#ansible)
- [Module 1: Getting Started](#module-1-getting-started)
    - [Lesson 1: Preparing your Managed Infrastructure](#lesson-1-preparing-your-managed-infrastructure)
    - [Lesson 2: Using Ad-hoc Commands](#lesson-2-using-ad-hoc-commands)
    - [Lesson 3: Using Ansible Playbook](#lesson-3-using-ansible-playbook)
    - [Lesson 4: Using Ansible Tower](#lesson-4-using-ansible-tower)
- [Module 2: Developing Flexible Playbooks](#module-2-developing-flexible-playbooks)
    - [Lesson 5: Working with Variables](#lesson-5-working-with-variables)
    - [Lesson 6: Using Conditionals](#lesson-6-using-conditionals)
    - [Lesson 7: Managing Files](#lesson-7-managing-files)
    - [Lesson 8: Using Roles and Collections](#lesson-8-using-roles-and-collections)
- [Module 3: Advanced Ansible Management](#module-3-advanced-ansible-management)
    - [Lesson 9: Ansible Best Practices and Optimization](#lesson-9-ansible-best-practices-and-optimization)
    - [Lesson 10: Using Filters](#lesson-10-using-filters)
    - [Lesson 11: Using Plugins](#lesson-11-using-plugins)
    - [Lesson 12: Advanced Ansible Tower Usage](#lesson-12-advanced-ansible-tower-usage)
- [Module 4: Managing Heterogeneous Environment with Ansible](#module-4-managing-heterogeneous-environment-with-ansible)
    - [Lesson 13: Managing Windows with Ansible](#lesson-13-managing-windows-with-ansible)
    - [Lesson 14: Managing Azure with Ansible](#lesson-14-managing-azure-with-ansible)
    - [Lesson 15: Managing Containers](#lesson-15-managing-containers)
    - [Lesson 16: Managing AWS with Ansible](#lesson-16-managing-aws-with-ansible)
    - [Lesson 17: Managing Network Devices with Ansible](#lesson-17-managing-network-devices-with-ansible)
    - [Lesson 18: Managing Virtual Machines with Ansible](#lesson-18-managing-virtual-machines-with-ansible)
    - [Lesson 19: Managing Kubernetes with Ansible](#lesson-19-managing-kubernetes-with-ansible)

# Module 1: Getting Started

### [Lesson 1: Preparing your Managed Infrastructure](lessons/Lesson-1-Preparing-your-Managed-Infrastructure.md)

- 1.1 Understanding Ansible
- 1.2 Setting up the Ansible Control Node
- 1.3 Understanding Requirements for Managing Assets with Ansible
- 1.4 Configuring Inventory
- 1.5 Understanding Ad-hoc Commands
- 1.6 Understanding the Course Lab Environment
- 1.7 Configuring Linux Managed Hosts with Ad-hoc Commands
- 1.8 Setting up Privilege Escalation
- 1.9 Understanding ansible.cfg and Working with Settings
- 1.10 Setting up Windows as a Managed Host
- Lesson 1 Lab Setting up an Ansible Managed Environment
- Lesson 1 Lab Solution Setting up an Ansible Managed Environment

### [Lesson 2: Using Ad-hoc Commands](lessons/Lesson-2-Using-Ad-hoc-Commands.md)

- 2.1 Ad-hoc Commands versus Playbooks
- 2.2 Exploring Essential Ansible Modules
- 2.3 Using Module Documentation
- 2.4 Using Ansible in an Idempotent way
- Lesson 2 Lab Using Ad-hoc Commands
- Lesson 2 Lab Solution Using Ad-hoc Commands

### [Lesson 3: Using Ansible Playbook](lessons/Lesson-3-Using-Ansible-Playbook.md)

- 3.1 Understanding Playbook Structure
- 3.2 Writing and Running your First Playbook
- 3.3 Understanding Task Execution and Errors
- Lesson 3 Lab Using a Playbook to Automate Web Server Setup
- Lesson 3 Lab Solution Using a Playbook to Automate Web Server Setup

### [Lesson 4: Using Ansible Tower](lessons/Lesson-4-Using-Ansible-Tower.md)

- 4.1 Understanding Ansible Tower
- Automation Platform and AWX
- 4.2 Installing Ansible Tower
- 4.3 Understanding Ansible Tower Main Components
- 4.4 Setting up Ansible Tower to Manage Assets
- 4.5 Configuring Ansible Tower to Manage Windows
- Lesson 4 Lab Setting up Ansible Tower to Manage Assets in Ansible
- Lesson 4 Lab Solution Setting up Ansible Tower to Manage Assets in Ansible

# Module 2: Developing Flexible Playbooks

### [Lesson 5: Working with Variables](lessons/Lesson-5-Working-with-Variables.md)

- 5.1 Separating Code from Site-Specific Configuration
- 5.2 Using Variables in a Playbook
- 5.3 Understanding Where to Define your Variables
- 5.4 Using Ansible Facts
- 5.5 Understanding Different Notations for Facts and Variables
- 5.6 Speeding up Fact Collection
- 5.7 Using Multi-valued Variables
- 5.8 Using Magic Variables
- 5.9 Using Register
- 5.10 Using Vault to Store Sensitive Information
- Lesson 5 Lab Making Playbooks Flexible with Variables
- Lesson 5 Lab Solution Making Playbooks Flexible with Variables

### [Lesson 6: Using Conditionals](lessons/Lesson-6-Using-Conditionals.md)

- 6.1 Conditionals Overview
- 6.2 Using Handlers for Conditional Task Execution
- 6.3 Using when to Run Tasks Based on Specific Conditions
- 6.4 Using register to Work with Task Results
- 6.5 Using Blocks
- 6.6 Using loop to Process a List of Items
- 6.7 Managing Failure with the fail Module
- 6.8 Using the assert Module
- Lesson 6 Lab Using when to Make the command Module Idempotent
- Lesson 6 Lab Solution Using when to Make the command Module Idempotent

### [Lesson 7: Managing Files](lessons/Lesson-7-Managing-Files.md)

- 7.1 Manipulating Files
- 7.2 Changing File Contents
- 7.3 Using the find Module
- 7.4 Using Templates
- Lesson 7 Lab Working with Files
- Lesson 7 Lab Solution Working with Files

### [Lesson 8: Using Roles and Collections](lessons/Lesson-8-Using-Roles-and-Collections.md)

- 8.1 Understanding Collections
- 8.2 Understanding Roles
- 8.3 Working with Galaxy
- 8.4 Using Collections
- 8.5 Using Collections from Automation Hub
- 8.6 Creating your own Roles
- Lesson 8 Lab Working with Roles and Collections
- Lesson 8 Lab Solution Working with Roles and Collections

# Module 3: Advanced Ansible Management

### [Lesson 9: Ansible Best Practices and Optimization](lessons/Lesson-9-Ansible-Best-Practices-and-Optimization.md)

- 9.1 Using Includes and Imports
- 9.2 Configuring Security
- 9.3 Using Tags
- 9.4 Using Delegation
- 9.5 Managing Parallelism
- 9.6 Efficiently Copying Files
- 9.7 Optimizing SSH
- 9.8 Case Study: Optimizing Ansible
- Lesson 9 Lab Optimizing Ansible
- Lesson 9 Lab Solution Optimizing Ansible

### [Lesson 10: Using Filters](lessons/Lesson-10-Using-Filters.md)

- 10.1 Understanding Filters and Variable Types
- 10.2 Using Filters to Change Variables
- 10.3 Using Filters to Work with Network Addresses
- 10.4 Using Filters in Loops
- Lesson 10 Lab Using Filters
- Lesson 10 Lab Solution Using Filters

### [Lesson 11: Using Plugins](lessons/Lesson-11-Using-Plugins.md)

- 11.1 Understanding Plugins and Filters
- 11.2 Exploring Lookup Plugins
- 11.3 Using Common Lookup Plugins
- 11.4 Using the fileglob Lookup Plugin
- 11.5 Using Callback and Timer Plugins
- 11.6 Using Plugin-Based Inventory
- 11.7 Configuring Fact Caching
- 11.8 Creating Random Passwords
- Lesson 11 Lab Configuring Fact Caching
- Lesson 11 Lab Solution Configuring Fact Caching

### [Lesson 12: Advanced Ansible Tower Usage](lessons/Lesson-12-Advanced-Ansible-Tower-Usage.md)

- 12.1 Managing Users and Teams
- 12.2 Creating Job Template Surveys
- 12.3 Configuring Notifications
- 12.4 Using Workflow
- 12.5 Scheduling Jobs
- 12.6 Importing Static Inventories
- 12.7 Creating and Updating Dynamic Inventories
- 12.8 Using Smart Inventories
- 12.9 Using Vault in Tower
- 12.10 Using the Tower API
- 12.11 Backing up Tower
- Lesson 12 Lab Advanced Ansible Tower Usage
- Lesson 12 Lab Solution Advanced Ansible Tower Usage

# Module 4: Managing Heterogeneous Environment with Ansible

### [Lesson 13: Managing Windows with Ansible](lessons/Lesson-13-Managing-Windows-with-Ansible.md)

- 13.1 Understanding Requirements for Managing Windows
- 13.2 Using Playbooks to Manage Windows
- Lesson 13 Lab Managing Windows with Ansible
- Lesson 13 Lab Solution Managing Windows with Ansible

### [Lesson 14: Managing Azure with Ansible](lessons/Lesson-14-Managing-Azure-with-Ansible.md)

- 14.1 Understanding Requirements for Managing Azure
- 14.2 Using Playbooks to Manage Azure
- Lesson 14 Lab Managing Azure
- Lesson 14 Lab Solution Managing Azure

### [Lesson 15: Managing Containers](lessons/Lesson-15-Managing-Containers.md)

- 15.1 Understanding Requirements for Managing Docker
- 15.2 Using Playbooks to Manage Docker
- 15.3 Managing Podman Containers
- Lesson 15 Lab Managing Containers
- Lesson 15 Lab Solution Managing Containers

### [Lesson 16: Managing AWS with Ansible](lessons/Lesson-16-Managing-AWS-with-Ansible.md)

- 16.1 Understanding Requirements for Managing AWS
- 16.2 Using Playbooks to Manage AWS
- 16.3 Configuring Dynamic Inventory
- Lesson 16 Lab Managing AWS with Ansible
- Lesson 16 Lab Solution Managing AWS with Ansible

### [Lesson 17: Managing Network Devices with Ansible](lessons/Lesson-17-Managing-Network-Devices-with-Ansible.md)

- 17.1 Understanding Network Device Management
- 17.2 Setting Up Cisco SMB Devices
- 17.3 Configuring Cisco SMB Devices with Ansible
- 17.4 Using Generic Modules for Network Device Management
- Lesson 17 Lab Automating Switch Setup with Ansible
- Lesson 17 Lab Solution Automating Switch Setup with Ansible

### [Lesson 18: Managing Virtual Machines with Ansible](lessons/Lesson-18-Managing-Virtual-Machines-with-Ansible.md)

- 18.1 Managing KVM Virtual machines
- 18.2 Understanding vSphere Management
- 18.3 Managing ESXi
- Lesson 18 Lab Managing a KVM Based Virtual Classroom with Ansible
- Lesson 18 Lab Solution Managing a KVM Based Virtual Classroom with Ansible

### [Lesson 19: Managing Kubernetes with Ansible](lessons/Lesson-19-Managing-Kubernetes-with-Ansible.md)

- 19.1 Understanding Requirements for Managing Kubernetes
- 19.2 Preparing the Kubernetes Setup
- 19.3 Writing a Playbook to Create a Kubernetes Cluster
- 19.4 Running the Playbook to Create a Kubernetes Cluster
- 19.5 Managing Kubernetes Resources
- Lesson 19 Lab Automating Kubernetes Application Deployment with Ansible
- Lesson 19 Lab Solution Automating Kubernetes Application Deployment with Ansible queue
