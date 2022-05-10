# Github

<style> /* For setting up draft tags */
r { color: Red } /* For corrections and changes */
o { color: Orange } /* Incomplete or need to update */
g { color: Green } /* General highlight 1*/
b { color: LightBlue } /* General highlight 2*/
</style>

**Content Overview**

1. Basics of Git

2. Setting up Git locally

3. Basics of GitHub

4. Setting up GitHub

5. Working with Repositories

<br>

---

<br>

## **What is Git?**

- Popular source control system
- Distributed System
- Free and Open Source

<br>

## **Why use Git?**

- It is fast
- Disconnected
- Branching
- Pull requests

<br>

**Centralized System**

1. In a Centralized source management system we have the centralized copy of the source code on the server.
2. It is the main repository and contains all versions of the code.
3. When we want to make changes to the code we will first copy the code from server.
4. This gets current version of the code down and you get the local copy of that code.
5. I can make changes to the code and when I commit, it would update the changes to the central repository.
6. All the other developers can then pull down this change and they will have the updated code as well.

   > In Centalized system we work with changesets. It is the number of changes that is treated as a whole.

<br>

**Distributed System**

1. A developer will clone the entire repository, and will get the entire history on their local machine.
2. This does not require a central store. Typically there will always be one like Github.
3. In this scenario we can work offline as each developer has a copy including history.
4. We can create local branches and only when we are ready we can send it to central repository from where it is ready to be distributed again.
   > Process of sending code back to repository is called pushing.
5. Other developers can pull those changes on their own machines.
   > This process is called pulling.
6. Pushing and Pulling requires to be connected however all other operations can be done in a disconnected way.

<br>

**3 Stages of Git**

There are 3 states in which a file can be in:

1. Commited
2. Modified
3. Staged

This can be considered as a promotion based level.  
As the content matures it can move up a level.

In _commited_ state data is basically stored in local database.  
In _modified_ state means the file has been changed but not yet commited to the databse yet.  
In _staged_ state means the modified file is marked to be part of the next commit snapshot.

> All these changes are still local

<br>

**3 Areas of Git**

1. Working directory: Where content is created, edit and deleted.
2. Staging directory: Where changes from the local directory will be staged before commited.
3. Once we perform a commit all changes will be stored in local Git directory, even when we clone from Github.
4. Finally we can send these files in central location or remote repo in our case which will be GitHub.

<br>

**Using Git**

Can be used from CLI: Local console.  
Or GUI: _GitHub Desktop_, SourceTree, Tower

```bash
git #
git config # Configure the tooling
git init # Create an empty repo, .get is creted in the current directory.
git clone # Clone a remote repo into local directory on a machine. Also creates a checking branch.
git add # We can add a file or multiple files into staging area. Making them ready for commit later. Options to add selected files as well.
git commit # Commits the changes to local repository. Commit message sent along.
```

---

<br>

## **Getting Started**

<br>

### **Setting up Git**

After installing git we can access git bash to interact with git configurations.

Usualy syntax of git goes along with git config and the user type global

The git config file stores values like user name and email under the key user.

```bash
git config --global user.name "Ankit Chauhan"
git config --global user.email "ankitchauhan.1718@gmail.com"
```

We can either call git config edit command to edit in code editor or set the name and email in bash itself.

```bash
git config --edit --global
```

Git will always open the code editor that has been setup in the environment variables. You can type code in bash to automatically open the code editor for git or change the calling variable.

```bash
git config --global core.editor "code --wait --new-window"

code
```

<br>

### **Working with Git locally**

Making the directory to be used with Git

```bash
mkdir "C:\code\firstGit"
```

Changing current directory to created directory

```bash
cd "C:\code\firstGit"
```

Initializing for git to use as database and track directory. Also serves as main branch to git.

```bash
git init
```

Verify the files in the current directory

```bash
ls --la
```

Check the status of the directory like 1. If the directory is main branch, 2. if there are any commits, 3. if any files are yet to commit

```bash
git status
```

Shortcut to create a file readme.md in same directory. Opens with Code editor automatically

```bash
code readme.md
```

If we created/modified a file then we can check status to check untracked files/changes waiting inside directory.

```bash
git status
```

Adding the file so that git does track the file. Adds the file to the list of objects being tracked by git.

```bash
git add readme.md
```

If we added a file to git, means git is now tracking the file for changes but it's not part of the commit yet.

```bash
git status
```

We pass some message while commiting and now a new commit is created locally.

```bash
git commit -m "Some commit"
```

Verifying current status after commit.

```bash
git status
```

Suppose we created number of files in our directory and checking the git status we see couple of files being indicated.  
We can use the below cmd simply to make git track all the files.

```bash
git add .
```

This way we can commit all files at once

```bash
git commit -am "New message"
```

View history of the git commits

```bash
git log
```

---

<br>

## **GitHub**

<br>

Github is web based hosting service for git and extends what we can do with git.

- Developers can use it to store code.
- Developers can use Pull requests users to pull code changes into another branches (Part of code review)
- Developers can work with issues to register bugs that needs to be fixed. Also contains Project board to manage work.
  > Anyone can propose changes to existing projects
- CI/CD features in GitHub help in countinuous integration and deployment. This is done using GitHub actions.

<br>

**GitHub Dashboard**

- _Repo_: A repository is a building block of GitHub
- _Issues_: Users can log bugs using issues.
- _Pull Request_: Someone asking you to merge changes into another branch.
- <o>_Action_:</o>
- _Projects_: Are like Project boards and is a way to manage the work inside a repository.
- _Wiki_: Used to store documentation.
- <o>_Security_:</o>
- _Insights_: Gives activity insight in the repo. Eg: How many people are working, How many changes and commits, etc.
- <o>_Settings_:</o>

<br>

### **Getting Started**

<br>

> Sign up on [github.com](https:\github.com) first.

<br>

**Connection Options**

- _HTTPS_: Requires username and password need to create a session everytime.
- _SSH_: You can create an SSH key to connect to your Github account from your local machine. Also Combines with Single Sign On. As secure as HTTPS.

**Generating SSH Keys and connecting with GitHub**

Go to your user account directory and check if we already have an SSH token.

```bash
ls -al ~/.ssh
```

If you do not have any id_rsa.pub file means you do not have any old ssh keys on your machine.  
Before adding the ssh key verify if the ssh key agent is running.

```bash
eval $(ssh-agent -s)
```

Add the ssh key in the current directory (current users directory)

```bash
ssh-add ~/.ssh/id_rsa
```

After the key has been added locally, we can now add it to GitHub.

- Go to the directory where added the SHA key, "C:\Users\username\.ssh\"
- Find the default id_rsa.pub file and edit with notpad. Copy all the content.
- Go to GitHub > Settings > SSH and GPG Keys > New SSH Key
- Give a name to the Key and Paste the local ssh key
- Save the ssh key

Now come back to Git bash and verify if everything works.

```bash
ssh -T git@github.com #Confirm the warning with yes
```

This results in below message, which you can confirm with yes.

```bash
The authenticity of host "github.com (13.234.176.102)" cannot be established.
ED25519 key fingerprint is SHA256:+DiY3wvvV6TuJJhbpZisF/zLDA0zPMSvHdkr4UvCOqU.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'github.com' (ED25519) to the list of known hosts.
Hi ankitpetjay1! You have successfully authenticated, but GitHub does not provide shell access.
```

<br>

### **GitHub Search Tools**

<br>

GitHub allows search options to look for query based search on entire GitHub.

Global Search on GitHub site. Once within the repository we can scope search by querying our search name in the _current repository_, _in this organization_ or _All github_

Advanced Search Option: Search syntax automatically optimizes based on advanced queries.

---

<br>

## **GitHub Repositories**

<br>

_**What are Repositories?**_

- They can be seen as a _folder_. All files reside in the repo including history.
- We can create a repo using the GitHub GUI.
- We can clone the repo to local machine using CLI
- Alternatively, we can initiate our work locally and push that to a repo on GitHub.
- Repo can be public or private.
- For a public repo, everyone can see the code but cannot make changes to it directly. Only collaborators can.
- Private repo's allow only users with access to it to view and interact with it.

> GitHub works in distributed way
>
> - Working Directory, Staging area, .git repo are local
> - However GitHub repo is remote.
> - It can host our local repositories over remote.

<br>

**Creating Repositories on GitHub**

We can create a new repo using the Github GUI from the repositories tab beside profile overview.

- We can provide description as well as select between Public and Private.

- The README file is a landing page for your repository. We can create it locally and push it.

- We can specify files that do not make sense to our code using .gitignore

- Choose a license to give people clear understanding of what they can and cannot do with your code. Eg: GNU General Public Library v3.0

> GitHub displays the repo as: <b>"Ankitpetjay1/Repo-name"</b>
>
> Repo "About" settings provide a Description for our repository which people will be able view.
>
> The first tab in the repository is _**<> Code**_ that displays out files and code inside the repo.
>
> The default branch is the _main_ branch which we will be creating pull requests to by default.
>
> Through the code button, we can use the ssh code, GitHub Desktop, Visual Studio or Zip file to interact with the repo.
>
> The repository will have an initial commit to view what was commited when the repo was created. We also have a commit code.
>
> If README file is not present GitHub will prompt you to update it.

<br>

**GitHub workflow**

1. Using the `git clone` cmd we create a local copy of the remote repository.
2. We can now edit files and add new files, the new files will be tracked using the `git add` command.
3. Once we are pleased with our work we will perform a commit to store changes in local repo.
4. We are now ready to push these changes back to GitHub. Using the `git push` command
   - If others have made changes while you were making the edits, your push will lead to conflict.
   - Recommended to check if other changes have been made before you push. If so bring those changes first to your local machine and fix them.
   - We can perform `git fetch` which will bring down the changes made that you do not have locally yet but will not merge. We can do `git merge` manually.
   - A `git pull` request is another shortcut method to do fetch and merge together in to your local repository.
5. After successful merge we can again push to Github so others can see the changes you have made locally.

<br>

**Working with Repository**

After creating the GitHub repository in previous steps, we are ready to clone the repo to our local machine.

Obtain the clone ssh link from within the Code dropdown in the repository code view.
