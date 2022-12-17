##GTG
from flask import Flask, render_template, request
import vsearch as vs

app = Flask(__name__)

@app.route('/')
@app.route("/entry")
def entry_page() -> 'html':
  return (
    render_template(
      "entry.html",
      the_title="Welcome to search4letters on the web!"
    )
  )
  
@app.route("/search4", methods=["POST"])
def do_search() ->'html':
  phrase = request.form["phrase"]
  letters = request.form["letters"]
  resultSet = vs.search4letters(phrase, letters)
  result = '{' + ", ".join(resultSet)+ '}'

  return (
    render_template(
      "results.html",
      the_title="Here are your results",
      the_phrase=phrase,
      the_letters=letters,
      the_results=result,
    )
  )

if (__name__ == "__main__"):
  app.run(debug=True)

##TYJC
