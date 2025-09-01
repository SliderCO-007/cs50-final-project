from flask import Blueprint, render_template

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/')
def home():
    return render_template('index.html')

@main_blueprint.route('/lies')
def lies():
    return render_template('index.html')

@main_blueprint.route('/deception')
def deception():
    return render_template('deception.html')

@main_blueprint.route('/about')
def about():
    return render_template('about.html')