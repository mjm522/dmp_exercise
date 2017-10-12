import numpy as np
import numpy as np

def dmptrain( trajData ,paras):
    global exercise_id

    kernelfcn = paras['kernelfcn']
    K = paras['K']
    D = paras['D']
    tau = paras['tau']
    ax = paras['ax']

    timestamp = trajData[:,1]
    dt = timestamp[2] - timestamp[1]

    # canonical system
    x = np.zeros([1, trajData.shape[0]])
    x[1] = 1
    # 1: Euler solution to exponential decreased canonical system
    for i in range(2, len(x)):
        x[i] = x[i-1] + 1/tau * ax * x[i-1] * dt 

    # calculate weights directly
    phi = kernelfcn(x)
    w = zeros([phi.shape[0], trajData.shape[1]-1])
    deno = np.sum(phi, axis=1)

    Y = trajData[:, 2:]
    goals = Y[-1,:].T
    Yd = np.hstack([np.zeros([1,Y.shape[1]]), np.diff(Y)/dt])
    Ydd = np.hstack([np.zeros([1,Yd.shape[1]]), np.diff(Yd)/dt])

    for i in range(2, trajData.shape[1]):

        if  exercise_id == 1:
            y = -K * (goals[i-1] - Y[:,i-1]) + D * Yd[:,i-1] + tau * Ydd[:,i-1]
        elif  exercise_id == 2 or exercise_id == 3:
            y = (tau * Ydd[:,i-1] + D * Yd[:,i-1])/K - (goals[i-1] - Y[:,i-1]) + (goals[i-1] - Y[1,i-1]) * x.T
         
         y = np.multiply(y, 1./(x.T))
         nume = phi * y
         wi = np.multiply(nume , 1./ (deno + 1e-6))
         w[:,i-1] = wi

    return w