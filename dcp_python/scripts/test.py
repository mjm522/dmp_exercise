import matplotlib.pyplot as plt

global exercise_id

testparas = paras
testparas.dt = 0.001

# play with the parameters
start_offset = [0,0]
goal_offset = [0,0]
speed = 1
external_force = [0,0,0,0]
alpha_phaseStop = 20


testparas.y0 = trajData[1,2:] + start_offset
testparas.dy = [0,0]
testparas.goals = trajData[end,2:]+ goal_offset
testparas.tau = 1/speed
testparas.ac = alpha_phaseStop

if exercise_id == 3:
    testparas.extForce = external_force
else:
    testparas.extForce = [0,0,0,0]


testTraj = dmptest(Ws, testparas)

plt.figure(1)
plt.axis([-2 2 -2 2])
plt.plot(trajData(:,2), trajData(:,3), 'b-')
plt.plot(testTraj(:,2), testTraj(:,3), 'r--')

plt.figure(2)
plt.axis([0 1 -2 2])
plt.plot(testTraj(:,1), testTraj(:,2), 'g-')
plt.plot(testTraj(:,1), testTraj(:,3), 'm-')
plt.show()