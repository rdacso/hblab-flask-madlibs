from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

@app.route('/')
def start_here():
    """Homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user."""

    player = request.args.get("person")

    return render_template("compliment.html",
                           person=player)


@app.route('/game')
def show_madlib_form():
    """Conditional dependant on user's response to  game play."""

    yesno = request.args.get("yesno")

    if yesno == 'yes':

        return render_template("game.html")
    else:

        return render_template("goodbye.html")
    

@app.route('/madlib')
def show_madlib():
    adjective = request.args.get('adjective')
    verbed = request.args.get('verbed')
    nounp = request.args.get('nounp')
    famousperson = request.args.get('famousperson')
    place = request.args.get('place')
    occupation = request.args.get('occupation')
    noun = request.args.get('noun')
    nationality = request.args.get('nationality')
    femalecelebrity = request.args.get('femalecelebrity')
    noun1 = request.args.get('noun1')
    femalefriend = request.args.get('femalefriend')
    nounp1 = request.args.get('nounp1')
    number = request.args.get('number')
    adjective1 = request.args.get('adjective1')

     
    return render_template('gameplay.html', adjective=adjective, verbed=verbed,
    nounp=nounp, famousperson=famousperson, place=place, occupation=occupation,
    noun=noun, nationality=nationality, femalecelebrity=femalecelebrity, noun1=noun1,
    femalefriend=femalefriend, nounp1=nounp1, number=number, adjective1=adjective1)

   

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
