# Countries Population

### What this application does?

This application retrieves a full list of Countries' names, capitals, and populations at defined years, then stores them in the database. You can then go to specific end points to retrieve different kinds of data.

### Where do you retrieve the list from?

The list is retrieved from [**an API endpoint**](https://documenter.getpostman.com/view/1134062/T1LJjU52#intro).


## How it works

### Core

This application is built with python, using Django as a framework to ease the process.

### Extras

* DRF (Django rest framework) was used to help serialize and view the API results easily in the browser without the need to use Postman, and to help with pagination as well. (Though it is recommended)
* Black was used to help format the files accordingly with [**PEP8 style guidelines**](https://www.python.org/dev/peps/pep-0008/).

### Starting the application

After making a virtual environment (Recommended), run the following commands:
```python
pip freeze -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

**NOTE** : Within the application there's a ```requirements.txt``` file that contains the requirements for the application to run. (Recommended to have those installed in a virtual environment)

## APIs in Action
**`/populate`**: First thing's first, let's populate the database.(Note that this page has no rendering effect as its only purpose is to populate the database, it also takes some time to get ALL the records as the API contains a very large number of records)

**`/population/`**: Now that the database is populated, we can go and check a list of the countries populations at different years. (Limited to 50 per page)
![image](https://user-images.githubusercontent.com/49989718/209130943-d9e0774e-e50c-4b66-8746-61d74b574dd6.png)
![image](https://user-images.githubusercontent.com/49989718/209130899-5eb3d83d-dd26-4fb2-ba74-698825a79ab6.png)

**`/population/<code>/`**: If we need to find out the population of one country at different points of time, this endpoint retrieves all the instances of the country with the code given as a parameter in the url. (Again, limited to 50 per page)
![image](https://user-images.githubusercontent.com/49989718/209131385-85fcff11-4ab2-48d5-ace3-ff39eba3e79e.png)
![image](https://user-images.githubusercontent.com/49989718/209131390-1ce3dd94-9e46-424d-b474-67246e98294e.png)
