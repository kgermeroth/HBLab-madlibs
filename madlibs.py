"""A madlib game that compliments its users."""

from random import choice, sample

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]

madlib_list = ['madlib.html', 'madlib1.html', 'madlib2.html']


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliments = sample(AWESOMENESS, 3)

    return render_template("compliment.html",
                           person=player,
                           compliments=compliments)

@app.route('/game')
def show_madlib_form():
    """Show response to if they want to play a game."""
    response = request.args.get("choice")

    if response == "yes":
        return render_template("game.html")
    else:
        return render_template("goodbye.html")

@app.route('/madlib')
def show_madlib():
    """Taking user input and populating madlib"""

    person = request.args.get("person").title()
    colors = request.args.getlist("colors")
    noun = request.args.get("noun")
    adjective = request.args.get("adjective")

    madlib_version = choice(madlib_list)

    last_color = colors.pop()

    if len(colors) == 0:
        color_str = last_color
    elif len(colors) == 1:
        color_str = colors[0] + " and " + last_color
    else:
        color_str = ", ".join(colors)
        color_str += f", and {last_color}"

    return render_template(madlib_version, person=person, color=color_str, noun=noun,
        adjective=adjective)

if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
