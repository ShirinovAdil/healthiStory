Before running server there is need to configure database settings. If you already install mysqlclient just go to settings.py file
and find DATABASES section and configure it, otherwise mysqlclient should be downloaded.
To do this open terminal and type (for windows) pip install mysqlclient, (for linux) pip3 install mysqlclient
For linux OS you can also install the package in the project ===>>>>> open terminal: pip3 install mysqlclient-2.0.1-cp38-cp38-linux_x86_64.whl
Once everything is fine with DB the next step is to install python packages placed in 'requirements.txt'
To do it type in terminal ====>>> pip install -r requirements.txt
To run the server open terminal ====>>> py manage.py runserver
To stop server press ctrl C
If you have unapplied migrations for Windows OS:
    1.Open terminal and type: py manage.py makemigrations (for windows)
    2.Then type: py manage.py migrate (for windows)
For Linux OS:
    1.python3 manage.py makemigrations
    2.python3 manage.py migrate
To see the admin page type in browser's url '/admin' after localhost...
-----------------------ABOUT THE PROJECT----------------------
The main app is HealtiStory, alongside this there are home(keeps static pages such as home page, contact page etc.),
account (for sign in and registration), product.
All HTML files are in templates folder. Css, images and js files are in static directory.
For multilingual web site all translations are in locale folder. To make new translations in terminal
===>>> django-admin makemessages -l az  (az is optional can be ru tr etc.)
The file with .po extension contains translatable stuff
Once the translations are ready open terminal ====>>>> django-admin compilemessages