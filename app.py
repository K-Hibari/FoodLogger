import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finalproject.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show restaurant"""
    # get user restaurant
    restaurants = db.execute(
        "SELECT * FROM restaurant WHERE user_id = :user_id", user_id=session["user_id"])

    if len(restaurants)>0:
        return render_template("index.html", restaurants=restaurants)
    else:
        msg = "--no restaurants rated--"
        return render_template("index.html", msg=msg)


@app.route("/delete", methods=["POST"])
@login_required
def delete():
    """delete restaurant"""
    restaurant_name = request.form.get("restaurant_name").upper()
    db.execute("DELETE FROM restaurant WHERE user_id = ? AND name = ?", session["user_id"], restaurant_name)
    return redirect("/")

@app.route("/add", methods=["GET", "POST"])
@login_required
def add():
    """add restaurant"""
    if request.method == "POST":
        name = request.form.get("name").upper()
        favourite = request.form.get("favourite").upper()
        rating = request.form.get("rating")
        critics = request.form.get("critics")
        location = request.form.get("location")

        if not name:
            return apology("must provide name")
        elif not favourite:
            return apology("please input yes or no to favourite")
        elif not critics:
            return apology("please give your critics")
        elif not location:
            return apology("please provide a location")
        elif not rating or not rating.isdigit() or int(rating) <= 0:
            return apology("must provide a positive integer number for rating")

        # add restaurant to the list
        db.execute("INSERT INTO restaurant (user_id, name, favourite, rating, critics, location) VALUES (:user_id, :name, :favourite, :rating, :critics, :location)",
                   user_id=session["user_id"], name=name, favourite=favourite, rating=rating, critics=critics, location=location)

        flash(f"Added {name} with a rating of {rating}!")
        return redirect("/")
    else:
        return render_template("add.html")



@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    session.clear()

    # reached through post
    if request.method == "POST":

        # ensure username is submitted
        if not request.form.get("username"):
            return apology("must provided username", 400)

        # ensure password provided
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # ensure confirmation is provided
        elif not request.form.get("confirmation"):
            return apology("must confirm password", 400)

        # ensure that password and confirmation match
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("passwords do not match", 400)

        # query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # ensure username does not alreaedy exist
        if len(rows) != 0:
            return apology("username already exist", 400)

        # insert new user
        db.execute("INSERT INTO users (username, hash) VALUES(?, ?)",
                   request.form.get("username"), generate_password_hash(request.form.get("password")))

        # query for new user
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # remember the user
        session["user_id"] = rows[0]["id"]

        # redirect user to homepage
        return redirect("/")

    else:
        return render_template("register.html")


@app.route("/map", methods=["GET"])
@login_required
def map():
    """map"""
    restaurants = db.execute(
        "SELECT * FROM restaurant WHERE user_id = :user_id", user_id=session["user_id"])
    
    return render_template("map.html", restaurants=restaurants)
    
    
