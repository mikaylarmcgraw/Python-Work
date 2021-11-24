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
` this will run the flask application on the specified port 9999. To stop the server just press CTR + C. In general there's no need to typically restart flask when making changes to your code. Flask will refresh itself and pick up your changes.

## CORS 
- To enable your application to send and receive requests from other web apps you need to enable CORS (Cross Origin Resource Sharing). You can enable CORS in your application with the following steps:
- First install the package flask-cors using the following command in your terminal window: `pip install -U flask-cors`
- Once CORS has been installed successfully add this import statement to your file: `from flask_cors import CORS`
- Next add this line of code below initializing your application in your file: `CORS(app)`

## Jinja Templates

Our flask application has a `templates` directory which contains components that display data to the user. Jinja templates generate text files which we use to create HTML.  Templates are text files with placehoders for varaibles you can see we insert a Jinja variable in our html document called `{{message}}` which we specify the variable contents in the view `flashcards.py`. You can also add logic to these templates such as if, for, filter statements, etc...

## Routing

App routing is used to map the specific URL with the associated function intended to perform a task. You specify a route to a function by adding `app.route("/cards")` above it. The route: `app.route("/cards)` for instance can display a list of all flashcards we have in our json file. You can pass in parameters to the route as well by using the `<type: variable>` syntax. For instance if you wanted to view a flashcard with index value 1 the route would look like: `app.route("/cards/<int:index")`

## Reverse URL Building
You can decouple the routes from the view by passing in the function name to the `url_for()` method. For instance in the card.html file we specify the URL for the home screen by passing in the welcome function: `url_for('welcome')`. This helps with not having to update all the routes if you decide to make a change later on.


## Error Handling

Error handling is used wrapping the block of code with a try except handler. You first import the abort module from flask using  this statement: `from Flask import abort` You can abort with an error code of a 404 for example if a URL entered by the user doesn't have a mapping by passing in the error status code to the abort function: `abort(404)`.
