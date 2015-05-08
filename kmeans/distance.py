import math

def euclidienne(point1, point2, min, max, manager) :
    sum = 0
    dist = 0
    names = manager.get_names()
    for name in names :
        attr1 = point1.get_attribute_by_name(name)
        attr2 = point2.get_attribute_by_name(name)
        dist = attr1.distance(attr2, min[name], max[name])
        sum += math.pow(dist, 2)
    return math.sqrt(sum)

def manhattan(point1, point2, min, max, nb_dimention) :
    sum = 0
    dist = 0
    for i in range(nb_dimension) :
        attr1 = point1.get_attribute(i)
        attr2 = point2.get_attribute(i)
        dist = attr1.distance(attr2, min.get_attribute(i), max.get_attribute(i))
        sum += math.fabs(dist)
    return math.sqrt(sum)

