#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 15:19:32 2019
@author: jamiehuang
"""


#print(n)
#print(n[0])
#print(n[1])

import json

class jsonformatter:
    def __init__(self):
        self.regions = []
        self.a = {}

    def __repr__(self):
        return json.dumps(self)

    def add_annotation(self, name="-", cx="-", cy="-", rx = "-", ry = "-", theta = "-"):
        new_annotation = Annotation(name, cx, cy, rx, ry, theta)
        self.regions.append(new_annotation)
        return new_annotation
    
    def add_region(self, name='-', type='-', image_quality='-'):
        new_reg = Reg(name, type, image_quality)
        self.regions.append(new_reg)
        return new_reg
    
    def add_a(self):
        new_a = A(self, filename = '-', size = '-', region = '-')
        self.a = {n[8].split('/')[1]: {"filename": n[8].split('/')[1], "size":1785427, "region": self.regions}}
        self.a['file_attributes'] = {'caption': '','public_domain': 'no','image_url': ''}
        return new_a
       
    def save_to_file(self):
        with open("annotated1.txt", 'w') as f:
            f.write(str(self.regions))
 
class A:
    def __init__(self, filename, size, region):
        self.filename = filename
        self.size = size
        self.region = region
        
class Reg:
    def __init__(self, name, type, image_quality):
        self.name = name
        self.type = type
        self.image_quality = image_quality
    
    def __repr__(self):
        return json.dumps({'name': self.name, 'type': self.type, 'image_quality': self.image_quality})

class Annotation:
    def __init__(self, name, cx, cy, rx, ry, theta):
        self.name= name
        self.cx = cx
        self.cy = cy
        self.rx = rx
        self.ry = ry
        self.theta = theta

    def __repr__(self):
        return json.dumps({"name": self.name, "cx": self.cx, "cy": self.cy, "rx": self.rx, "ry": self.ry, "theta": self.theta})

jsonformatter = jsonformatter()
lines_l=[]

with open('/Users/jamiehuang/Documents/Roberts_Lab/Code/annotations1.txt') as f:
    lines = f.readlines()
    
    for line in lines:
        lines_l.append(line)

for i in range(1, len(lines_l)):
    n = lines_l[i].split(' ')
    #print(n)

for i in range(len(lines_l)):
    jsonformatter.add_annotation("ellipse", int(n[0]), int(n[1]), int(n[2]), int(n[3]), 0)
    jsonformatter.add_region('not_defined', 'yes', {'good': True, 'frontal': True, 'good_illumination': True})
    

print({n[8].split('/')[1]: {"filename": n[8].split('/')[1], "size":1785427, "region": regions}})

#'region_attributes': {'name': 'not_defined', 'image_quality': {'good': True, 'frontal': True, 'good_illumination': True}}

jsonformatter.save_to_file()
