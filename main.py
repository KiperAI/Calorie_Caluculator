from flask.views import MethodView
from wtforms import Form, StringField, SubmitField, SelectField
from flask import Flask, render_template, request
from temperature import Temperature
from calorie import Calorie

app = Flask(__name__)


class HomePage(MethodView):

    def get(self):
        return render_template('index.html')


class CalorieFormPage(MethodView):

    def get(self):
        calories_form = CaloriesForm()

        return render_template('calorie_form_page.html',
                               caloriesform=calories_form)

    def post(self):
        calories_form = CaloriesForm(request.form)

        temperature = Temperature(country=calories_form.country.data,
                                  city=calories_form.city.data).get()

        calorie = Calorie(weight=float(calories_form.weight.data),
                          height=float(calories_form.height.data),
                          age=float(calories_form.age.data),
                          temperature=temperature,
                          activity_level=calories_form.activity_level.data)

        calories = calorie.calculate()

        return render_template('calorie_form_page.html',
                               caloriesform=calories_form,
                               calories=calories,
                               result=True)


class CaloriesForm(Form):
    weight = StringField('Weight: ')
    height = StringField('Height: ')
    age = StringField('Age: ')
    country = StringField('Country: ', default='Poland')
    city = StringField('City: ', default='Lublin')
    activity_level = SelectField('Activity Level: ', choices=[
        ('sedentary', 'Sedentary'),
        ('low', 'Low'),
        ('moderate', 'Moderate'),
        ('high', 'High'),
        ('very_high', 'Very High')
    ], default='sedentary')
    button = SubmitField('Calculate')

app.add_url_rule('/',
                view_func=HomePage.as_view('home_page'))
app.add_url_rule('/calorie_form',
                view_func=CalorieFormPage.as_view('calorie_form_page'))

app.run(debug=True)
