import json

def sum_product(json_file):
    with open(json_file, 'r') as k:
        dat = json.load(k)

    total_sum = 0
    for item in dat:
        score = item['score']
        weight = item['weight']
        product = score * weight
        total_sum += product

    return total_sum

