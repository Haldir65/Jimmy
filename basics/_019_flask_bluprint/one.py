from flask import Blueprint, render_template, abort,Flask
from jinja2 import TemplateNotFound

simple_page = Blueprint('simple_page', __name__,
                        template_folder='templates')

@simple_page.route('/', defaults={'page': 'index'})
@simple_page.route('/<page>')
def show(page):
    try:
        # return render_template('pages/%s.html' % page)
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)

def main():
    app = Flask(__name__)
    app.register_blueprint(simple_page,url_prefix='/pages')
    app.run(debug=True,port=9876)

if __name__ == '__main__':
    main()        