# dengue

Dengue GIBD Project

# IMPORTANT

The following are some notes and **strong** recommendations provided by Ramiro Rivera <ramarivera@gmail.com> on 2020/06/27. Feel free to reach out if you have any questions.

- Please make sure to update the requirements.txt file every time you install a new package, otherwise Heroku won't be able to find the right packages even if they work in your local machine. You can do this by running `pip freeze > requirements.txt`
- The procfile callable format is {APP_MODULE}:{APP_CALLABLE}, where APP_MODULE is a full dotted module address (if you had app.py inside a folder called dengue then APP_MODULE would be dengue.app without the .py extension) and APP_CALLABLE is either a gunicorn compatible variable (dash_app.server or django for example) or a callable wrapped in strings. If not APP_CALLABLE is provided gunicorn will default to look for `application`. Therefore the right argument for us is `app:server` since we are invoking the `app.py` file which is in the repository root and starting the `server` application (flask app) exposed by the Dash framework.
- In order for gitignore files to work they must be called `.gitignore`. Windows can sometimes (usually) mess up this with their extensions shit.
- I've configure this repo to be automatically formatted by Black every time the app file is saved. This assumes black is installed in your current python interpreter path (either conda, global python or a virtualenv). If not, make sure you drop to a shell running your python interpreter and just `pip install black`. easy peasy.
- Please use Vs Code.
