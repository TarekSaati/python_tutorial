import argparse
from oop import Magazine

defaults = {
    'description': ['The Guardian', 25, 'USA'],
    'topics': ['news', 'sports', 'fashion']
    }

parser = argparse.ArgumentParser()

# nargs -> '*'(zero+) or '+'(one+) or '?'(one-opt) or argparse.REMAINDER (all remainings)
parser.add_argument("-d", "--description", nargs=3, help='magazine info: name, page number, origin', default=defaults['description'])

group = parser.add_mutually_exclusive_group()
# a flag option to mark the mag as open or archived
group.add_argument('-o', "--open", action="store_true")
group.add_argument('-r', "--archived", action="store_true")

parser.add_argument("-t", "--topics", nargs='+', help='magazine topics', default=defaults['topics'])

parser.add_argument("-a", "--action", choices=["navigate"], nargs='+', help='select an action: navigate, ...')

parser.add_argument("-p", "--params", nargs='+', help='set the action parameters')



if __name__ == '__main__':
    args = parser.parse_args()
    args = vars(args)
    
    myMag = Magazine(*args['description'], args['topics'])
    print(myMag.name)
    print('bool: ', args['archived'])
    if args['action'] == ['navigate']:
        myMag.navigate(*args['params'])
        print(myMag.currentPage, myMag.currentTopic)
