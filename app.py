from flask import Flask, jsonify
import firestore
import firebase_admin
from firebase_admin import credentials

default_app = firebase_admin.initialize_app()
db = firestore.Client()


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/v1')
def my_api():
    return jsonify({'status': 'Bark bark! Ready to roll.'})


@app.route('/v2')
def gcp_api():
    my_quiz = db.collection(u'quiz')
    docs = my_quiz.stream()
    q_one = docs.one.question
    # for doc in docs:
    #     print(f'{doc.id} => {doc.to_dict()}')
    return jsonify(q_one)


# app.run(debug=True)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)content_copy
