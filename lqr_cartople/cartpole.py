import gymnasium as gym
import numpy as np
import scipy
import scipy.linalg
import matplotlib.pyplot as plt
def linearized_init(M, m, l, q1, q2, q3, q4, r):
    '''
    Parameters:
    ----------
    M, m: floats
    masses of the rickshaw and the present
    l : float
    length of the rod
    q1, q2, q3, q4, r : floats
    relative weights of the position and velocity of the rickshaw,
    the angular displacement theta and the change in theta, and the control
    Return
    -------
    A : ndarray of shape (4,4)
    B : ndarray of shape (4,1)
    Q : ndarray of shape (4,4)
    R : ndarray of shape (1,1)
    '''
    g = 9.8
    ### Матрица А с невесомым стержнем
    # A = np.array([[0., 1., 0., 0.],
    #               [0., 0., m*g/M, 0.],
    #               [0., 0., 0., 1.],
    #               [0., 0, g/(M*l)*(M+m), 0.]])
    ### Матрица А с массивным стержнем
    A = np.array([[0., 1., 0., 0.],
                  [0., 0., 3*m*g/(4*M+m), 0.],
                  [0., 0., 0, 1.],
                  [0., 0., 3*g/(2*l)*(1.+(3*m)/(4*M+m)), 0.]])
    # # # Вектор B для невесомого стержня
    # B = np.array([0., 1/M, 0., 1/(M*l)],)
    # # # Вектор B для массивного стержня
    B = np.array([0., 1/(M+m/4), 0., 3/(2*l*(M+m/4))])
    B = B.reshape((4, 1))
    Q = np.diag(np.array([q1, q2, q3, q4]))

    R = np.array([r])
    R = R.reshape((1, 1))
    return A, B, Q, R

def find_P(A, B, Q, R):
    P = scipy.linalg.solve_continuous_are(A, B, Q, R)
    return P

def main():
    env = gym.make('CartPole-v1', render_mode='human')
    observation, info = env.reset()

    #Зададим параметры
    M = env.unwrapped.masscart
    m = env.unwrapped.masspole
    l = env.unwrapped.length * 2
    q1 = 1.
    q2 = 1.
    q3 = 1.
    q4 = 1.
    r = 10
    A, B, Q, R = linearized_init(M, m, l, q1, q2, q3, q4, r)
    P = find_P(A, B, Q, R)
    steps = []
    step = 0
    x_ax = []
    v_ax = []
    angle_ax = []
    psi_ax = []
    u_ax = []
    while True:
        steps.append(step)
        step += 1
        z = observation.copy()
        z[2] = -z[2]
        z[3] = -z[3]
        x_ax.append(z[0])
        v_ax.append(z[1])
        angle_ax.append(z[2])
        psi_ax.append(z[3])
        u = - np.linalg.inv(R)@B.T@P@z
        u_ax.append(u)
        env.unwrapped.force_mag = abs(u[0])
        action = int(np.heaviside(u[0], 0))
        # action = env.action_space.sample()  # agent policy that uses the observation and info
        observation, reward, terminated, truncated, info = env.step(action)
        if terminated or truncated:
            observation, info = env.reset()
            break

    env.close()
    plt.plot(steps, x_ax, label='x')
    plt.plot(steps, v_ax, label='v')
    plt.plot(steps, angle_ax, label=r'$\theta$')
    plt.plot(steps, psi_ax, label=r'$\psi$')
    plt.plot(steps, u_ax, label='u')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()