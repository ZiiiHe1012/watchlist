from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def hello():
    return "Welcone to my Watchlist!"

@app.route('/user/<name>')
def user_page(name):
    return f'User: {escape(name)}'

@app.route('/test')
def test_for_url():
    print(url_for('hello'))
    print(url_for('user_page', name = 'Alice'))
    print(url_for('user_page', name = 'Bob'))
    print(url_for('test_for_url'))
    print(url_for('test_for_url', num = 2))
    return "Test Page"      
