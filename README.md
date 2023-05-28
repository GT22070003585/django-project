Django Project

In this project I developed a website where you first login or create a user and then login. 
After succesfully logging in, you access a website that sells electronics.
At the bottom of the website you can access three more pages: A "Get In Touch" page, a "Shipping and Returns" page and a "Help us Improve" page.
The first two that were mentioned contain just text whereas the "Help Us Improve" page has polls.
By choosing a question from the pole the user can choose(vote) one of the answers that are given.

First of all, download all the folders and files. The main app/folder is django_project.
The "accounts" app/folder is for login and sign up of a user, the "website" app/folder contains the website(main page), contact and shipping pages.
The "polls" contain the necessary files to create questions that users can vote on the given choices of each question.

Open Commnad Prompt, go to the same directory as manage.py and type:
python manage.py runserver
(make sure you have django succesfully installed n your computer)
after you press enter, the command prompt will give you a web link to click on.
After clicking that you will be directed to a website where you have the choice to login or register an account if you are a new user.
after signing upyou can login and gain acccess to the website, that has three other pages at the bottom.

One of those pages are the polls.
If you wish to add more questions or choices on there go back to the terminal and type:
python manage.py createsuperuser
This will give you blanks to fill such as user, email (not real one) and a password.
After you creater your "super user" aka admin account
run the server again but now at the end of the http link add 'admin/'.
This will direct you to the admin page where you login with your super user details and can add as many questions as you want (relevant to the project).
Those questions also require choices where you also have a chance to add them.
