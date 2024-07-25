from flask import Flask, render_template, abort

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/messages/<int:idx>')
def message(idx):
    messages = ['Flask1', 'Flask2', 'Flask3']
    try:
        return render_template('message.html', message=messages[idx])
    except IndexError:
        abort(404)


if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80)