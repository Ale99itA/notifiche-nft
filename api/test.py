from flask import Flask

app = Flask(__name__)

@app.route('/api/test', methods=['GET'])
def test():
    return "Test success", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
