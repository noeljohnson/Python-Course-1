from flask import Flask
import vsearch as vs

app = Flask(__name__)

@app.route('/')
def hello() -> str:
  return ("Hello World from Flask")

@app.route("/search4")
def do_search() ->str:
  return (str(vs.search4letters("life, the universe and everything", "eiru")))

app.run()
