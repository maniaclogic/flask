from flask import Flask, request
from app import do_calculation

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main_loop():
    data = request.json
    return do_calculation(data)


if __name__ == '__main__':
    app.run(debug=True)
