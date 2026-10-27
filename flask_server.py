from flask import Flask, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "change-this-to-something-random-later"

@app.before_request
def log_request():
    print(f"REQUEST: {request.method} {request.path}")
    print(f"COOKIES: {request.cookies}")

@app.route("/")
def home():
    name = request.args.get("name")
    if name:
        session["username"] = name
        return f"<h1>Logged in as {name}.</h1><p><a href='/logout'>Log out</a></p>"
    elif "username" in session:
        return f"<h1>Welcome back, {session['username']}!</h1><p><a href='/logout'>Log out</a></p>"
    else:
        return "<h1>Hello, stranger.</h1><p>Visit /?name=YOURNAME to log in.</p>"

@app.route("/logout")
def logout():
    session.pop("username", None)
    return "<h1>Logged out.</h1><p><a href='/'>Back home</a></p>"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
