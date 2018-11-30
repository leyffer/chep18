import numpy as np
import pyrapp

import sys
m=int(sys.argv[1])
n=int(sys.argv[2])

np.random.seed(1)

X_fit=sorted(np.random.rand(30, 1)*100)
Y_fit=np.array([(1+x)/(1+x +x**2) for x in X_fit]).ravel()
X=list(np.random.rand(200, 1)*100)
for x in X_fit:
    X.append(x)
X=sorted(X)

R=pyrapp.Rapp(X_fit,Y_fit,order=(m,n))

import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rc('text', usetex = True)
font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 22}
mpl.rc('font', **font)
mpl.style.use('ggplot')

f, ax = plt.subplots(1,1)#,sharex=True, gridspec_kw = {'height_ratios':[3, 1]})

ax.scatter(X_fit,Y_fit, label="Data")
LAB="Rational approx (m={},n ={})".format(m,n)
if n==0:
    LAB="Polynomial approx (m={})".format(m)
ax.plot(X, [R(x) for x in X], "b", label=LAB)
ax.legend(loc=1)
ax.set_ylim((-0.2,1.2))
ax.set_ylabel("f(x)")
ax.set_xlabel("x")
ax.set_xlim((-1,101))

fname='test04_{}_{}.pdf'.format(str(m).zfill(2),n)
plt.savefig(fname)
print("File written to {}".format(fname))
