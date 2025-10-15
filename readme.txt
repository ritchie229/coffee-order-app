#--------------------------------------------
#--------------- COFFEE-APP -----------------
#------------by-Rishat-Mukhtarov-------------
#----------------------------------year-2025-
#-------------------------tested-on-Shipyard-
#--------------------------------------------


The project structure:

coffee-order-app
├── docker-compose.yml
├── init_db
│   └── init.sql
├── nginx
│   ├── default.conf
│   └── Dockerfile
├── readme.txt
└── web
    ├── app.py
    ├── Dockerfile
    ├── static
    │   ├── img
    │   │   ├── americano.jpg
    │   │   ├── capuchino.jpg
    │   │   ├── espresso.jpg
    │   │   ├── latte.jpg
    │   │   └── mocachino.jpg
    │   └── style.css
    └── templates
        └── index.html

Start: docker compose --build up
Stop: docker compose stop (to start after stopping use docker compose up)
Remove: docker compose down (all containers will be removed, no data stored - using an external volume is not presentes as the app was deployed on Shipyard)

This is a simple web app created in terms of DevOps study process consists of three parts, DB, WEB app and NGINX.
DB - MariaDB;
WEB - python flask app;
NGINX (can be skipped using flask app directly on port 5000).

This app is somewhat like an emulator of a coffee machine, you enter your name and choose the coffee type, press Order button and in a short while it returns "Please your coffee".

Let the Power be with You.
