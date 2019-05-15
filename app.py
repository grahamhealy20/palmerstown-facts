from flask import Flask, jsonify, request

app = Flask(__name__)

RESPONSE_TEMPLATE = {
    "payload": {
        "google": {
            "expectUserResponse": False,
            "richResponse": {
                "items": [
                    {
                        "simpleResponse": {
                            "textToSpeech": "this is a simple response"
                        }
                    }
                ]
            }
        }
    }
}


@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        data = request.data

    return jsonify(RESPONSE_TEMPLATE)
