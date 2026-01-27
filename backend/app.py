from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2
import os

app = Flask(__name__)
CORS(app)

DB_HOST = os.environ.get("DB_HOST")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")

def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )

@app.route("/add", methods=["POST"])
def add_message():
    data = request.json
    message = data.get("message")

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO messages (content) VALUES (%s)", (message,))
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"status": "Message added"})

@app.route("/messages", methods=["GET"])
def get_messages():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT content FROM messages")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    return jsonify([row[0] for row in rows])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
