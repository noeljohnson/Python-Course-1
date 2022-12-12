<!--GTG-->
from flask import Flask, render_template
import vsearch as vs

app = Flask(__name__)

@app.route('/')
def hello() -> str:
  return ("Hello World from Flask")

@app.route("/entry")
def entry_page() -> str: #html string
  return (
    render_template(
      "entry.html",
      the_title="Welcome to search4letters on the web!"
    )
  )
  
@app.route("/search4")
def do_search() ->str:
  return (str(vs.search4letters("life, the universe and everything", "eiru")))

app.run()
<!--TYJC-->
