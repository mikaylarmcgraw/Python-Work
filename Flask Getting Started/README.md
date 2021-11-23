# Flask Learning Spike

## Installing packages in project
- When creating a web application with Flask you need to first install Flask in your project using the command: ` pip install -U Flask` and adding the following import statement: `from flask import FLASK`

## Adding Flask to Application
- In your class file under the import statements insert this line of code: `app = Flask(__name__)
`. This sets the `__name__` variable to the module name. For instance in our flashcards.py file our variable `__name__` will be set to `flashcards`. 

## Setting FLASK_APP & FLASK_ENV Variables
- You need to specify what file and environment you want your flask app to run and in what mode. For this project we want to run `flashcards.py` in development mode.

Run the following to specify what file your flash app will run:

Windows users:
- `set FLASK_APP=flashcards.py`
- `$env:FLASK_APP = "flashcards.py`

Mac users:
- `export FLASK_APP=flashcards.py`

Next enter the following tp specify the environment your flask app is running on: 

Windows users:
- `set FLASK_ENV=development`
- `$env:FLASK_ENV = "development`

Mac users:
- `export FLASK_ENV=development`


## Running Flask Application
- Once your environment is successfully set up you can run the following command: `python -m flask run -p 9999
` this will run the flask application on the specified port 9999. To stop the server just press CTR + C.
## CORS 
- To enable your application to send and receive requests from other web apps you need to enable CORS (Cross Origin Resource Sharing). You can enable CORS in your application with the following steps:
- First install the package flask-cors using the following command in your terminal window: `pip install -U flask-cors`
- Once CORS has been installed successfully add this import statement to your file: `from flask_cors import CORS`
- Next add this line of code below initializing your application in your file: `CORS(app)`

## Jinja Templates

Our flask application has a `templates` directory which contains components that display data to the user. Jinja templates generate text files which we use to create HTML.  Templates are text files with placehoders for varaibles you can see we insert a Jinja variable in our html document called `{{message}}` which we specify the variable contents in the view `flashcards.py`. You can also add logic to these templates such as if, for, filter statements, etc...