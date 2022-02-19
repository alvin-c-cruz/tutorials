from flask import Blueprint, render_template

bp = Blueprint('basics', __name__, template_folder='pages', static_folder='static', url_prefix='/basics',
               static_url_path='static')


@bp.route('/')
def home():
    return render_template('basics/home.html')


@bp.route('/<page_name>')
def page(page_name):
    return render_template(f'basics/{page_name}.html')
