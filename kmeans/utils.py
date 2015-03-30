#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class Data(object) :
	'''
	Chargement des données
	'''

	def __init__(self,pathname) :
		'''
		pathname : le fichier d'entrée	
		'''
		self.pathname = pathname
		self.relation = ''
		self.attributs = []
		self.data = []
		self.classe = []

	def opendata(self):
		with open(self.pathname,'r') as f:
			for line in f:
				line = line.lstrip()
				#header
				if line and line[0]=="@" :
					s = line.split()
					if s[0]=='@relation' or s[0]=='@RELATION' :
						self.relation = s[1]
					elif s[0]=='@attribute' or s[0]=='@ATTRIBUTE' :
						if s[1] == 'class' :
							s = s[2][1:len(s[2])-1].split(',')
							for c in s :
								self.classe.append(c)
						elif s[2][1] == '{' :
							t = s[1][1:len(s[1])-2].split(',')
							self.attributs.append((s[1], t))
						else :
							self.attributs.append((s[1],[]))
				elif line and not line[0]=="%":
					line = line.rstrip()
					#on separe les valeurs
					vals = line.split(",")
					#on ajoute a la liste des resultat
					self.data.append(tuple(vals))
			return self.data


if __name__ == "__main__":
	if len(sys.argv)<2:
		print sys.argv[0] + " pathToFile"
	else :
		data = Data('data/iris.arff.txt')
		data.opendata()
		print 'Relation :' + data.relation
		print 'attributs :' 
		print data.attributs
		print 'Classe :'
		print data.classe
		
