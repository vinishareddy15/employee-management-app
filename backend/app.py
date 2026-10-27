from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route("/")
def home():
    conn = psycopg2.connect(
        host="employee-db.co5ccquga9v4.us-east-1.rds.amazonaws.com",
        database="employee_db",
        user="postgres",
        password="Devops1234"
    )

    cur = conn.cursor()
    cur.execute("SELECT * FROM employees")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return str(rows)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
