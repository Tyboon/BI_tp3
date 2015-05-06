#!/usr/bin/python
#-*-coding:utf-8-*

import sys
import random

"""
Module definissant des algorithmes de classification
"""

class KMeans(object) :
    """
    Algorithme du K-Means
    """

    def __init__(self, data, k, distance, factory=None) :
        """
        values : les entrees a traiter
        k : le nombre de clusters souhaite (k > 0)
        distance : la function de distance a utiliser
        """
        self.data = data
        self.k = k
        self.distance = distance
        self.factory = factory
        self.clusters = []
        self.init_clusters()
        '''
        self.min
        self.max
        self.nb_dimension
        '''

    def init_clusters(self) :
        print "Initilalization of", self.k, "clusters..."
        centroids = random.sample(self.data, self.k)
        for centroid in centroids :
            cluster = self.factory.create_cluster(centroid)
            self.clusters.append(cluster)

    def choose_cluster(self, point) :
        min = sys.maxint
        choice = None
        for cluster in self.clusters :
            centroid = cluster.get_centroid()
            dist = self.distance(centroid, point, self.data.get_min(), self.data.get_max())
            if dist < min :
                min = dist
                choice = cluster

        origin = point.get_cluster()
        if origin != choice :
            choice.add_point(point)
            origin.remove_if_present(point)

    def distribute_values(self) :
        print "Begining the distribution of the points..."
        while True :
            for point in self.data :
                self.choose_cluster(point)
            states = map((lambda x: x.has_changed()), self.clusters)
            if not any(states) :
                break
            for cluster in self.clusters :
                cluster.update_centroid()
        print "Finished!"
        print ""

class Cluster(object) :

    def __init__(self, centroid) :
        self.centroid = centroid
        self.points = []
        self.changed = False
        self.nb_points = 0
        self.add_point(centroid)

    def add_point(self, point) :
        if point not in self.pointss :
            self.points.append(point)
            point.set_cluster(self)
            self.nb_points += 1
            self.changed = True
    
    def remove_if_present(self, point) :
        if point == self.centroid :
            raise CannotRemoveTheCentroidError()

        try :
            self.values.remove(point)
            self.nb_points -= 1
            self.changed = True
        except ValueError :
            pass

    def get_centroid(self) :
        return self.centroid

    def update_centroid(self) :
        # TODO to change
        self.centroid = sum(self.points)/len(self.points)
        self.changed = False

    def has_changed(self) :
        return self.changed

class CannotRemoveTheCentroidError(Exception) :
    pass
