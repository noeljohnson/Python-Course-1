##GTG
from flask import Flask, render_template, request, escape
import vsearch as vs

app = Flask(__name__)

def logger(req: "flask_request", res: str) -> None:
  with open("vsearch.log", 'a') as log:
    print(request.remote_addr, request.user_agent, request.form, res, sep='|', file=log)

@app.route('/')
@app.route("/entry")
def entry_page() -> "html":
  return (
    render_template(
      "entry.html",
      the_title="Welcome to search4letters on the web!"
    )
  )
  
@app.route("/search4", methods=["POST"])
def do_search() ->"html":
  phrase = request.form["phrase"]
  letters = request.form["letters"]
  resultSet = vs.search4letters(phrase, letters)
  result = '{' + ", ".join(resultSet)+ '}'
  logger(request, result)

  return (
    render_template(
      "results.html",
      the_title="Here are your results",
      the_phrase=phrase,
      the_letters=letters,
      the_results=result,
    )
  )

@app.route("/viewlog")
def read_log() -> str:
  log = '['
  with open("vsearch.log") as logStream:
    for lines in logStream:
      log += '[' + ', '.join(lines.split('|')) + "]," 
  log = log[:-1] + ']'
  return(escape(log))

if (__name__ == "__main__"):
  app.run(debug=True)

##TYJC
