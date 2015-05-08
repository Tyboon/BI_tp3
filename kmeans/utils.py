#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from kmeans import *
from data import *
from distance import *

def opendata(pathname):
    relation = None
    classe = []
    attributs = []


    manager = AttributeManager()
    data = Data(manager)
    with open(pathname,'r') as f:
        for line in f:
            line = line.lstrip()
            #header
            if line and line[0]=="@" :
                s = line.split()
                if s[0]=='@relation' or s[0]=='@RELATION' :
                    relation = s[1]
                elif s[0]=='@attribute' or s[0]=='@ATTRIBUTE' :
                    if s[1] == 'class' :
                        s = s[2][1:len(s[2])-1].split(',')
                        for c in s :
                            classe.append(c)
                    elif s[2][1] == '{' :
                        t = s[1][1:len(s[1])-2].split(',')
                        attributs.append((s[1], t))
                    else :
                        manager.add_attribute(s[1])
            elif line and not line[0]=="%":
                line = line.rstrip()
                #on separe les valeurs
                vals = line.split(",")
                #on ajoute a la liste des resultat
                point = Point()
                names = manager.get_names()
                for i in range(manager.get_nb_attributes()) :
                    attribute = AttributeNumerical(float(vals[i]))
                    point.add_attribute_named(attribute, names[i])
                data.add_point(point)
        return data


if __name__ == "__main__":
    if len(sys.argv) < 2 :
        print sys.argv[0] + " pathToFile"
    else :
        data = opendata('data/iris.arff.txt')
#print 'Relation :' + relation
#print 'attributs :'
#print data.attributs
#print 'Classe :'
#print data.classe
        kmeans = KMeans(data, 3, euclidienne)
        kmeans.distribute_values()
