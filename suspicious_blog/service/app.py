from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/s3cr3t-p4gE-wottt')
def secret():
    return render_template('s3cr3t-p4gE-wottt.html')


if __name__ == "__main__":
    app.run(host='127.0.0.1')    #modify if needed