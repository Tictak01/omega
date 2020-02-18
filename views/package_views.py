import flask
from omega.infrastructure.view_modifiers import response
import omega.services.package_service as package_service

blueprint = flask.Blueprint('packages', __name__, template_folder='templates')

@blueprint.route('/project/<package_name>')
#@response(template_file='packages/details.html')
def package_details(package_name: str):
    return "Thicc booty {}".format(package_name)

@blueprint.route('/<int:rank>')
def popular(rank: int):
    print(type(rank), rank)
    return "Thicc booty {}".format(rank)

