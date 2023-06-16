# Search System
Developed with: Python, Django and MySQL<br>
Interface: Bootstrap

The database structure anda data is based on the project of the course [Buscas em textos com Python](https://www.udemy.com/course/inteligencia-artificial-buscas-em-textos-com-python/) created by Jones Granatyr 

![Search](https://github.com/joselinosantosti/search-system/blob/master/search/static/img/search.png)

# How to run
## 1. Install MySQL Database 
### On Linux
1. `apt install mysql-server mysql-client python3 -y`
2. `sudo apt-get install python3-dev default-lib mysqlclient-dev build-essential`
### Other Os, follow the link
https://github.com/PyMySQL/mysqlclient/blob/main/README.md

## 2. Create a database with name "search" and import data from the file search.sql using some tool like Mysql Workbench or Dbeaver
`CREATE DATABASE search`

## 3. Clone this repository and extract in your computer
`git clone https://github.com/joselinosantos/search-system.git`

## 4. On project directory create and activate a virtual env with the follow commands
`virtualenv .venv`
`source .venv/bin/activate`

## 5. Install all libs
`pip install -r requirements.txt`

## 6. Check the database password
The password from prject is 'admin', check your database and set the configuration on file settings.py on line 'PASSWORD': 'admin',

## 7. Run the app with:
`python manage.py runserver`<br>
Access the url in your browser: localhost:8000

## 8. Insert some word and click in search button