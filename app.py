from flask import Flask
import flask
app = flask.Flask(__name__)


@app.route('/')
def index():
    test_packages = ['p1', 'p2', 'p3']
    return flask.render_template('index.html', packages=test_packages)

@app.route('/about')
def about():
    return flask.render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)

