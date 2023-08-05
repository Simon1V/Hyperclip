import numpy as np
import timeit 
import math
import z3 
import torch

def main(): 
	geometry = Geometry() 
	mMetric = geometry.minkowskiMetric(3)	
	
class Geometry: 
	def __init__(self): 
		pass 
		
	def minkowskiMetric(self, dimension:int):
		assert isinstance(dimension, int) and dimension >= 0 
		minkowskiMetric = np.eye(dimension)
		minkowskiMetric[0] = -1
		return minkowskiMetric  
		
	def quadraticForm(self, v:torch.Tensor):
		assert len(v) == 1 
		return np.dot(v[1:],v[1:])- v[0]*v[0]

	def billinearForm(self, u:torch.Tensor, v:torch.Tensor):
		return 0.5 * (quadraticForm(u + v) - quadraticForm(u) - quadraticForm(v)) 

	def hyperbolicDistance(self, u:torch.Tensor, v:torch.Tensor):
		assert u.shape[0] == v.shape[0] 
		return np.arcosh(-billinearForm(u, v))
	
if __name__ == "__main__": 
	main() 

