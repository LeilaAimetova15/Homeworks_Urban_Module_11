from pprint import pprint
import requests
import inspect

class House:
    def __init__ (self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

h = House('ЖК Высь', 15)

def introspection_info(obj):
    result = []
    result.append(type(obj))
    result.append(obj.__module__)
    for dir_item in inspect.getmembers(obj):
        result.append(dir_item)
    return result

pprint(introspection_info(House))



