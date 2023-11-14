# Hackathon-ULBS
Acest Repo este pentru proiectul Hackathon Open Your Mind
Echipa Logiscool Sibiu

Tema proiect: Transport Urban

____Basic Git Commands____

1) **_git clone <repo_link>_**
    Git clone is a command for downloading existing source code from a remote repository (like Github, for example). In other words, Git clone basically makes an identical copy of the latest version of a project in a repository and saves it to your computer.
2) **_git branch <branch-name>_**
    Branches are highly important in the git world. By using branches, several developers are able to work in parallel on the same project simultaneously. We can use the git branch command for creating, listing and deleting branches. This command will create a branch locally.
3) **_git push -u <remote> <branch-name>_**
    To push the new branch into the remote repository, you need to use this command
4) **_git branch or git branch --list_**
    Viewing branches
5) **_git branch -d <branch-name>_**
    Deleting a branch
6) **_git checkout <name-of-your-branch>_**
    This is also one of the most used Git commands. To work in a branch, first you need to switch to it. We use git checkout mostly for switching from one branch to another. We can also use it for checking out files and commits.
7) **_git checkout -b <name-of-your-branch>_**
    shortcut command that allows you to create and switch to a branch at the same time
8) **_git status_**
    The Git status command gives us all the necessary information about the current branch. 
9) **_git add <file_name>_**
    We need to use the git add command to include the changes of a file(s) into our next commit.
    To add everything at once: **_git add -A_**
10) **_git commit -m "commit message"_**
    This is maybe the most-used command of Git. Once we reach a certain point in development, we want to save our changes (maybe after a specific task or issue).
    Git commit is like setting a checkpoint in the development process which you can go back to later if needed.
    We also need to write a short message to explain what we have developed or changed in the source code.
11) **_git push <remote> <branch-name>_**
    After committing your changes, the next thing you want to do is send your changes to the remote server. Git push uploads your commits to the remote repository.
12) **_git push --set-upstream <remote> <name-of-your-branch>_**
    However, if your branch is newly created, then you also need to upload the branch with the following command: **_git push -u origin <branch_name>_**
13) **_git pull <remote>_**
    The git pull command is used to get updates from the remote repo. This command is a combination of git fetch and git merge which means that, when we use git pull, it gets the updates from remote repository (git fetch) and immediately applies the latest changes in your local (git merge).
14) **_git log -- oneline_**
    to see our commit history
15) **_git revert_**
    Sometimes we need to undo the changes that we've made. There are various ways to undo our changes locally or remotely (depends on what we need), but we must carefully use these commands to avoid unwanted deletions.
16) **_git fetch_**
    Before merging, you should update your local dev branch:
17) **_git merge <branch-name>_**
    Finally, you can merge your feature branch into dev

More info can be found in here: https://www.freecodecamp.org/news/10-important-git-commands-that-every-developer-should-know/
