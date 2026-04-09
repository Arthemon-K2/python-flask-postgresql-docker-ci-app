from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        host=os.environ.get('DB_HOST', 'db'),
        database=os.environ.get('POSTGRES_DB', 'testdb'),
        user=os.environ.get('POSTGRES_USER', 'testuser'),
        password=os.environ.get('POSTGRES_PASSWORD', 'testpassword')
    )

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Flask app! \n"
                               "This app connects to a PostgreSQL database and retrieves data from the 'users' table."})

@app.route("/health")
def health():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT 1;")
        cur.fetchone()
        cur.close()
        conn.close()

        return jsonify({
            "status": "ok",
            "app": "running",
            "database": "connected"
        }), 200
    except Exception as exc:
        return jsonify({
            "status": "error",
            "app": "running",
            "database": "disconnected",
            "details": str(exc)
        }), 500
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)