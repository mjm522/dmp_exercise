import numpy as np
import numpy.matlib as npm
from scipy.interpolate import interp1d

def processTrajectory(trajectory , endTime=1.0, timeStep=0.001):

    trajectory = np.vstack([trajectory, npm.repmat(trajectory[-1,:],20,1)])

    dt = timeStep
    
    time_stamps = np.arange(0, endTime, timeStep)

    trajData = np.zeros([time_stamps.shape[0], 3])

    trajData[:,0] = time_stamps
    
    for ID in range(trajectory.shape[1]):
        traj = trajectory[:,ID]
        nsample = np.arange(0.,  len(traj)*dt, dt)
        nnsample = np.arange(0., len(traj)*dt-dt,  (len(traj)*dt-dt) / (1./dt))
        trajData[:,ID+1] = interp1d(nsample, traj)(nnsample)
    
    return trajData

