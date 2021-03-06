import matplotlib.pyplot as plt
import numpy as np 


#Definimos la función que efectua la transformada rápida de Fourier. Devuelve array con coeff complejos.
def FastFurierT(x):
    N = len(x)
    N_min = min(N, 32)
    
    n = np.arange(N_min)
    k = n[:, None]
    M = np.exp(-2j * np.pi * n * k / N_min)
    X = np.dot(M, x.reshape((N_min, -1)))
    
    while X.shape[0] < N:
        X_even = X[:, :X.shape[1] / 2]
        
        X_odd = X[:, X.shape[1] / 2:]
        
        factor = np.exp(-1j * np.pi * np.arange(X.shape[0])
                        / X.shape[0])[:, None]
        X = np.vstack([X_even + factor * X_odd,
                       X_even - factor * X_odd])

    return X.ravel()




#Definimos la función que efectua la transformada inversa rápida de Fourier. Devuelve array con coeff complejos.
def InverseFastFurierT(x):
    N = len(x)
    N_min = min(N, 32)
    
    n = np.arange(N_min)
    k = n[:, None]
    M = np.exp(2j * np.pi * n * k / N_min)
    X = (1./N)*np.dot(M, x.reshape((N_min, -1)))
    
    while X.shape[0] < N:
        X_even = X[:, :X.shape[1] / 2]
        
        X_odd = X[:, X.shape[1] / 2:]
    
        factor = np.exp(1j * np.pi * np.arange(X.shape[0])
                        / X.shape[0])[:, None]
        X = np.vstack([X_even + factor * X_odd,
                       X_even - factor * X_odd])

    return X.ravel()




plt.plot(X,M)
plt.savefig('imagen.png')
