#!/usr/bin/python

import sys
import random

# place given argument names into list
givers = sys.argv
givers.pop(0)
receivers = []

# create receivers
for person in range(0,len(givers)):
    receivers.insert(person,givers[person])

# shuffle receivers list
random.shuffle(receivers)

# loop through and make sure no one has themselves
for i in range(0,len(givers)):
    if givers[i] == receivers[i]:
        if i == len(givers)-1:
            temp = receivers[i]
            receivers[i] = receivers[0]
            receivers[0] = temp
        else:
            temp = receivers[i+1]
            receivers[i+1] = receivers[i]
            receivers[i] = temp
        

# print files named after who is the giver
for person in range(0,len(givers)):
    f = open(givers[person]+'.txt', 'w')
    f.write('{} is giving a gift to {}'.format(givers[person], receivers[person]))


