from flask import Flask, jsonify
import firebase_admin
from firebase_admin import credentials
from google.cloud import firestore

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
    my_quiz = db.collection(u'quiz').document(u'one')
    doc = [(my_quiz.get()).to_dict()]
    quiz_all = db.collection(u'quiz')
    docs = quiz_all.stream()
    collection=[]
    for doc in docs:
        collection.append(doc.to_dict())
    return jsonify(collection)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
