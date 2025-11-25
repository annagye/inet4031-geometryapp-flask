# INET 4031 Intro to Systems
# Project: Geometry Calculator Web App
# Author: Joe Axberg
# Updated for lab use: 2025

from flask import Flask, request, redirect, url_for
import cylinder
from sphere import Sphere

app = Flask(__name__)

# Home page - choose calculator
@app.route("/", methods=["GET", "POST"])
def mainForm():
    if request.method == "POST":
        sphere_choice = request.form.get("sphere")
        cylinder_choice = request.form.get("cylinder")

        if sphere_choice == "on":
            return redirect(url_for('sphereForm'))
        elif cylinder_choice == "on":
            return redirect(url_for('cylinderForm'))

    # Simple HTML form embedded in the route
    return '''
    <h1>Geometry Calculator</h1>
    <form method="POST">
        <input type="checkbox" name="sphere"> Sphere<br>
        <input type="checkbox" name="cylinder"> Cylinder<br><br>
        <button type="submit">Make Selection</button>
    </form>
    '''

# Cylinder page
@app.route("/cylinder", methods=["GET", "POST"])
def cylinderForm():
    if request.method == "POST":
        radius = request.form.get("rad")
        height = request.form.get("hgt")
        vol = cylinder.volume(int(radius), int(height))
        return f'''
        <h1>Cylinder Volume Calculator</h1>
        <p>Radius: {radius}</p>
        <p>Height: {height}</p>
        <p>Volume: {vol}</p>
        <a href="/">Home</a>
        '''

    return '''
    <h1>Cylinder Volume Calculator</h1>
    <form method="POST">
        <label>Radius:</label>
        <input type="text" name="rad" required><br><br>
        <label>Height:</label>
        <input type="text" name="hgt" required><br><br>
        <button type="submit">Calculate Volume</button>
    </form>
    <a href="/">Home</a>
    '''

# Sphere page
@app.route("/sphere", methods=["GET", "POST"])
def sphereForm():
    if request.method == "POST":
        radius = request.form.get("rad")
        s = Sphere(float(radius))
        vol = s.volume()
        return f'''
        <h1>Sphere Volume Calculator</h1>
        <p>Radius: {radius}</p>
        <p>Volume: {vol}</p>
        <a href="/">Home</a>
        '''

    return '''
    <h1>Sphere Volume Calculator</h1>
    <form method="POST">
        <label>Radius:</label>
        <input type="text" name="rad" required><br><br>
        <button type="submit">Calculate Volume</button>
    </form>
    <a href="/">Home</a>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
