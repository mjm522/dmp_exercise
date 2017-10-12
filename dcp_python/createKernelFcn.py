import numpy as np

def createKernelFcn(centers, dd):
    
    def Kernel(q):
        D = np.sum( (np.diff(centers,1,2)*0.55)**2, 1)
        D = 1./[D,D[-1]]
        D = D * dd
        
        res = np.zeros([centers.shape[1], q.shape[1]])
        for i in range(q.shape[1]):
            qq = np.repmat( q[:,i],1, centers.shape[1] )           
            res[:,i] = np.exp( -0.5* np.multiply( np.sum( (qq-centers)**2, 1), D))     
        
    return res
    y = Kernel
    
    return y

