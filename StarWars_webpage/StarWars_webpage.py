from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def form_stuff():
    """  """

    return render_template('StarWars_webpage.html')


# @app.route('/', methods=['GET', 'POST'])
# def form_data():
#     return render_template('StarWars_webpage.html', user_name=request.form['user_name'],
#                            user_email=request.form['user_email'],
#                            user_donate_amount=request.form['user_donate_amount'])
#
#
# if __name__ == "__main__":
app.run()
# app.run(host='0.0.0.0', port=8080)
