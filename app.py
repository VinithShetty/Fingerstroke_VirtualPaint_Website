from flask import Flask, render_template
import subprocess


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title='Home Page', content='Welcome to my website!')



@app.route('/run-visual-script', methods=['GET'])
def run_visual_script():
    try:
        result = subprocess.check_output(["python", "visual.py"], stderr=subprocess.STDOUT, universal_newlines=True)
        return result
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output}"

    

if __name__ == '__main__':
    app.run(debug=True)
