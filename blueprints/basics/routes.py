from flask import Blueprint, render_template

bp = Blueprint('basics', __name__, template_folder='pages', url_prefix='/basics')


@bp.route('/')
def home():
    return render_template('basics/home.html')


@bp.route('/<page_name>')
def page(page_name):
    return render_template(f'basics/{page_name}.html')
