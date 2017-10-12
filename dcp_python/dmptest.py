import numpy as np

def dmptest(w, paras):
    global exercise_id

    kernelfcn = paras['kernelfcn']
    goals = paras['goals']
    tau = paras['tau']
    dt = paras['dt']
    K = paras['K']
    D = paras['D']
    y = paras['y0']
    dy = paras['dy']

    if not ('extForce' in  paras.keys()):
        extForce = np.array([0,0,0,0])
    else
        extForce = paras['extForce']

    u = 1
    ax = paras['ax']

    id = 1
    yreal = y
    dyreal = dy
    Y[id,:] = yreal
    timestamps[id] = 0
    t = 0
    while u > 1e-3:
        id = id + 1
        kf = kernelfcn(u)
        forces = w.T * kf / np.sum(kf)

        if  exercise_id == 1:
            scaling = np.multiply((goals - paras['y0']), 1./paras['original_scaling'])
            ddy = K * (goals - y) - D * dy + np.multiply(scaling, forces.T) * u
        elif  exercise_id == 2 or exercise_id == 3:
            scaling = goals - paras['y0']
            ddy = K * (goals - y) - D * dy - K * scaling * u + K * forces.T * u
        
        # Euler Method
        dy = dy + dt * ddy/tau
        y = y + dy * dt/tau

        if  exercise_id == 1 or exercise_id == 2:
            Y[id,:] = y
        elif  exercise_id == 3:
            Ky = 300
            Dy = np.sqrt(4*Ky)
            ddyreal = Ky * (y - yreal) - Dy * dyreal
            if (timestamps[id-1] >= extForce[1]) and (timestamps[id-1] < extForce[1] + extForce[2]):
                ddyreal = ddyreal + extForce[3:]
            
            dyreal = dyreal + ddyreal * dt
            yreal = yreal + dyreal * dt
            Y[id,:] = yreal
        
        #canonical system
        if  exercise_id == 1 or exercise_id == 2:
            u = u + 1/tau * ax * u * dt
        elif  exercise_id == 3:
            phasestop = 1 + paras['ac'] * np.sqrt(np.sum((yreal - y)**2))
            u = u + 1/tau * ax * u * dt / phasestop

        t = t + dt
        timestamps[id] = t

    traj = [timestamps.T,Y]

    return traj
