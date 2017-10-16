import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
from dmptest import dmptest
from dmptrain import dmptrain
import matplotlib.pyplot as plt
from createKernelFcn import createKernelFcn
from processTrajectory import processTrajectory

# 1: general dmp formulation
# 2: new dmp formulation with goal change
# 3: add tracking system and phase stopping
exercise_id = 1


################################################ TRAIN ################################################################

trajectory = np.loadtxt('recorded_trajectory.txt')

trajData = processTrajectory(trajectory)

rbf_num = 500
dc = 1. / (rbf_num -1 )
centers = np.arange(1., 0., -dc)[None, :]

paras = {}
paras['kernelfcn'] = createKernelFcn(centers, 1)
paras['D'] = 200
paras['K'] = paras['D']**2./4.
paras['tau'] = 1.
paras['ax'] = -3.
paras['original_scaling'] = trajData[-1,1:] - trajData[1,1:] + 1e-5
Ws = dmptrain(trajData,paras, exercise_id)

################################################ TEST ################################################################

testparas = paras
testparas['dt'] = 0.001

# play with the parameters
start_offset = np.array([0.,0.])
goal_offset = np.array([0.,0.])
speed = 1.
external_force = np.array([0.,0.,0.,0.])
alpha_phaseStop = 20.


testparas['y0'] = trajData[0, 1:] + start_offset
testparas['dy'] = np.array([0., 0.])
testparas['goals'] = trajData[-1,1:]+ goal_offset
testparas['tau'] = 1./speed
testparas['ac'] = alpha_phaseStop

if exercise_id == 3:
    testparas['extForce'] = external_force
else:
    testparas['extForce'] = np.array([0,0,0,0])


testTraj = dmptest(Ws, testparas, exercise_id)


plt.figure(1)
# plt.axis([-2, 2, -2, 2])
plt.plot(trajData[:,1], trajData[:,2], 'b-')
plt.plot(testTraj[:,1], testTraj[:,2], 'r--')

plt.figure(2)
# plt.axis([0, 1, -2, 2])
plt.plot(testTraj[:,0], testTraj[:,1], 'g-')
plt.plot(testTraj[:,0], testTraj[:,2], 'm-')
plt.show()