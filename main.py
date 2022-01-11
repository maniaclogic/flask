from flask import Flask, request
from datetime import datetime
from app import Monday

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def query():
    data = request.args
    if datetime.today().weekday() == 0:
        return Monday()
    elif data:
        return str(data['query'])
    else:
        return "Hello world"


if __name__ == '__main__':
    app.run(debug=True)
