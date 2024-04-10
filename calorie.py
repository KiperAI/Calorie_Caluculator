from temperature import Temperature


class Calorie:
    """
    Represent amount of calories calculated with
    BMR = 10*weight + 6.25*height - 5*age + 5 - 10*temperature

    """
    def __init__(self, weight, height, age, temperature, activity_level):
        self.temperature = temperature
        self.age = age
        self.height = height
        self.weight = weight
        self.activity_level = activity_level

    def calculate(self):
        result = 10 * self.weight + 6.25 * self.height - 5 * self.age + 5 - self.temperature * 10
        activity_factors = {
            'sedentary': 1.2,
            'low': 1.375,
            'moderate': 1.55,
            'high': 1.725,
            'very_high': 1.9
        }
        activity_factor = activity_factors.get(self.activity_level, 1.2)
        total_calories = result * activity_factor
        return total_calories


if __name__ == '__main__':
    temperature = Temperature(country='poland', city='lublin').get()
    calorie = Calorie(temperature=temperature, weight=83, height=180,
                      age=27, activity_level='sedentary')
    print(calorie.calculate())
