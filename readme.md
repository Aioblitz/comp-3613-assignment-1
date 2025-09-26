## CLI Usage Guide


### General Format

```shell
flask <group> <command> [arguments]
```

---

### Student Commands

#### List Shortlisted Positions

Lists all students, prompts for your student ID, then displays jobs you are shortlisted for.

```shell
flask student list
```

---

### Staff Commands

#### Shortlist a Student for a Job

Lists all jobs, prompts for a job ID, then lists students not yet shortlisted for that job. Prompts for a student ID to shortlist.

```shell
flask staff shortlist
```

---

### Employer Commands

#### Change Application Status

Lists all jobs, prompts for a job ID, then lists applications for that job. Prompts for a student ID and new status (`accepted` or `rejected`).

```shell
flask employer change-status
```

#### Create a New Job Posting

Lists all employers, prompts for your employer ID, job title, and description, then creates the job.

```shell
flask employer create
```

---

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

