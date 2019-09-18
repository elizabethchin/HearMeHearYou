# <div align="center"><img src="/static/img/readme.png" title="HearMeHearYou" alt="Hear Me Hear You Logo"></div>

**HearMeHearYou** is a confidential resource to resolve workplace issues. My vision is for companies to adopt this platform with independent oversight. With encryption built in users can submit inquiries securely with the option to remain anonymous. Employees can seek advice on career development, any workplace conflicts such as bullying, sexual harassment, whatever concerns they have. The hope is to create a better work environment and democratize workplace support.

# Table of Contents
* [Tech Stack](#techstack)
* [Current Features](#current-features)
* [Installation & Use](#installation)
* [Future Features](#future-features)
* [About the Developer](#developer)

## <a name="techstack"></a>Tech Stack
__Frontend:__ HTML5, CSS, Javascript, jQuery, Bootstrap <br/>
__Backend:__ Python, Flask, PostgreSQL, SQLAlchemy<br/>
__APIs:__ Google Maps <br/>

## <a name="current-features"></a>Current Features
- Encryption
- Anonymous submissions
- Reply thread
- Save reports for later submission
- Record keeping



## <a name="installation"></a>Installation & Use

#### Requirements:

- PostgreSQL
- Python 3.7.4
- Google Map API Key

To have this app running on your local computer, please follow the below steps:

Clone repository:
```
$ git clone https://github.com/elizabethchin/HearMeHearYou
```
Create a virtual environment:
```
$ virtualenv env
```
Activate the virtual environment:
```
$ source env/bin/activate
```
Install dependencies:
```
$ pip install -r requirements.txt
```
Get your own secret keys for [Google Maps](https://developers.google.com/maps/documentation/javascript/get-api-key). Save them to a file `secrets.py`. Your file should look something like this:
```
keys = {"google_map_api": api_key_here}
```
Create database 'hearmehearyou'.
```
$ createdb hearmehearyou
```


Query the database, run in interactive mode
```
$ python3 -i model.py
```
Create your database tables and seed example data.
```
$ python3 seed.py
```
Run the app from the command line.
```
$ python3 server.py
```
## <a name="future-features"></a>Future Features

- Deployment - <a href="www.hearmehearyou.com"> www.hearmehearyou.com
-  SocketIO for instant messaging

## <a name="installation"></a>About the Developer
This is Elizabeth's first project, she loves how programming constantly challenges her and the juxtaposition of structure and creativity it offers. Checkout her <a href="https://www.linkedin.com/in/elizabethtchin/">Linkedin</a>



