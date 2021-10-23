from sys import argv
import json


script_name, fTests, fValues = argv
id_values_list = {}
with open(fTests, 'r') as f1:
    tests = f1.read()
    testsParsed = json.loads(tests)
with open(fValues, 'r') as f2:
    values = f2.read()
    valuesParsed = json.loads(values)


def find_value_by_id(obj):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if isinstance(v, (dict, list)):
                find_value_by_id(v)
            elif k == 'id':
                id_values_list[v] = obj.get('value')

    elif isinstance(obj, list):
        for v in obj:
            find_value_by_id(v)


def find_empty_in_tests(obj):

    if isinstance(obj, dict):
        for k, v in obj.items():
            if isinstance(v, (dict, list)):
                find_empty_in_tests(v)
            elif k == 'id' and obj.get('value') == '':
                try:
                    obj['value'] = id_values_list[v]
                except KeyError as e:
                    pass
    elif isinstance(obj, list):
        for v in obj:
            find_empty_in_tests(v)


find_value_by_id(valuesParsed)
find_empty_in_tests(testsParsed)
with open('../report.json', 'w') as fp:
    json.dump(testsParsed, fp,  indent=1)
