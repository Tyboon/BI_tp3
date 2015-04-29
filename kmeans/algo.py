#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Point(object) :
	
	def __init__(self,attributs) :
		self.val = attributs
		self.clust = None
		self.dist = None

	def get_cluster(self) :
		return self.clust

	def get_attribut(self, i) :
		return self.val[i]

class Cluster(object) :

	def __init__(self,p) :
		self.centroid = p
		self.points = [p]
		self.min = p
		self.max = p
		self.nb_point = 0

	def add_point(self,point) :
		self.points.add(p)
		self.nb_point += 1

	def rm_point(self,point) :
                # TODO if not present
		self.points.remove(p)
		self.nb_point -= 1

	def min_point(self) :
		self.min = min(self.points)

	def max_point(self) :
		self.max = max(self.points)

	def wc(self) :
		self.wc = 0
		for p in self.points :
			self.wc = distance(p,self.centroid)
		self.wc / self.nb_point

	def update(self) :
		self.min = min_point()
		self.max = max_point()
		self.wc = wc()

class Distance(object) :
	

class Kmeans(object) :
	
	def __init__(self, k) :
		self.clusters = []
		self.k = k

	def launch() :
		
