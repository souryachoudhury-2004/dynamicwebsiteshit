from flask import Flask, render_template
import requests

URL_age = "https://api.agify.io/?name="
URL_gender = "https://api.genderize.io?name="

app = Flask(__name__)


@app.route("/<name>")
def home(name):
    age_response = requests.get(url=URL_age+name).json()
    age = age_response["age"]
    print(age)
    gender_response = requests.get(url=URL_gender+name).json()
    gender = gender_response["gender"]
    print(gender)

    return render_template("index.html", person_name=name, person_age=age, person_gender=gender)


if __name__ == "__main__":
    app.run(debug=True)
