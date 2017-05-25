For this tect test for SkyBet I decided to try learn a new python framework to create a very light weight restful web app to control a form.
I chose flask due to its very simple start up and useful libraries to create this.

The plan is to:
1. Create a local JSON file on disk, read from this file to populate a form with peoples first and second name. By using the root dirctory and GET request.
2. Create a way to change this form and post it back to the server and save back to the file on disk. POST request send JSON from form.
3. Add ID values to check boxes and send a DELETE request to the server to remove a particular form entry.
4. A JQuery method to create a new item on the form so more users can be added.
5. Add some form validation and a email field.
6. Create some nice styles builing on a basic bootstrap theme.

Requirements:

Python 3.6


Install:

 sudo pip install virtualenv
 
 sudo pip install Flask


 run:

 . venv/bin/activate

export FLASK_APP=skyForm.py

flask run
