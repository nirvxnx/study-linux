from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='db',
                            database='mydatabase',
                            user='user',
                            password='password')
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS visits (id SERIAL PRIMARY KEY, timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP);')
    cur.execute('INSERT INTO visits (timestamp) VALUES (CURRENT_TIMESTAMP);')
    conn.commit()
    cur.execute('SELECT COUNT(*) FROM visits;')
    visit_count = cur.fetchone()
    cur.close()
    conn.close()
    return f"This page has been visited {visit_count[0]} times."

if __name__ == '__main__':
    app.run()
