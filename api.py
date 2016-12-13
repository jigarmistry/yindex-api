from flask import Flask,jsonify
from spiders.inc_state import get_income_statement_wsj

app = Flask(__name__)


@app.route('/')
def stock_api():
    return 'Stock API'


@app.route('/inc_state/my')
def inc_state_my():
    json = get_income_statement_wsj("MY","7106","quarter")
    return jsonify(json)


if __name__ == "__main__":
    app.run(debug=True)