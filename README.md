# Calendar

The technologies used to complete the task:
* PostgeSQL 14.3
* Python3 (psycopg2 and datetime libraries)

The list of German holidays was found [here](https://www.iamexpat.de/expat-info/german-holidays) (though I didn't go in the region specifics)

The calendar was made with the generate_series() function for the current year (2022)

## PostgreSQL DB set up

User admin with password 'admin' with superuser privilieges was created, as well as database 'crud':

(psql)
```
create role admin with encrypted password 'admin';
alter user admin with superuser;
create database crud;
grant all privileges on database crud to admin;
```
