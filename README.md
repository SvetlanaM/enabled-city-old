# EnabledCity - readme by Svetlana Margetova #

With us, you never see the city the same way.


### Technologies: ####

#### Server: ####
* Python (Django framework)
* MongoDB (MongoEngine)

#### Client: ####
* AngularJS with Marionette
* Twitter Bootstrap
* OAuth2.io

#### External API services: ####
* Forsquare API
* Google API
* Locu API

### Running locally ###

1. Install dependencies : `(sudo) npm install && pip install -r requirements.txt && bower install`
2. Run the application : `python server/server.py`
3. Open a web browser with URL [http://localhost:5000](http://localhost:5000)


### Setting up database ###
* #### Use our demo database (publicly available) ####
    
    1. Go to the *server/db.py*
    2. Change `os.environ['MONGOLAB_URI']` to `'mongodb://admin:iicenajv@ds053948.mongolab.com:53948/words'`

* #### Use your own database ####

    1. Create your own database and create *users* collection
    2. Go to the *server/db.py*
    3. Change `os.environ['MONGOLAB_URI']` with your *mongodb://* database url


### Build the application ###

1. Run `grunt build` command from command line
2. Go to the *server/app.py*
3. Change `../app` folders to `../dist` (2x)
4. Run the application : `python server/server.py`


[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/samuelmatis/langmaster.io/trend.png)](https://bitdeli.com/free "Bitdeli Badge")
