#!/usr/bin/python
#-*-coding:utf-8-*

import sys
import random

from data import *

"""
Module definissant des algorithmes de classification
"""

class KMeans(object) :
    """
    Algorithme du K-Means
    """

    def __init__(self, data, k, distance) :
        """
        values : les entrees a traiter
        k : le nombre de clusters souhaite (k > 0)
        distance : la function de distance a utiliser
        """
        self.data = data
        self.manager = data.get_manager()
        self.k = k
        self.distance = distance
        self.clusters = []
        self.min = dict()
        self.max = dict()
        self.init_clusters()
        self.init_min_max()
        '''
        self.min
        self.max
        self.nb_dimension
        '''

    def init_clusters(self) :
        print "Initilalization of", self.k, "clusters..."
        centroids = random.sample(self.data.get_points(), self.k)
        for centroid in centroids :
            cluster = Cluster(centroid, self.manager)
            self.clusters.append(cluster)

    def init_min_max(self) :
        names = self.manager.get_names()
        points = self.data.get_points()
        for name in names :
            attribute = points[0].get_attribute_by_name(name)
            self.min[name] = attribute.get_value()
            self.max[name] = attribute.get_value()
            for point in points :
                attribute = point.get_attribute_by_name(name)
                if self.min[name] > attribute.get_value():
                    self.min[name] = attribute.get_value()
                if self.max[name] < attribute.get_value():
                    self.max[name] = attribute.get_value()
            

    def choose_cluster(self, point) :
        min = sys.maxint
        choice = None
        for cluster in self.clusters :
            centroid = cluster.get_centroid()
            dist = self.distance(centroid, point, self.min, self.max, self.manager)
            if dist < min :
                min = dist
                choice = cluster

        origin = point.get_cluster()
        if origin != choice :
            choice.add_point(point)
            try :
                origin.remove_if_present(point)
            except :
                pass

    def distribute_values(self) :
        print "Begining the distribution of the points..."
        while True :
            for point in self.data.get_points() :
                self.choose_cluster(point)
            states = map((lambda x: x.has_changed()), self.clusters)
            if not any(states) :
                break
            for cluster in self.clusters :
                cluster.update_centroid()
        print "Finished!"
        print ""
        print self.min
        print self.max
        for cluster in self.clusters :
            print "-------------------------------------"
            print "Centroid: ", cluster.get_centroid()
            for point in cluster.get_points() :
                print point

class Cluster(object) :

    def __init__(self, centroid, manager) :
        self.data = Data(manager)
        self.manager = manager
        self.centroid = centroid
        self.changed = False
        self.normalizer = Normalizer(manager)
        self.add_point(centroid)

    def get_points(self) :
        return self.data.get_points()

    def add_point(self, point) :
        self.data.add_point(point)
        self.normalizer.update_adding(point)
        point.set_cluster(self)
        self.changed = True
    
    def remove_if_present(self, point) :
        if point == self.centroid :
            raise CannotRemoveTheCentroidError()

        try :
            self.data.remove_point(point)
            self.normalizer.update_removing(point)
            self.changed = True
        except ValueError :
            pass

    def get_centroid(self) :
        return self.centroid

    def update_centroid(self) :
        names = self.manager.get_names()
        point = Point()
        nb_points = self.data.get_nb_points()
        for name in names :
            total = self.normalizer.get_sum_of(name)
            mean = total / nb_points
            attribute = AttributeNumerical(mean)
            point.add_attribute_named(attribute, name)
        self.centroid = point
        self.changed = False

    def has_changed(self) :
        return self.changed

class Normalizer(object) :

    def __init__(self, manager) :
        self.manager = manager
        self.sum = dict()
        self.initialize()

    def initialize(self) :
        names = self.manager.get_names()
        for name in names :
            self.sum[name] = 0

    def get_sum_of(self, name) :
        return self.sum[name]

    def update_adding(self, point) :
        self.update_adding_sum(point)

    def update_removing(self, point) :
        self.update_removing_sum(point)

    def update_adding_sum(self, point) :
        names = self.manager.get_names()
        for name in names :
            attribute = point.get_attribute_by_name(name)
            self.sum[name] += attribute.get_value()

    def update_removing_sum(self, point) :
        names = self.manager.get_names()
        for name in names :
            attribute = point.get_attribute_by_name(name)
            self.sum[name] -= attribute.get_value()

class CannotRemoveTheCentroidError(Exception) :
    pass
