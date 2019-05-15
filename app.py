from flask import Flask, jsonify

from scraper import get_random_fact

URL = 'https://en.wikipedia.org/wiki/Palmerstown'
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def factoid():
    """
    Fetch a fact about Palmerstown from the Wikipedia article specified in URL and return it as a Google
    DialogFlow response.

    :return: A JSON response of a google DiaglogFlow payload with the fact as the textToSpeech message.
    """
    response = {
        "payload": {
            "google": {
                "expectUserResponse": False,
                "richResponse": {
                    "items": [
                        {
                            "simpleResponse": {
                                "textToSpeech": get_random_fact(url=URL)
                            }
                        }
                    ]
                }
            }
        }
    }
    return jsonify(response)
