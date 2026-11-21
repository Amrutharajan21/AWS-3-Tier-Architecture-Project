
import os
from flask import Flask, request, jsonify
import pymysql

app = Flask(__name__)

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER", "admin"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME", "feedbackdb"),
    "cursorclass": pymysql.cursors.DictCursor
}

@app.route("/")
def health():
    return jsonify({"status": "Flask is running"})

@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()

    try:
        conn = pymysql.connect(**DB_CONFIG)
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO feedback (name, email, feedback) VALUES (%s, %s, %s)",
                (data["name"], data["email"], data["feedback"])
            )
        conn.commit()
        conn.close()

        return jsonify({"message": "Feedback submitted successfully!"})

    except Exception as e:
        return jsonify({"error": "Unable to submit feedback"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
