# spk_pool_scrp
#### Video Demo:  [link](https://www.loom.com/share/e0f8a0aff530453cad06b7de0268d5ad)
#### Description:

the project contains these main parts:

* database modul
  * there you can find create_table.py and database.py
    * create.py contains function which will create table into database when you run it
    * database.py contains two functions one is parsing database.ini file and the second function will use these params to connect int database
* app.py
  * here is the main logic of the program. The app.py contains 2 functions - the first one is for scraping data from website. I am using the beautifulsoup as library for scraping. I am parsing result and store it into 2 variables. The second function is for save the new raw with results int database. It contain these colums: id, num_ppl_in_swimming_pool, num_ppl_in_sauna, timestamp 
* __main__.py
  * in main you can find also 2 functions the main which is creating instance of App class end using it and the second function is for schedule and run it the main function every 10 minutes
  * I am using the schedule library here because it is the easiest way how to run it locally imo.



project is available on my github [https://github.com/jakubturner/spk_scrp_pool]
you can copy it as you wish.

prerequisites:

* python 3.8 + [link](https://www.python.org/downloads/)
* poetry [link](https://python-poetry.org/docs/)
* postgresql [link](https://www.postgresql.org/download/)

purpose of project:
We have serious problem to get into swimming pool and sauna in our city - we tried really hard with my friends but there were lot of people everytime in every hour. So we decided, that we have to fight against those people which are waiting for us and everytime we try to get into sauna or swimming pool, they run into the gate of our local swimming pool and try to occupy every free cabinet in the cloakroom. We tried to be faster but everytime they beat us. So we have to be clever next time and in this moment we created the new strategy. 

We will be scrape data from local swimming pool website [here](https://www.sumperksportuje.cz/aquacentrum/kryty-bazen) and store it into postgresql database. After few weeks (after the all the bad people which try to block us from visiting sauna and swimming pool will think that they won), we will load those data into visualisation toll (plotly, powerbi) and we will plan the revenge in time that we will know that they are not near the our oasis. We will occupy all cabinets and drink all tea and water there. If you want to help us continue below ->


How to install it

in root directory run: 
```sh
poetry shell
```

it could create poetry virtual environment

then you can continue to install all dependencies:

```sh
poetry install
```

after that you need the last step -> create database.ini file with your database credentials
so create that file in root of project and fill it with your credentials like this: 

```sh
[postgresql]
host=[your host name]
database=[your database name]
user=[your user name]
password=[your database password]
```


How to run it

because you install all dependencies the app is now as package itself - it means that you can call it with

```sh
spk_scrp
```
