def make_car(manufacturing, type, **car_info):
    car_info['manufacturing'] = manufacturing
    car_info['type'] = type
    return car_info

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)