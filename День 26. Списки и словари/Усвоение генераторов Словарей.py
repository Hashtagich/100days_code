# Задание №1
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {key: len(key) for key in sentence.split()}
print(result)
# Задание №2
weather_c = {
    'monday': 12,
    'tuesday': 14,
    'wednesday': 15,
    'thursday': 14,
    'friday': 21,
    'saturday': 22,
    'sunday': 24
}


def temp_f(temp):
    return round(((temp * 9 / 5) + 32), 1)


weather_f = {key: temp_f(values) for key, values in weather_c.items()}
print(weather_f)
