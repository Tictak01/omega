import flask
from omega.infrastructure.view_modifiers import response
import omega.services.package_service as package_service

blueprint = flask.Blueprint('home', __name__, template_folder='templates')

@blueprint.route('/')
@response(template_file='home/index.html')
def index():
    return {'packages': package_service.get_details()}
    #return flask.render_template('home/index.html', packages=get_details())

@blueprint.route('/about')
@response(template_file='home/about.html')
def about():
    return {}#flask.render_template('home/about.html')