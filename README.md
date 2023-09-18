
Hello ,


My final project is a to do list project that include login and sign up / register systems has been built using Django, a high-level web framework that allows developers to quickly and iteratively build, 
prototype and deploy web applications. It does this by including a large amount of the common functionality of web applications (i.e. user account management, security, database management) right out of the box. 
The framework also encourages developers to work within this philosophy - the re-usable elements of a project (such as a comments system, or an basket order system) are housed in self-contained ‘app’ directories, 
so they can easily be picked up and slotted into other projects that require the same functionality..


### Features :

   - sign up system :*
      The User can create an account using my simple sign up system which required a username and password and password verification 

       Note : Name and password should be well selected and not already used otherwise the sign up will fail and the user will be auto redirected to same signup page       again.

   - Login system :*
     The user can simply visit my website login to his already created account where he will find all his tasks done or not done yet saved and secured. Nothing will be lost / changed 
     and no one will have access to an other user account whiithout his permission and without giving him the login details .

   - Eveything will be auto saved and any saved changes can be done only by the user. 
   - System wont auto delete the user account or auto change anything.
   - Create new Task : users are allowed to create / generate multiple tasks and add description to the ( discription is optional ) the user can create a new task even when description field is empty.
   - Edit tasks : The User have access to all his created tasks and he can edit theml at anytime : Task Name and description 
   - Mark the task as done/undone : User can mark his task as done/undone whenever it is by clicking it and checking/unchecking the ( Complete ) checkbox and submiting.Task bubble will be white 
     and will be changed to green when it s marked as done and the -task name will be crossed aswell so it s easier to figure it out from the user
   - Delete task : User have permission to delete his own tasks whenever he want to ( tasks will be permanently deleted and no way to restore them .
   - The system got counter included , this counter will indicate how many uncomplited tast are left to do/complete.
   - Search bar : this search bar will help users filter any task by name or even a letter from the name to make it even easier in case the user don't remember the whole task name.

#### Files and directories
  - `todo_list` - the core project folder .
  - `base` - main application directory.
    - `templates/base` contains all application templates.
        - `main.html` - base templates. All other tempalates extend it.
        - `login.html` - this is the form used for the login page , will contain 2 inputs which are username and password and a login button with a register now button aswell .
        - `register.html` - this is the register/signup template: contains 3 inputs ( Username/Password/Password Confirmation) a register now button and a login button if the user already have an account.
        - `task_list.html` - templates for users tasks list and it is considered as the default basic interface for users to check/edit and add tasks.
        - `task_form.html` - template that shows when the user want to add/edit a task.It will contain all taks details such as task name and description and completed or not and from there the user can edit or add a new task.
        - `task_confirm_delete.html` - this template shows when the user want to delete a task to display a sentence to inform the user that he is going to permanently delete the task .
        - `task.html` - template for the task display structure.
    - `admin.py` - contains the basic admin panel 
    - `models.py` contains only 1 main class that including 5 models : `user` model to show the user name / `title` model for the task title / `description` for the task description / 
        `complete` model to mark the taskas completed when it is and finally a `created` model to show those created tasks with a default value as true.
    - `urls.py` - all application URLs/Paths ( i used 9 Paths) .
    - `views.py` respectively, contains all application views . With 8 main classes here are some inportant ones : 
        - `CustomLoginView` which will redirect the user the login template which is login.html.
        - `RegisterPage` this views class is used to redirect the user to the registering template which is register.html
        -  `TaskList` this view class will render the tasks list and it contains search and the filter conditions.
        `TaskUpdate` this view display the task update template which contains 3 input fields ( title / discription / complete or not ) and give the ability to the user to manage them .
    - `test.py` - made it to run any test needed in there.
    - `forms.py` - contains forms used on my project to facilitate the work
    - `apps.py` - contains all my projects apps



#### Why My Project ? ( justtification : )
   *This project is distinct from all previous projects so far. Why?*

         -More views with complex relation between them.
         -contains login and signup system
         -Saves hashed password reset code in db.
         -all Static files are included in 1 html file linked and extended to all other html files which made the work cleaner.
         -Completely Mobile responsive. 
         -Easy to use and eveything is so clear and tidy.
     ---> This project wasn't easy to make and it almost contains all stuffs i learned from CS30W course and im proude today that im able finally to work out a project
          that way and i want to Thank all CS50 Havard Team . This project is a way complicated to do but i made it so simple for users , The project main main interfaces are so simple and clean and the code it so tidy and clean aswell. I hope you enjoy it ! 



#### This project Have no extra requirements (just basic requirements) : Python / Django


Great regards , Neder Said . 
