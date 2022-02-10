#Booking Diagnostic

####Quick Start Guide

1. Setting up a virtual environment

    After cloning the project, go to the project folder using the terminal and type the following command:
    
    ```
    python3 -m venv venv
    ```
    
    now activate the environment:
    
    ```
    source venv/bin/activate
    ```

2. Django must be installed, along with all required modules and third-party libraries
    
    Type the following command:
    
    ```
   pip3 install -r requirements.txt
   ```
   
3. Need to create a database

    Type the following command:
    
    ```
   sudo apt install postgres
   sudo -i -u postgres
   psql
   ```
   
   then
   
   ```
    CREATE DATABASE dbname;
    ```
   
    after that go to the ***.env*** file and change the database settings to your database:
    
    ```
    SECRET_KEY=generate your own secret key and paste here
    DB_NAME=username
    DB_USER=name of database
    DB_PASSWORD=your password
    DOMAIN=http://localhost:8000
   ```
   
4. Migrations to the database

    Type the command in the terminal:
    
    ```
   python3 manage.py makemigrations
   ```
   
   then
   
   ```
    python3 manage.py migrate
    ```
   
5. Create superuser

    Enter the following command to create a superuser:
    
    ```
   python3 manage.py createsuperuser
   ```
    
    then enter the requested data

6. Before start
   Run test
   ```
   python3 manage.py test
   ```
    
7. Server start

    Enter the following command in terminal:
    
    ```
   python3 manage.py runserver
   ```   

    Fine! Project is ready to use.

#Docker Flow
