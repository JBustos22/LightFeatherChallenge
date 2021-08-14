**LightFeatherChallenge - Supervisors api**

About:

This api contains two endpoints: GET:/api/supervisor and POST:/api/submit. The supervisor endpoint returns a list of supervisors ordered alphabetically by jurisdiction, last name, and first name. The submit endpoint requires the user to submit a POST request with form data containing the following fields:

`firstName`(required), `lastName`(required), `email`(optional), `phoneNumber`(optional), and `superVisor`(required).
The response specifies whether the request was successful or not, and output is printed to the server's console

**Installing and Running Instructions**

* **Debian-based Linux**
1. Clone the repository and navigate into the base project directory
2. If the docker engine and/or docker-compose is not installed in your system, run the provided install script with ``sudo chmod +x install_linuyx.sh && /bin/bash install_linux.sh``
3. Run the application with `sudo docker-compose up`
4. To hit the supervisors endpoint, either navigate to http://localhost:5000/api/supervisors on a browser or run
`curl -X GET http://localhost:5000/api/supervisors`
5. To hit the submit endpoint, run `curl -i -X POST -F firstName=John -F lastName=Doe -F email=johndoe@email.com -F superVisor=JaneDoe -F phoneNumber=999-999-9999 http://localhost:5000/api/submit`
6. If the response is successful, run `sudo docker logs supervisor_api` to see the console output

* **Windows**
1. Clone the repository and navigate into the base project directory
2. Install python 3.6 or later and pip3: https://www.python.org/downloads/, https://phoenixnap.com/kb/install-pip-windows
3. Run a command prompt as administrator
4. Enter the base project's directory
5. Run `pip install -r requirements.txt`
6. Run `python main.py`
7. To hit the supervisors endpoint, either navigate to http://localhost:5000/api/supervisors on a browser, or open a new command prompt and run
    `curl -X GET http://localhost:5000/api/supervisors`
8. To hit the submit endpoint, run `curl -i -X POST -F firstName=John -F lastName=Doe -F email=johndoe@email.com -F superVisor=JaneDoe -F phoneNumber=999-999-9999 http://localhost:5000/api/submit`
9. If the response was successful, check the command prompt running the application to see the console output
