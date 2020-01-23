# Book review site
It's my solution for CS50's Web Programming with Python and JavaScript project 1.
https://docs.cs50.net/web/2020/x/projects/1/project1.html

# I am NOT front-end developer. User interface is only for testing.

* Website where you can find book if it is in database and look at average grade from Good Reads page.
* User must be log in to add review.
* App use external Postgres database, you have to set environment variables for database to run app.
* For security reason database credentials are not added to repository.

TO RUN:
* Set up Postgres database
* pip install -r requirements.txt
* export FLASK_APP=application.py
* flask run