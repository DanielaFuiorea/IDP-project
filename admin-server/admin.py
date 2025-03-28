from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/admin/update', methods=['POST'])
def update_game():
    data = request.json
    return jsonify({"message": f"Updated {data['title']} with {data['discount']} discount."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
