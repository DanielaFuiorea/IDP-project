from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/games')
def games():
    return jsonify([
        {"title": "Cyberpunk 2077", "discount": "50%"},
        {"title": "Elden Ring", "discount": "30%"}
    ])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
