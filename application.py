from flask import Flask, render_template, request, redirect
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

@app.route("/")
def index_page():
    """Show an index page."""

    return "<html><body>This is the homepage.</body></html>"

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")

@app.route("/templates/application-form")
def application_form_page():
    """Shows an application form page."""

    return render_template("application-form.html")


@app.route("/application", methods=["POST"])
def submit_form_page():

    first_name = request.form.get("user_firstname")
    last_name = request.form.get("user_lastname")  
    salary_requirements = request.form.get("user_salary")
    job_preference = request.form.get("user_job")

    return render_template("application-response.html",
                            first=first_name,
                            last=last_name,
                            salary=salary_requirements,
                            job=job_preference)

@app.route("/templates/application-response", methods=["GET"])
def application_response_page():

    return render_template("application-response.html")

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0", port=5001)

