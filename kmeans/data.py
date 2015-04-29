import math

class Attribut(object) :

    def __init__(self, type, value) :
        self.type = type # numeric ou nominal
        self.value = value

class Type(object) :

    def distance(self, value1, value2, min=None, max=None) :
        raise NotImplementedError()

class Numeric(Type) :

    def distance(self, value1, value2, min, max) :
        return (value1 - value2) / (max - min)

class Nominal(Type) :

    def distance(self, value1, value2, min=None, max=None) :
        if value1 == value2 :
            return 0
        return 1

class Distance(object) :

    def euclidienne(self, point1, point2, min, max, nb_dimension) :
        sum = 0
        dist = 0
        for i in range(nb_dimension) :
            attr1 = point1.attributs[i]
            attr2 = point2.attributs[i]
            type = attr1.type
            dist = type.distance(attr1,attr2,min,max)
            sum += math.pow( dist, 2)
        return math.sqrt(sum)

    def manhattan(self, poin1, point2, min, max, nb_dimention) :
        sum = 0
        dist = 0
        for i in range(nb_dimension) :
            attr1 = point1.attributs[i]
            attr2 = point2.attributs[i]
            type = attr1.type
            dist = type.distance(attr1,attr2,min,max)
            sum += math.fabs(dist)
        return math.sqrt(sum)

