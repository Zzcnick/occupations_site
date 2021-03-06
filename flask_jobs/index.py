# Occupations Chooser Website

from flask import Flask, render_template, redirect
from utils import profession # Occupation Selector
app = Flask(__name__)

# Website Routes
# ===============================================================
@app.route("/")
def redir():
    return redirect("/occupations/")

@app.route("/occupations/")
def occupations():
    raw_data = profession.parseCSV("data/occupations.csv")
    return render_template(
        "simple_dark.html",
        title="Occupation Randomizer",
        occupation=profession.choose(raw_data),
        data=raw_data
    )

# Prevents following code from running unless it is standalone.
# ===============================================================
if (__name__ == "__main__"):
    app.debug = True # Debugging
    app.run() # Start
    
