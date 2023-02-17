travel_log = [
    {"country": 'France',
     'visits': 12,
     'cities': ["Paris", "Lille", "Dijon"]
     },
    {
        "country": 'Germany',
        'visits': 5,
        'cities': ["Berlin", "Hamburg", "Stuttgart"]
    },
]


def add_new_country(country_v, visits_v, cities_v):
    new_conutry = {}
    new_conutry['country'] = country_v
    new_conutry['visits'] = visits_v
    new_conutry['cities'] = cities_v
    print(new_conutry)
    travel_log.append(new_conutry)


add_new_country("Russia", 2, ["Moscow", "S-P"])
print(travel_log)
