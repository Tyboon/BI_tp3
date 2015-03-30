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
		self.points = []
		self.min = None
		self.max = None
		self.wc = None
		self.bc = None

	def add_point(self,point) :
		self.points.add(p)

	def rm_point(self,point) :
		self.points.remove(p)

	def min_point(self) :
		return min(self.points)

	def max_point(self) :
		return max(self.points)

	def wc(self) :
		pass

	def bc(self) :


	def update(self) :
		self.min = min_point()
		self.max = max_point()

		

class Distance(object) :

class Kmeans(object) :
	
	def __init__(self, k) :
		self.clusters = []
		self.k = k

	def launch() :
		
