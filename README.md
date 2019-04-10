# Dashboard

> Dashboard for technical interview at Playvox.

## Frontend setup
Front end is builded with vuejs, also uses chartjs for the plots.
Is located inside the "dashboard" folder, the available commands are:
### install dependencies
npm install
### serve with hot reload at localhost:8080
npm run dev
### build for production with minification
npm run build

## Database
The used database was MongoDB, to create the collections was used the "mgeneratejs" tool.
This tool directly insert a desired random data to the database.
Respect to the length: 
- For the stage 1 and 3 the data has the correspondent slength (1.2M and 456 respectitly).
- For the 2 was created a test DB with around 7M registers, because the problem to storage locally a 1000M DB.
Additional comments:
To archive a better performance, the stage 1 collections was joined in one collection called BOOKS.

## Backend
The backend was deployed using Flask. Its an API who answer to each request.
It was created inside a python virtual environment. The required libraries are:
- flask, flask_cors, pymongo,bson, json, datetime
All of them are available via pip command.
To start the server a simple "python server.py" command its required.

## General Info
The used strategy used was: Due to the soft proccessing stage, the db query was enough.
- If the Query is fast, only execute it.
- If its slow, store it in a local text file, and do available its consult.



