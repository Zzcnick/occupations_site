# Occupations Chooser Website

import profession # Occupation Selector
from flask import Flask, render_template, redirect
app = Flask(__name__)

# Website Routes
# ===============================================================
@app.route("/")
def redir():
    return redirect("/occupations")

@app.route("/occupations")
def occupations():
    return render_template(
        "simple_dark.html",
        title="Occupation Randomizer",
        occupation=profession.choose(profession.parseCSV("occupations.csv"))
    )

# Prevents following code from running unless it is standalone.
# ===============================================================
if (__name__ == "__main__"):
    app.debug = True # Debugging
    app.run() # Start
    
