def describe_city(city_name,city_country='china'):
    """城市所在国家"""
    print(f"{city_name.title()} is in {city_country.title()}")
    
describe_city(city_name='shanghai')
describe_city(city_name='beijing')
describe_city(city_name='tokey',city_country='japan')