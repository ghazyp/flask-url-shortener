from flask import Flask, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
import random
import string

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    short = db.Column(db.String(10), unique=True, nullable=False)
    long = db.Column(db.String(500), nullable=False)
    clicks = db.Column(db.Integer, default=0)

def generate_short_url():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

@app.route('/')
def home():
    return "Welcome to the URL Shortener! Use POST /shorten to shorten a URL."

@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.json
    long_url = data.get("url")
    short_url = generate_short_url()
    new_entry = URL(short=short_url, long=long_url)
    db.session.add(new_entry)
    db.session.commit()
    return jsonify({"short_url": f"http://localhost:5000/{short_url}"}), 201

@app.route('/<short>')
def redirect_url(short):
    url_entry = URL.query.filter_by(short=short).first()
    if url_entry:
        url_entry.clicks += 1
        db.session.commit()
        return redirect(url_entry.long)
    return "URL not found", 404

if __name__ == '__main__':
    with app.app_context():  # <-- This ensures an application context is active
        db.create_all()
    app.run(debug=True)
