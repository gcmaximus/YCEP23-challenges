#!/usr/bin/env python3
from flask import Flask, request, render_template, redirect
import os

app = Flask(__name__)

@app.route('/')
def main():
    return redirect('/read')

@app.route('/read', methods=['GET', 'POST'])
def read():
    if request.method == 'GET':
        return render_template('read.html')
    elif request.method == 'POST':
        filename = request.form.get("filename")
        try:
            # print('dirname:     ', os.path.dirname(__file__))
            filename = f'/home/ctf/files/{filename}'
            with open(filename, 'r') as f:
                content = f.read()
                return f'''
                <h1>File Contents:</h1>
                <h2>{content}</h2>'''
            
        except FileNotFoundError:
            return '<h2>File Not Found</h2>'
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)  # modify if needed