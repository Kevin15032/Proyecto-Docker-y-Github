from pydoc import render_doc
from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="db2"
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

@app.route('/')
def index():
    conn = get_db_connection()
    if conn is None:
        return "Error al conectar con la base de datos."

    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students')
    results = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template('index.html', students=results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)