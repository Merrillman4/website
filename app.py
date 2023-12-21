
from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    portfolio = []
    for dirpath, dirnames, filenames in os.walk('static'):
        for dirname in dirnames:
            photoshoot = {'title': dirname, 'images': []}
            for filename in os.listdir(os.path.join(dirpath, dirname)):
                if filename.endswith('.jpg'):
                    photoshoot['images'].append(filename)
            portfolio.append(photoshoot)
    return render_template('index.html', portfolio=portfolio)

if __name__ == '__main__':
    app.run(debug=True)
