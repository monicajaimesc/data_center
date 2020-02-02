#!/usr/bin/python3
"""Init the application"""
from flask import Flask, jsonify, render_template
from firebase_admin import credentials, firestore, initialize_app
from models import str_to_number
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'XYZ')
"""cities = [
    "amazonas", "antioquia", "arauca", "atlantico", "bolivar",
    "boyaca", "caldas", "caqueta", "casanare", "cauca",
    "cesar", "choco", "cordoba", "cundinamarca", "huila",
    "magdalena", "meta", "nariño", "putumayo", "quindio",
    "risaralda", "santander", "tolima"
]
"""


@app_views.route('/', strict_slashes=False)
def view_states():
    """
    if request.method == 'GET':
        states_ = storage.all('State')
        state_return = []
        for state in states_.values():
            state_return.append(state.to_dict())
        return jsonify(state_return)

    elif request.method == 'POST':
        data = request.get_json()
        if data is None:
            abort(400, 'Not a JSON')
        if data.get('name') is None:
            abort(400, 'Missing name')
        new_state = State(**data)
        new_state.save()
        return make_response(jsonify(**new_state.to_dict()), 201)
        """
    return "Hello world!"




if __name__ == "__main__":
    app.run(debug=True)