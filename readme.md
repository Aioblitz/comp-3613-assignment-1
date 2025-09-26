## CLI Usage Guide
The general flow of what needs to be done are listed below for the 4 main features needed. Each command prompts the users to look at the terminal and provide input accordingly.

#### Create a New Job Posting

Lists all employers, prompts for your employer ID, job title, and description, then creates the job.

```shell
flask employer create
```
sample input for testing based on freshly initialised db

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

---

#### Change Application Status

Lists all jobs, prompts for a job ID, then lists applications for that job. Prompts for a student ID and new status (`accepted` or `rejected`).

```shell
flask employer change-status
```

---

#### List Shortlisted Positions

Lists all students, prompts for your student ID, then displays jobs you are shortlisted for.

```shell
flask student list
```

---
### Misc Commands
#### List All Users

Lists all users in the database, showing their correct type (Student, Staff, Employer).

```shell
flask user list
```

#### List All Jobs

Lists all jobs in the database, showing job details and employer organization name.

```shell
flask user list-jobs
```

---
# Flask Commands

