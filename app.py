# flask_web/app.py

from flask import Flask, render_template
app = Flask(__name__, template_folder='src')

@app.route('/')
def hello_world():
    return render_template('index.html')
    # return 'Hey, we have Flask in a Docker container!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
