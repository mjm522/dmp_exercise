import numpy as np
import numpy.matlib as npm

def createKernelFcn(centers, dd):
    
    def Kernel(q):
        D = np.sum( (np.diff(centers,1, axis=1)*0.55)**2, axis=0)
        D = 1./np.hstack([D, D[-1]])
        D = D * dd
        
        res = np.zeros([centers.shape[1], q.shape[1]])
        for i in range(q.shape[1]):
            qq = npm.repmat( q[:,i], 1, centers.shape[1])
            df = np.sum( (qq-centers)**2, axis=0)
            res[:,i] = np.exp( -0.5* np.multiply( np.sum( (qq-centers)**2, axis=0), D))     
        
        return res
    y = Kernel
    
    return y

