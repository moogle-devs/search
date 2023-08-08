from flask import Flask, render_template, redirect, request
from json import loads

app = Flask(__name__)
with open("sites.json") as file:
  sites = loads(file.read())

@app.route('/')
def index():
  return redirect("https://m00gle.repl.co/")

app.run("0.0.0.0", port=81)
