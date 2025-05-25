import os
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from datetime import datetime, timezone

app = Flask(__name__) #The __name__ represents the current file


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['UPLOAD_FOLDER'] = 'static/uploads'
db = SQLAlchemy(app)

# Model 
class User(db.Model):
    email = db.Column(db.String(120), primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=False)
    # license = db.Column(db.String(120), nullable=False)
    
@app.route('/api/add_user', methods=['POST'])
def add_user():
    email = request.form.get('email')
    name = request.form.get('name')
    phone = request.form.get('phone')
    # license = request.form.get('license')
    age = request.form.get('age') 
    
    db.session.add(User(name=name, age=int(age)))
    db.session.commit()
    return jsonify({'message': f"name :{name} and age: {age} received"})


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/team')
def team():
    return render_template('team.html')
@app.route('/appointment')
def appointment():
    return render_template('appointment.html')


if __name__ == "__main__":
    app.run(debug=True)
    
