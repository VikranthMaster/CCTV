from flask import Flask, render_template
#In raspi do this from gpiozero import CPUTemperature()
#cpu = CPUTemperature()
#cpu.temperature

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/temperature")
def temperature():
    return render_template('temperature.html')

@app.route("/stairs")
def stairs():
    return render_template('stairs.html')

app.run(debug=True)