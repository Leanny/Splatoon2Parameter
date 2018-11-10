import json
from math import isclose, log2
import argparse

with open('parameter.json', 'r') as fp:
    parameters = json.load(fp)

def calcSkillPoint2Percent(points):
    return min(max(0.0, 3.3*points-0.027*points**2), 100.0)
    
def lerpN(slope, percentage):
    if isclose(percentage, 0.0) or not slope >= 0.001:
        return 0.0
    return 1/percentage**(log2(slope))

def get_slope(ability):
    high, mid, low = ability
    if isclose(high, low):
        return 0.0
    return (mid-low)/(high-low)
    
def get_effect(ability, points, ninjasquid = False):
    high, mid, low = ability
    slope = get_slope(ability)
    tmp = calcSkillPoint2Percent(points)
    if ninjasquid:
        tmp *= 0.8 # ninja squid adds percentage penality
    percentage = tmp / 100.0
    result = low + (high - low) * lerpN(slope, percentage)
    if ninjasquid:
        return 0.9 * result # ninja squid reduces speed by 10%
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--parameter', type=int, help='Parameter to calculate, requires a category')
    parser.add_argument('-c', '--category', type=int, help='List parameters under this category or calculate given parameter')
    parser.add_argument('-l', '--list', action='store_true', help='List categories of parameters')
    parser.add_argument('-n', '--ninja-squid', action='store_true', help='Enable ninja squid effect in calculation')
    args = parser.parse_args()
    
    if args.category is not None:
        category_names = sorted([*parameters.keys()])
        assert(0 < args.category <= len(category_names))
        category = category_names[args.category-1]
        parameter_names = sorted([*parameters[category].keys()])

        if args.parameter is not None:
            assert(0 < args.parameter <= len(parameter_names))
            parameter_name = parameter_names[args.parameter - 1]

            print(category, parameter_name, sep=' - ')

            aps = sorted([mains*10 + subs*3 for mains in range(4-int(args.ninja_squid)) for subs in range(10)])
        
            print('{:<10}{:<}'.format('AP','Effect'))
            for ap in aps:
                effect = get_effect(parameters[category][parameter_name], ap, args.ninja_squid)
                print('{:<10}{:05.4f}'.format(str(ap).rjust(2), effect))
        else:
            print('Parameters under', category)
            for i, parameter_name in enumerate(parameter_names):
                print(i + 1, parameter_name)

    elif args.list:
        print('Categories:')
        category_names = sorted([*parameters.keys()])

        for i, category in enumerate(category_names):
            print(i+1, category)
    else:
        parser.print_help()
