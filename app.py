from flask import Flask, render_template

import commande

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/getIsRunning')
def getIsRunning():
    isRunning = commande.getIsRunning()
    print(isRunning)
    return render_template('isRunning.html', isRunning=isRunning)

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
