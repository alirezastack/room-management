# Room Management API

## Setting up a new environment
```shell
python3 -m venv env
source env/bin/activate
```

## Install requirements
Next step after activating virtual environment is to install django DRF requirements via `pip`:
```shell
pip install -r requirements.txt
```

## Run the project
Now go to `rooms/roomproj` and issue the below command to start a django development server:
```shell
$ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
October 30, 2021 - 17:58:46
Django version 3.2.8, using settings 'roomproj.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Now you should be up and running! :)