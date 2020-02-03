#!/usr/bin/python3
"""
this file has the endpoint route for the app
"""

from api.v1.views import app_views
from flask import jsonify
from models import storage

app = Flask(__name__)


# convert as array
states = [
             {"Amazonas", "Antioquia", "Arauca", "Atlantico", "Bolivar", "Boyaca", "Caldas", "Caqueta", "Casanare", "Cauca",
             "Cesar", "Choco", "Cordoba", "Cundinamarca", "Guainia", "Guaviare", "Huila", "Magdalena", "Meta", "Narino",
             "Norte de santander", "Putumayo", "Quindio", "Risaralda", "San andres", "Santander", "Sucre", "Tolima", "Valle del cauca",
             "Vaupes", "Vichada"}]


@app_views.route('/', strict_slashes=False)
def json_status():
    """
    return a json file
    """
    return jsonify({"status": "OK"})


@app_views.route('/states', methods=['GET', 'POST'], strict_slashes=False))
def endpoint_number_objects():
    """
    endpoint that retrieves the number
    of each objects by type:
    param cls: string representing the class name
    return: objects
    """
    object_states = {"Amazonas": "amazonas",
                      "Arauca": "arauca",
                      "Atlantico": "atlantico",
                      "Bolivar": "bolivar",
                      "Boyaca": "boyaca",
                      "caldas": "users"
                      }

    obj_return = {}
    for cls in classes:
        obj_return[object_states[cls]] = storage.count(cls)
    return jsonify(obj_return)


if __name__ == '__main__':
    app.run()