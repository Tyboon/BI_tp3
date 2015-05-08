# -*- coding: utf-8 -*-

import math

class Data(object) :

    def __init__(self, manager) :
        self.manager = manager
        self.points = []
        self.nb_points = 0
    
    def get_manager(self) :
        return self.manager
    
    def get_points(self) :
        return self.points
    
    def get_nb_points(self) :
        return self.nb_points

    def add_point(self, point) :
        if point not in self.points :
            self.points.append(point)
            self.nb_points += 1

    def remove_point(self, point) :
        self.points.remove(point)
        self.nb_points -= 1

class Point(object) :

    def __init__(self) :
        self.attributes = dict()
        self.cluster = None
        self.length = 0

    def get_attribute_by_name(self, name) :
        return self.attributes[name]

    def add_attribute_named(self, attribute, name) :
        self.attributes[name] = attribute
        self.length += 1

    def get_cluster(self) :
        return self.cluster

    def set_cluster(self, cluster) :
        self.cluster = cluster

    def nb_attributes(self) :
        return self.length

    def __str__(self) :
        res = "{"
        for key in self.attributes :
            res += str(key)
            res += ": "
            res += str(self.attributes[key])
            res += ", "
        res += "}"
        return res

class AttributeManager(object) :

    def __init__(self) :
        self.names = []
        self.attributes = dict()
        self.nb_attributes = 0

    def get_names(self) :
        return self.names

    def get_nb_attributes(self) :
        return self.nb_attributes

    def add_attribute(self, name, values=None) :
        self.names.append(name)
        self.attributes[name] = values
        self.nb_attributes += 1

class Attribute(object) :

    def __init__(self, value) :
        self.value = value

    def get_value(self) :
        return self.value

    def compare(self, attribute) :
        raise NotImplementedError()

    def distance(self, attribute, min, max) :
        raise NotImplementedError()

    def is_countable(self) :
        return False

    def __str__(self) :
        return str(self.value)

class AttributeCountable(Attribute) :

    def is_countable(self) :
        return True

class AttributeNumerical(AttributeCountable) :

    def compare(self, attribute) :
        return self.value - attribute.value

    def distance(self, attribute, min, max) :
        return (self.value - attribute.value) / (max - min)

class AttributeNominal(Attribute) :

    def distance(self, attribute, min=None, max=None) :
        if self.value == attribute.value :
            return 0
        return 1
