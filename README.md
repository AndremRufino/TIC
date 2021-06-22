RUN PROJECT:
    - Requirements : 
        - python 3.8
        - django 
        - djangorestframework
        - psycopg2
        - psycopg2-binary
    run in your ubuntu:
        - which python3
        if the command above return a error run these commands
           - sudo apt-get install python3
           - sudo apt-get install python3-pip
        

    run: pip install (name_of_the_package)

STEP-BY-STEP:
    * OPEN THE FILE settings.py /TIC/TIC/settings.py
    * On the fields DATABASE text your postgresql data
    * With the database configured text on terminal (your terminal (vscode) needs to be in the directory /TIC/TIC ): 
        - python manage.py makemigrations
        - python manage.py migrate
        - python manage.py runserver
    * Test in Postman ;)