#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

class Shape:
    def __init__(self,data):
        self.data = data
        self.description = "Calculate area giving {x,y}"
        self.version = "0.1"

    def area(self):
        return {'area': self.data['x'] * self.data['y']}
    
    def setDescription(self,text):
        self.description = text

    def setVersion(self,text):
        self.version = text

        
class Square(Shape):
    def __init__(self,data):
        self.data=data
        self.data['y']=data['x']
