import numpy as np
a = np.array([1,2])
b = np.array([2,3])
c = np.array([2,1])
d = np.array([-1,-2])


norm_a=np.linalg.norm(a)
norm_b=np.linalg.norm(b)
norm_c=np.linalg.norm(c)
norm_d=np.linalg.norm(d)

dot_a_b = np.dot(a,b)
dot_b_c = np.dot(b,c)
dot_c_d = np.dot(c,d)
dot_d_a = np.dot(d,a)

print(f"similarity between a and b is : {dot_a_b/(norm_a*norm_b)}")
print(f"similarity between b and c is : {dot_b_c/(norm_b*norm_c)}")
print(f"similarity between c and d is : {dot_c_d/(norm_c*norm_d)}")
print(f"similarity between d and a is : {dot_d_a/(norm_d*norm_a)}")