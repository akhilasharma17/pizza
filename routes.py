from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template("home.html")


'''
@app.route('/about')
def aboutpage():
    return render_template("home.html")
'''


# templating with jinja
@app.route('/pizza/<int:id>')
def pizza(id):
    conn = sqlite3.connect('pizza.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Pizza WHERE pizza_id=?", (id,))
    pizza = cursor.fetchone()
    return render_template('pizza.html', pizza=pizza)


if __name__ == "__main__":
    app.run(debug=True)
