# Lesson 12 - Advanced Ansible Tower Usage

- [Lesson 12 - Advanced Ansible Tower Usage](#lesson-12---advanced-ansible-tower-usage)
    - [12.1 Managing Users and Teams](#121-managing-users-and-teams)
      - [Understanding Tower Users](#understanding-tower-users)
      - [Understanding Organizations](#understanding-organizations)
      - [Understanding User Types](#understanding-user-types)
      - [Understanding Teams](#understanding-teams)
      - [Organization Roles](#organization-roles)
      - [CREATE USER](#create-user)
      - [CREATE Teams](#create-teams)
      - [Assign user to group](#assign-user-to-group)
      - [Assign permissions to group](#assign-permissions-to-group)
      - [CREATE Organizations](#create-organizations)
    - [12.2 Creating Job Template Surveys](#122-creating-job-template-surveys)
      - [Understanding Job Templates](#understanding-job-templates)
      - [Defining Survey Answer Types](#defining-survey-answer-types)
      - [Creating Surveys](#creating-surveys)
      - [Create Survey](#create-survey)
      - [Test survey](#test-survey)
    - [12.3 Configuring Notifications](#123-configuring-notifications)
      - [create notification](#create-notification)
      - [Enable notification for template](#enable-notification-for-template)
    - [12.4 Using Workflow](#124-using-workflow)
      - [Understanding Workflow](#understanding-workflow)
      - [Create Job1](#create-job1)
      - [Create Job2](#create-job2)
      - [CREATE WORKFLOW](#create-workflow)
    - [12.5 Scheduling Jobs](#125-scheduling-jobs)
      - [Understanding Scheduled Jobs](#understanding-scheduled-jobs)
      - [Create Schedules](#create-schedules)
    - [12.6 Importing Static Inventories](#126-importing-static-inventories)
    - [12.7 Creating and Updating Dynamic Inventories](#127-creating-and-updating-dynamic-inventories)
      - [Dynamic Inventory and Tower](#dynamic-inventory-and-tower)
      - [Create credentails](#create-credentails)
    - [12.8 Using Smart Inventories](#128-using-smart-inventories)
      - [Understanding Smart Inventory](#understanding-smart-inventory)
      - [Understanding Smart Inventory Filters](#understanding-smart-inventory-filters)
    - [12.9 Using Vault in Tower](#129-using-vault-in-tower)
      - [Tower and Vault](#tower-and-vault)
    - [12.10 Using the Tower API](#1210-using-the-tower-api)
      - [Understanding Tower API](#understanding-tower-api)
      - [Understanding Tower API](#understanding-tower-api-1)
      - [Demo: Launching Job Templates Using API](#demo-launching-job-templates-using-api)
      - [Using the API to Lauch Jobs from a playbook](#using-the-api-to-lauch-jobs-from-a-playbook)
    - [12.11 Backing up Tower](#1211-backing-up-tower)
    - [Lesson 12 Lab Advanced Ansible Tower Usage](#lesson-12-lab-advanced-ansible-tower-usage)
    - [Lesson 12 Lab Solution Advanced Ansible Tower Usage](#lesson-12-lab-solution-advanced-ansible-tower-usage)
      - [Create Job1](#create-job1-1)
      - [Create Job2](#create-job2-1)
      - [Create Job3](#create-job3)
      - [CREATE WORKFLOW](#create-workflow-1)

### 12.1 Managing Users and Teams

#### Understanding Tower Users

- Tower users are used by people that need access to the Tower interface.
- Tower users are used with Role Based Access Control (RBAC) to grant users access to specific roles.
- Roles can be assinged to individual users or teams.
- Depending on the RBAC settings granted to an Ansible user, the user will be able to view, use, change or remove Ansible objects.

#### Understanding Organizations

- An organization is a collection of teams, projects and inventories.
- Organizations make sense in very large deployments, as the allow users and teams to be configured with access to specific sets of reslurces.
- Ansible Tower comes with one organization, named Default.
- According to the Ansible Tower usage license, additional organizations may be created.
- Users exist at the Ansible Tower level and can have roles in multiple organizations.

#### Understanding User Types

- Be default, there are three types of usres.
  - System Administrator had read/write access to the entire Tower installation.
  - System Auditor had read-only access to the entire installation.
  - Normal user starts with minimal access, and must be provided with access by adding roles to the user.

#### Understanding Teams

- A team is a group of users.
- Teams exist at an organization level.
- System Administrator users can assign the team roles on resources in different organizations.
- Teams cannot get roles on the organization object.

#### Organization Roles

- Differrent roles are available and can be connected to the users.
  - Organization Admin.
  - Project Admin.
  - Inventory Admin.
  - Credential Admin.
  - Notification Admin.
  - Workflow Admin.
  - Job Template Admin.
  - Auditor.
  - Member.
  - Read.
  - Execute.
- Roles are assigned with an organization scope or a project scope.

#### CREATE USER

- Navigate to TOWER Dashboard.
  - Choose **ACCESS** -> **Users**
  - Choose **Plus**
  - Fill the details
  - USER TYPE: **Normal User**
  - Choose **SAVE**
  - Repeat it, to crete more users.

#### CREATE Teams

- Navigate to TOWER Dashboard.
  - Choose **ACCESS** -> **Teams**
  - Choose **Plus**
  - NAME: **normalusers**
  - Choose **SAVE**
  - Repeat it, to crete more teams.

#### Assign user to group

- Navigate to TOWER Dashboard.
  - Choose **ACCESS** -> **Teams**
  - Choose **Edit team** icon for **normalusres** group
  - Choose **USERS**
  - Choose **Plus**
  - Choose user name.
  - Choose **SAVE**
  - Repeat it, to add more users to the team.

#### Assign permissions to group

- Navigate to TOWER Dashboard.
  - Choose **ACCESS** -> **Teams**
  - Choose **Edit team** icon for **normalusres** group
  - Choose **PERMISSIONS**
  - Choose **Plus**
  - Choose Job name and again choose the same job name under NAME.
  - Choose **PERMISSIONS**
  - Choose **Plus**
  - Choose **TEAMS**
  - Select the team name **normalusers**.
  - normalusers: Choose **Execute**
  - Choose **SAVE**
  - Logout and login with the new user.
  - Repeat it, to assign permissions for more teams.

#### CREATE Organizations

- Navigate to TOWER Dashboard.
  - Choose **ACCESS** -> **Organizations**
  - Choose **Plus**
  - NAME: **myorg**
  - Choose **SAVE**
  - Repeat it, to crete more organizations.

### 12.2 Creating Job Template Surveys

#### Understanding Job Templates

- **vars_prompt** from Ansible Engine is not supported in Tower.
- An alternative is provided by Job Template surveys.
- On a job, use **EXTRA VARIABLES** to define variables on the job.
- Select **PROMPT ON LAUNCH** to prompt for variable values while launching the Job Template.
- These options make sense for a skilled Ansible user.
- To make it easy for anyone to provide variables, a Job Template Survey can be used.
- Job Template Surveys prompt for variables when the job is started.
- Variables from a survey have the highest priority.

#### Defining Survey Answer Types

- In surveys, the variable types can be defined as one of the following.
  - Text: this is text on a single line.
  - Textarea: text on multiple lines.
  - Password: treated as sensitive information.
  - Multiple choice (single select): a list of options where one can be selected.
  - Multiple choice (multiple select): a list of options where one or more can be selected.
  - Integer: an integer number.
  - Float: a floating-point decimal.
- While creating surveys, a default answer can be specified.
- Questions can also be marked as required: an answer must be provided.

#### Creating Surveys

- A survey cannot be created during creation of the template.
- Create the Job Template first, save it, and next add the Survey to it.

#### Create Survey

- Navigate to TOWER Dashboard.
  - Choose **RESOURCES** -> **Templates**
  - Choose **my-template**
  - Choose **ADD SURVEY**
    - PROMPT: **Which username**
    - DESCRIPTION: **Enter the name of the user you want to create**
    - ANSWER VARIABLE NAME: **username**
    - ANSWER TYPE: **Text**
      - MINIMUM LENGTH: **2**
      - MAXIMUM LENGTH: **1024**
    - Choose **ADD**
  - Choose **SAVE**
  - Repeat it, to add more surveys.

#### Test survey

- Navigate to TOWER Dashboard.
  - Choose **RESOURCES** -> **Templates**
  - Click on **Start a job using this tempalte** icon for **my-template**
  - Survey will pops up.
  - WHICH USERNAME: **anil**
  - Choose **NEXT**
  - Choose **LAUNCH**

### 12.3 Configuring Notifications

#### create notification

- Navigate to TOWER Dashboard.
  - Choose **ADMINISTRATION** -> **Notifications**
  - Choose **Plus**
  - NEW NOTIFICATION TEMPLATE
    - NAME: **Enter some good name**
    - ORGANIZATION: Choose **Default** and choose **SAVE**
    - TYPE: Email
    - Choose **SAVE**

#### Enable notification for template

- Navigate to TOWER Dashboard.
  - Choose **RESOURCES** -> **Templates**
  - Choose **my-template**
  - Choose **NOTIFICATIONS**
  - Click under **FAILURE**
  - Choose **my-template**
  - Choose **SAVE**

### 12.4 Using Workflow

#### Understanding Workflow

- A Workflow Job Template is used to run multiple Job Templates in a sequence.
- Using Workflows makes it easier to work with playbooks (Job Templates) that are provided from different teams.
- In a Workflow, complex relations between jobs can be defined. In these relations, the next job is started depending on the result of the previous job.
  - On success
  - On failure
  - Always
- Before creating a Workflow, a Workflow Job Template has to be defined.
- After defining the Workflow Job Template, the Workflow Visualizer is used to define the actual workflow.

#### Create Job1
- Navigate to TOWER Dashboard.
  - Choose **RESOURCES** -> **Templates**
  - Choose **Plus** icon
  - Choose **Job Template**
    - NAME: **creatingsomething**
    - JOB TYPE: **Run**
    - INVENTORY: **my-inventory**
      - Choose **SELECT**
    - PROJECT: **my-project**
      - Choose **SELECT**
    - PLAYBOOK: Choose **installsomething.yml**
    - CREDENTIALS: **my-credentials**
      - Choose **SELECT** 
    - Choose **SAVE**
    - Choose **LAUNCH**

#### Create Job2
- Navigate to TOWER Dashboard.
  - Choose **RESOURCES** -> **Templates**
  - Choose **Plus** icon
  - Choose **Job Template**
    - NAME: **removesomething**
    - JOB TYPE: **Run**
    - INVENTORY: **my-inventory**
      - Choose **SELECT**
    - PROJECT: **my-project**
      - Choose **SELECT**
    - PLAYBOOK: Choose **removesomething.yml**
    - CREDENTIALS: **my-credentials**
      - Choose **SELECT** 
    - Choose **SAVE**
    - Choose **LAUNCH**

#### CREATE WORKFLOW

- Navigate to TOWER Dashboard.
  - Choose **RESOURCES** -> **Templates**
  - Choose **Plus** icon
  - Choose **Workflow Template**
  - NAME: **myworkflow**
  - Choose **SAVE**
  - WORKFLOW VISUALIZER
    - Choose **START**
    - Choose **createsomething**
    - RUN: **Always**
    - Choose **SELECT**
    - Choose **Plus** in the visualizer which added **createsomething**
    - Choose **removesomething**
    - RUN: **On Success**
    - Choose **SELECT**
    - Choose **SAVE**
    - **ADD SURVEY**
      - PROMPT: **What do you want to install**
      - DESCRIPTION: **Enter the name of the package as it is known in the repositories**
      - ANSWER VARIABLE NAME: **something**
      - ANSWER TYPE: **Text**
        - MINIMUM LENGTH: **2**
        - MAXIMUM LENGTH: **1024**
      - Choose **ADD**
    - Choose **SAVE**
    - **PERMISSIONS**
      - You can add permissions.
    - **NOTIFICATIONS**
      - You can add notifications.
    - Go back to workflow 
    - Choose **SAVE**
    - Choose **LAUNCH**

### 12.5 Scheduling Jobs

#### Understanding Scheduled Jobs

- Scheduled Jobs allow you to run Job Templates o a cron-like schedule.
- After Job execution, results can be consulted in completed Jobs.
- Also, notification templates can be configured to send information about Job success or failure in an automated way.
- To use notifications, you will first create the notification template and then add it to a Job Template for execution.

#### Create Schedules

- Navigate to TOWER Dashboard.
  - Choose **RESOURCES** -> **Templates**
  - Choose **my-template**
  - Choose **SCHEDULES**
    - Choose **Plus**
    - Fill the details.
    - Choose **SAVE**
  - Choose **DETAILS**
    - Choose **SAVE**

### 12.6 Importing Static Inventories

- Static inventories can easily be imported if they are in Git or any other external system.
- Local static inventory files are imported with the **aws-manage** cli utility on the Tower server.
  - awx-manage inventory_import --source=/root/my-inventory --inventory-name="myinventory"

- **Projects** 
  - Choose **Plus** icon
  - NAME: my-project
  - ORGANIZATION: **Default**
  - SCM TYPE: Git
    - SCM URL: https://github.com/anilitblr/tower
  - SCM UPDATE OPTIONS: **UPDATE REVISION ON LAUNCH**
    - Choose **SAVE**
- **Inventories** 
  - DETAILS 
    - click on **Plus**
    - Choose **inventory**
    - NAME: **newinventory**
  - ORGANIZATION: **Default**
  - SOURCES  
    - Click on **Plus**
    - NAME: **fromproject**
    - SOURCE: **Source from a Project**
    - PROJECT: **my-project**
    - INVENTORY FILE: **inventory**
    - UPDATE OPTIONS: **UPDATE ON PROJECT UPDATE**
    - Scroll down and choose **HOSTS** above **fromproject** under **SOURCES**
    - Click **SAVE**
  - Update inventory file
    - Update the inventory file and push it to the GitHub.
    - Go to **HOSTS** in **newinventory** to see the updated hosts.
    - Go to **GROUPS** in **newinventory** to see the updated groups.

### 12.7 Creating and Updating Dynamic Inventories

#### Dynamic Inventory and Tower

- Tower comes with a set of dynamic inventories to connect to common external environments like AWS, Azure, OpenStack and more.
- Custom inventory scripts can also be used.

#### Create credentails

- Navigate to TOWER Dashboard.
  - Choose **RESOURCES** -> **Credentails**
  - Choose **Plus** icon
  - **DETAILS**
    - NAME: azure
    - ORGANIZATION: Default
    - Choose pagination number **3** and select **Microsoft Azure Resource Manager**
    - Choose **SELECT**
    - **TYPE DETAILS**
      - SUBSCRIPTION ID: **xxxxxxxxxx**
      - CLIENT ID: **xxxxxxxxxx**
      - CLIENT SECRET: **xxxxxxxxxx**
      - TENANT: **xxxxxxxxxx**
      - Choose **SAVE**
  - **Inventories** 
    - **DETAILS**
      - Choose **SAVE** 
        - click on **Plus**
        - Choose **inventory**
        - NAME: **azure-inventory**
        - ORGANIZATION: **Default**
        - Choose **SAVE**
      - **SOURCES**
        - click on **Plus**
        - NAME: **myazure**
        - SOURCE: **Microsoft Azure Resource Manager**
        - CREDENTIAL: **azure**
        - Choose **SAVE**
  - **Inventroy Scripts**
    - click on **Plus**
    - NAME: **ldap-ipa**
    - ORGANIZATION: **Default**
    - CUSTOM SCRIPT: Copy code from this file `ldap-freeipa/ldap-freeipa.py` and paste it here.
    - Choose **SAVE**

### 12.8 Using Smart Inventories

#### Understanding Smart Inventory

- Smart inventory is dynamically created from other inventory sources by using a filter.
- The filter is using Ansible facts that are discovered from the different hosts.
- Smart inventory uses fact cache, so you will have to create a Job Template with the "use fact cache" option and run it periodically.

#### Understanding Smart Inventory Filters

- A filter may look like **ansible_facts.ansible_distribution:RedHat**
- In this filter, pre Ansible 2.5 notation is used (modren notation is not yet supported)
- **ansible_facts** indicates the filter applies to Ansible facts, and not a host name or something else.
- Also notice there is no white space between the colon and the value you want to match.

- Navigate to TOWER Dashboard.
  - Choose **RESOURCES** -> **Templates**
    - Choose **Plus** icon
    - Choose **Job Template**
      - NAME: **creatingsomething**
      - JOB TYPE: **Run**
      - INVENTORY: **my-inventory**
        - Choose **SELECT**
      - PROJECT: **my-project**
        - Choose **SELECT**
      - PLAYBOOK: Choose **factcache.yml**
      - CREDENTIALS: **my-credentials**
        - Choose **SELECT** 
      - OPTIONS: **ENABLE FACT CACHE**
      - Choose **SAVE**
      - Choose **LAUNCH**
  - Choose **RESOURCES** -> **Inventories**
    - **DETAILS**
      - Choose **SAVE** 
        - click on **Plus**
        - Choose **smart inventory**
        - NAME: **smart**
        - ORGANIZATION: **Default**
        - SMART HOST FILTER:
          - Click on **search icon**
          - Type following text in SEARCH box: **ansible_facts.ansible_distribution:Rocky**
          - Click on **search icon**
          - Choose **SAVE**
        - Choose **SAVE**

### 12.9 Using Vault in Tower

#### Tower and Vault

- To use Vault-encrypted files, you need to create a vault credentails.
- Job Tempalte must be configured with both the vault credentail and the machine credentail to run the job.

- Navigate to TOWER Dashboard.
  - Choose **RESOURCES** -> **Credentails**
    - DETAILS
      - NAME: **vault**
      - ORGANIZATION: **Default**
      - CREDENTIAL TYPE: Vault 
        - Choose **SELECT**
        - VAULT PASSWORD: **PASSWORD-GOES-HERE**
        - Choose **SAVE**
  - Choose **RESOURCES** -> **Templates**
    - Choose **Plus** icon
    - Choose **Job Template**
      - NAME: **vaulted**
      - JOB TYPE: **Run**
      - INVENTORY: **my-inventory**
        - Choose **SELECT**
      - PROJECT: **my-project**
        - Choose **SELECT**
      - PLAYBOOK: Choose **vaulted.yml**
      - CREDENTIALS: **my-credentials**
        - Choose **SELECT** 
      - CREDENTIALS: **my-credentials**
        - CREDENTIALS TYPE: Choose **Vault**
        - Choose **SELECT** 
      - Choose **SAVE**
      - Choose **LAUNCH**

### 12.10 Using the Tower API

#### Understanding Tower API

- Tower provides a REST API that allows controlling Tower from playbooks.
- This allows clients to perform actions using standard HTTP methods, such as GET, POST, PUT and DELETE
  - **curl -X GET https://tower.example.com/api/ -k**
- The API is browsabe, which means you can access it from a graphical browser and investigate the different elements by clicking on them.
  - https://tower.example.com/api/
- When using **curl**, pipe through **json_pp** for readable ("pretty print") output.
  - **sudo dnf install -y perl-JSON-PP**
  - **curl -X GET https://tower.example.com/api/v2 -ks | json_pp**

#### Understanding Tower API

- Some information requires proper authentication.
  - **curl -X GET https://tower.example.com/api/v2/activity_stream/ -k**
  - **curl -X GET --user admin:password https://tower.example.com/api/v2/activity_stream/ -k**
- When using a graphical browser, use the question mark icon to get more information about resources.

#### Demo: Launching Job Templates Using API

- Start by getting information about Jobs.
  - **curl -X GET --user admin:password https://tower.example.com/api/v2/job_templates/ -ks | json_pp | grep name**
- Use POST and launch to launch any Job.
  - **curl -X POST --user admin:password https://tower.example.com/api/v2/job_templates/"updatecache"/lauch/ -ks | json_pp**
  - In the output, look for the job ID.
- Use the Job ID to get a Job status update.
  - **curl -X GET --user admin:password https://tower.example.com/api/v2/jobs/25/ -ks | json_pp**

#### Using the API to Lauch Jobs from a playbook

- The **uri** can be used to run a Job using the API.
- See **launchtowerjob.yaml** in the **tower** directory.

### 12.11 Backing up Tower

```bash
cd <ansible-tower-inst-dir>
sudo ./setup.sh -b
```

### Lesson 12 Lab Advanced Ansible Tower Usage

- Create a Job Template Workflow that meets the following requirements.
  - The primary job to be used creates a user with a password.
  - Configure a variables prompt, whre the user needs to input username as well as password.
  - It is allowed but not required to use a properly encrypted password.
  - If the job executes successfully, another job should run that creates the directory /${USER}/files and sets the user you created as owner to that directory.
  - If the job fails to execute, a dedicated job should run that prints the message "failed to create user"

### Lesson 12 Lab Solution Advanced Ansible Tower Usage

```bash
vim createuser.yaml
vim createdir.yaml
vim failing.yaml
# Push above file to the GitHub.
```

#### Create Job1
- Navigate to TOWER Dashboard.
  - Choose **RESOURCES** -> **Templates**
    - Choose **Plus** icon
    - Choose **Job Template**
      - NAME: **createuser**
      - JOB TYPE: **Run**
      - INVENTORY: **my-inventory**
        - Choose **SELECT**
      - PROJECT: **my-project**
        - Choose **SELECT**
      - PLAYBOOK: Choose **createuser.yml**
      - CREDENTIALS: **my-credentials**
        - Choose **SELECT** 
      - OPTIONS: **ENABLE PRIVILEGE ESCALATION**
      - Choose **SAVE**

#### Create Job2
- Navigate to TOWER Dashboard.
  - Choose **RESOURCES** -> **Templates**
    - Choose **Plus** icon
    - Choose **Job Template**
      - NAME: **createdir**
      - JOB TYPE: **Run**
      - INVENTORY: **my-inventory**
        - Choose **SELECT**
      - PROJECT: **my-project**
        - Choose **SELECT**
      - PLAYBOOK: Choose **createdir.yml**
      - CREDENTIALS: **my-credentials**
        - Choose **SELECT** 
      - OPTIONS: **ENABLE PRIVILEGE ESCALATION**
      - Choose **SAVE**

#### Create Job3
- Navigate to TOWER Dashboard.
  - Choose **RESOURCES** -> **Templates**
    - Choose **Plus** icon
    - Choose **Job Template**
      - NAME: **failing**
      - JOB TYPE: **Run**
      - INVENTORY: **my-inventory**
        - Choose **SELECT**
      - PROJECT: **my-project**
        - Choose **SELECT**
      - PLAYBOOK: Choose **failing.yml**
      - CREDENTIALS: **my-credentials**
      - Choose **SAVE**

#### CREATE WORKFLOW

- Navigate to TOWER Dashboard.
  - Choose **RESOURCES** -> **Templates**
  - Choose **Plus** icon
  - Choose **Workflow Template**
  - NAME: **lab12**
  - ORGANIZATION: **Default**
  - INVENTORY: **my-inventory**
  - Choose **SAVE**
  - WORKFLOW VISUALIZER
    - Choose **START**
    - Choose **createuser**
    - RUN: **Always**
    - Choose **SELECT**
    - Choose **Plus** in the visualizer which added **createuser**
    - Choose **createdir**
    - RUN: **On Success**
    - Choose **SELECT**
    - Choose **SAVE**
    - Choose **Plus** in the visualizer which added **createdir**
    - Choose **failing**
    - RUN: **On Failure**
    - Choose **SELECT**
    - Choose **SAVE**
    - **ADD SURVEY**
      - PROMPT: **Enter username**
      - DESCRIPTION: **Enter the name of the username**
      - ANSWER VARIABLE NAME: **username**
      - ANSWER TYPE: **Text**
        - MINIMUM LENGTH: **2**
        - MAXIMUM LENGTH: **1024**
      - Choose **ADD**
      - PROMPT: **Enter password**
      - DESCRIPTION: **Enter password**
      - ANSWER VARIABLE NAME: **password**
      - ANSWER TYPE: **Text**
        - MINIMUM LENGTH: **2**
        - MAXIMUM LENGTH: **1024**
      - Choose **ADD**
    - Choose **SAVE**
    - Choose **SAVE**
    - Choose **LAUNCH**
    - ENTER USERNAME: **anil**
    - ENTER PASSWORD: **password**
    - Choose **NEXT**
