#fitquo
A project for CS 411 - Database Systems at University of Illinois at Urbana-Champaign.
Created by Madina Abdrakhmanova, Rishi Bajekal, Mohd Irtefa, and Stephen Lee.

__BEFORE EDITING OR ADDING CODE, PLEASE MAKE SURE YOUR TEXT EDITOR IS SETUP TO USE 4 ACTUAL SPACES (NOT TAB) ON AN INDENT.__

##Installation:
To install and run this application. Follow the steps below.

###Create Virtual Environment
If you haven't done so already, create a virtualenv for the project using:

    mkvirtualenv fitquo

###Activate the Virtual Environment
Whenever you want to work on the project, before beginning work, run:

    workon fitquo

##Contributing to the Project
When contributing to the project, follow these guidelines:

###Code Reviews
- Use personal branches (ie. __do not__ develop in the `master` branch)
- When you're ready to promote your code, create a [Pull Request](https://help.github.com/articles/using-pull-requests).
    - If possible, reference your Task or Story from the Pivotal Tracker
- Code review comments are recorded in github
- Code reviewer sign-off must be recorded as a comment on the pull request

###Git Workflow
Here is a sample workflow of how to work on a new Task.
For the purposes of this outline, assume I am working on a task called "Build project skeleton".
The feature branch I am working on is called `skeleton-rishi`.

1. Create a new feature branch for the task (assumes your current branch is `master`)

    ```
    git checkout -b skeleton-rishi
    ```

2. Complete the work for the task (including unit tests)
3. Push task branch to github so that you can create a pull request

    ```
    git push origin skeleton-rishi
    ```

4. Create a pull request at https://github.com/rishibajekal/trainerhack
5. Your code now needs to be reviewed by someone else on the team. Make any changes suggested by the reviewer and repeat steps 2 through 3
    - Comment on your pull request if new commits are made so anybody involved is notified of changes
6. You (the developer), merges your user branch into `master`

    ```
    git checkout master
    git pull
    git merge skeleton-rishi
    git push origin master
    ```

7. Remove the remote and local feature branch

    ```
    git push origin :skeleton-rishi     # Deletes the remote skeleton-rishi branch from github
    git branch -d skeleton-rishi        # Deletes your local skeleton-rishi branch
    ```

