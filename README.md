### Jirani
### Description
##### Jirani is a web application where one can use to be on loop with the occurences of their surroundings. Search/create and join a hood and get to interact.
### Author
Murathe Isaac

![ss](https://user-images.githubusercontent.com/29546502/75358026-4eac4080-58c3-11ea-9069-19e532523cc3.png)



## Live site

### Requirements
##### These are the requirements you need to get the project running locally on your machine:
  - Text Editor
  - Install python3
  - Install and activate virtual
  - Install Django
  - Setup Database (postgresql)
  
### Set up Process
##### Install your preferred version of python
  - ```sudo apt-get install python3.6```
  - ```python --version``` to confirm that python has been installed.

##### Git clone the project on your current directory by:
  - ```git clone https://github.com/Murathe/aawards.git```.
##### Open the project on your terminal:
  - ```atom . or code .``` , 
##### Move to your project directory:
  - ```cd Innstagram```.
##### Install virtual environment using python:
  - ```python3.6 -m venv virtual```, check your project to confirm you have a folder called virtual,
  - then activate it by running ```source virtual/bin/activate```
##### To install the packages in the ```requirements.txt file```,
  - ```pip install -r requirements.txt```  
##### To open python shell:
  - ```python3.6``` ,
  - ```import django```
  - And lastly ```django.get_version()``` to see and confirm the version of django installed.
  - You can then ```ctrl z``` to get out of the shell,
##### After confirming you have all this
  - ```python3 manage.py runserver``` to run the project.
  - Then click the local host link given to open the project on a browser ```http://127.0.0.1:8000/```.


#### For more information read the following django and python documentation:
  - [DjangoDocumentation](https://docs.djangoproject.com/en/1.11/intro/install/)
  - [PythonDocumentation](https://www.python.org/doc/)



### User Stories
1. Sign in with the application to start using.
2. Set up a profile about me and a general location and my neighborhood name.
3. Find a list of different businesses in my neighborhood.
4. Find Contact Information for the health department and Police authorities near my neighborhood.
5. Create Posts that will be visible to everyone in my neighborhood.
6. Change My neighborhood when I decide to move out.
7. Only view details of a single neighborhood.


### Technologies Used
1. Python
2. Django
3. PostgreSQL


### Licence
[MIT](LICENSE)

