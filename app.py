from flask import Flask
import flask
app = flask.Flask(__name__)

def get_details():
    items = [{'name': 'details1', 'version':'1'}, {'name': 'butt', 'version':'0.95'}, {'Wut': 'sup'}]
    return items
@app.route('/')
def index():
    test_packages = ['p1', 'p2', 'p3']
    return flask.render_template('home/index.html', packages=get_details())

@app.route('/about')
def about():
    return flask.render_template('home/about.html')


if __name__ == '__main__':
    app.run(debug=True)

