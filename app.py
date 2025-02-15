from flask import Flask, render_template, request, jsonify

app = Flask(__name__) #The __name__ represents the current file
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