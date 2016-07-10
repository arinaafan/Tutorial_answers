# Module 6
#
# 1. Import the numpy package under the name np
import numpy as np
# 2. Convert a list of numbers (5 elements) to a numpy array
my_array = np.array([1, 2, 3, 4, 5], float)
# 3. Convert a numpy array to a list
my_array.tolist() # ==> [1.0, 2.0, 3.0, 4.0, 5.0]
# 4. Create two numpy arrays of the same length and apply following mathematical operations: +,*,-,/,%
my_array2 = np.array([10, 20, 30, 40, 50], float)
my_array + my_array2 # ==> array([ 11.,  22.,  33.,  44.,  55.])
my_array * my_array2 # ==> array([  10.,   40.,   90.,  160.,  250.])
my_array - my_array2 # ==> array([ -9., -18., -27., -36., -45.])
my_array / my_array2 # ==> array([ 0.1,  0.1,  0.1,  0.1,  0.1])
my_array % my_array2 # ==> array([ 1.,  2.,  3.,  4.,  5.])
# 5. Create a null vector of size 10 but the fifth value which is 1 *
null_vect = np.zeros(10)
null_vect[4] = 1
# 6. Create a vector with values ranging from 10 to 99 *
my_vect = np.arange(10, 100)
# 7. Create a 3x3 matrix with values ranging from 0 to 8 *
my_matrix = np.array(range(9), float).reshape((3, 3))
# 8. Find indices of non-zero elements from [1,2,0,0,4,0] *
print np.nonzero([1,2,0,0,4,0]) # ==> (array([0, 1, 4]),)
# 9. Declare a 10x10x10 array with random values *
my_matrix = np.random.random((10,10,10))
# 10. Normalize a 5x5 random matrix (between 0 and 1) *
Z = np.random.random((5,5))
Zmax,Zmin = Z.max(), Z.min()
Z = (Z - Zmin)/(Zmax - Zmin)
# 11. Multiply a 5x3 matrix by a 3x2 matrix (real matrix product) *
Z = np.dot(np.ones((5,3)), np.ones((3,2)))
# 12. Create a random vector of size 1000 and find the mean value *
my_matrix = np.random.random(1000)
my_matrix.mean()
# 13. Create two numpy arrays and apply following correlation functions: Pearson r, Spearman rho, Kendall tau
np.corrcoef(my_array, my_array2)[0, 1] # ==> 1.0
import scipy.stats.stats
scipy.stats.pearsonr(my_array, my_array2) # ==> (1.0, 0.0)
scipy.stats.spearmanr(my_array, my_array2) # ==> (1.0, 0.0)
scipy.stats.kendalltau(my_array, my_array2) # ==> (0.99999999999999978, 0.014305881024332568)

