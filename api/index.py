from flask import Flask
import random

app = Flask(__name__)

quotes = [
    "Programs must be written for people to read, and only incidentally for machines to execute. – Harold Abelson",
    "Any fool can write code that a computer can understand. Good programmers write code that humans can understand. – Martin Fowler",
    "Before software can be reusable it first has to be usable. – Ralph Johnson",
    "Code is like humor. When you have to explain it, it’s bad. – Cory House",
    "Simplicity is the soul of efficiency. – Austin Freeman",
    "Make it work, make it right, make it fast. – Kent Beck",
    "The best error message is the one that never shows up. – Thomas Fuchs"
]

@app.route('/')
def home():
    return "<h2>Welcome to the Coding Quote API</h2><p>Visit <code>/quote</code> to get a random programming quote.</p>"

@app.route('/quote')
def quote():
    return random.choice(quotes)

if __name__ == '__main__':
    app.run(debug=True)
