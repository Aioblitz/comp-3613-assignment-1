## CLI Usage Guide
The general flow of what needs to be done are listed below for the 4 main features needed. Each command prompts the users to look at the terminal and provide input accordingly.

#### Create a New Job Posting

Lists all employers, prompts for your employer ID, job title, and description, then creates the job.

```shell
flask employer create
```
Sample input for testing based on freshly initialised db.

 ```shell
5
CSR
Customer Sales Representative
```
---

#### Shortlist a Student for a Job

Lists all jobs, prompts for a job ID, then lists students not yet shortlisted for that job. Prompts for a student ID to shortlist.

```shell
flask staff shortlist
```

Sample input for testing based on following the previous step.

 ```shell
1 or 2
2 or 3
```

---

#### Change Application Status

Lists all jobs, prompts for a job ID, then lists applications for that job. Prompts for a student ID and new status (`accepted` or `rejected`).

```shell
flask employer change-status
```

Sample input for testing based on following the previous step.

 ```shell
1 or 2
2 
accepted
```

---

#### List Shortlisted Positions

Lists all students, prompts for your student ID, then displays jobs you are shortlisted for.

```shell
flask student list
```

Sample input for testing based on following the previous step.

 ```shell
2 or 3
```

---
### Misc Commands

#### Edit Jobs 

Edits the title and description of a given job to user specified values

```shell
flask employer edit
```

#### List All Users

Lists all users in the database, showing their correct type (Student, Staff, Employer).

```shell
flask user list-users
```

#### List All Jobs

Lists all jobs in the database, showing job details and employer organization name.

```shell
flask user list-jobs
```
