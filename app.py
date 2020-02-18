from flask import Flask
import flask
app = flask.Flask(__name__)

def main():
    register_blueprints()
    app.run(debug=True)

def register_blueprints():
    from omega.views import home_views
    from omega.views import package_views
    from omega.views import cms_views


    app.register_blueprint(home_views.blueprint)
    app.register_blueprint(package_views.blueprint)
    app.register_blueprint(cms_views.blueprint)

if __name__ == '__main__':
    main()

