import math

class Data(object) :

    def __init_(self) :
        self.points = []
        self.min = None
        self.max = None

    def add_point(self, point) :
        self.points.append(point)
        self.update_min_max(point)

    def update_min_max(self, point) :
        if self.min == None :
            self.min = point

        if self.max == None :
            self.max = point

        for i in range(point.nb_attibutes()) :
            att_min = self.min.get_attribut(i)
            att_max = self.max.get_attribut(i)
            att_point = point.get_attribut(i)

            if att_min.compare(att_point) < 0 :
                self.min.set_attribut(i, att_point)

            if att_max.compare(att_point) > 0 :
                self.max.set_attribut(i, att_point)

class Point(object) :

    def __init__(self, attributes, length) :
        self.attributes = attributes
        self.cluster = None
        self.length = length

    def get_cluster(self) :
        return self.cluster

    def set_cluster(self, cluster) :
        self.cluster = cluster

    def get_attribut(self, i) :
        return self.attributes[i]

    def set_attribute(self, i, att) :
        self.attributes[i] = att

    def nb_attributes(self) :
        return self.length

class Attribute(object) :

    def __init__(self, value) :
        self.value = value

    def compare(self, attribute) :
        raise NotImplementedError()

    def distance(self, attribute, min, max) :
        raise NotImplementedError()

class AttributeNumerical(Attribute) :

    def compare(self, attribute) :
        return self.value - attribute.value

    def distance(self, attribute, min, max) :
        return (self.value - attribute.value) / (max - min)

class AttributeNominal(Attribute) :

    def compare(self, attribute) :
        if self.value != attribute.value :
            return 1
        
        return 0

    def distance(self, attribute, min=None, max=None) :
        if self.value == attribute.value :
            return 0

        return 1

def euclidienne(self, point1, point2, min, max) :
    sum = 0
    dist = 0
    for i in range(point1.nb_attributes()) :
        attr1 = point1.get_attribute(i)
        attr2 = point2.get_attribute(i)
        dist = attr1.distance(attr2, min.get_attribute(i), max.get_attribute(i))
        sum += math.pow(dist, 2)
    return math.sqrt(sum)

def manhattan(self, poin1, point2, min, max, nb_dimention) :
    sum = 0
    dist = 0
    for i in range(nb_dimension) :
        attr1 = point1.get_attribute(i)
        attr2 = point2.get_attribute(i)
        dist = attr1.distance(attr2, min.get_attribute(i), max.get_attribute(i))
        sum += math.fabs(dist)
    return math.sqrt(sum)

