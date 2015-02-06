#!/usr/bin/env python3

import sys

# lower-case boolean
bool = lambda s: {'1':'true', '0':'false'}[s]

attribute_names = ['animalname', 'hair', 'feathers', 'eggs', 'milk', 'airborne',
        'aquatic', 'predator', 'toothed', 'backbone', 'breathes', 'venomous',
        'fins', 'legs', 'tail', 'domestic', 'catsize','type']

attribute_types= [str,  bool, bool, bool, bool, bool, bool, bool, bool, bool,
        bool, bool, bool, int, bool, bool, bool, int]

if len(sys.argv) != 2:
    print('Usage:', sys.argv[0], 'in.data > out.csv')
else:
    with open(sys.argv[1]) as f:
        print(','.join(attribute_names))
        for line in f:
            attributes = line.split(',')
            print(','.join(str(f(x)) for f, x in zip(attribute_types, attributes)))
