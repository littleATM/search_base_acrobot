import numpy as np

ENV = 'Acrobot-v1'
import gym


class node:

    def __init__(self):
        self.father_nodes_list = list()
        self.action_dis = [-1] * 3
        self.action_state = [-1] * 3

    def get_key(num):
        return [-np.pi + 2 * np.pi / 10 * (num % 10), -np.pi + 2 * np.pi / 10 * ((num / 10) % 10),
                -4 * np.pi + 8 * np.pi / 10 * ((num / (10 * 10)) % 10),
                -9 * np.pi + 18 * np.pi / 10 * ((num / (10 * 10 * 10)) % 10)]

    def get_num(dim: list):
        k = int((dim[0] + np.pi-0.0001) * 10 / (2 * np.pi)) + int((dim[1] + np.pi-0.0001) * 10 / (2 * np.pi)) * 10 + int(
            (dim[2] + 4 * np.pi-0.0001) * 10 / (8 * np.pi)) * 100 + int((dim[3] + 9 * np.pi-0.0001) * 10 / (18 * np.pi)) * 1000
        if k > 1000:
            print("dim", dim)
        print(k)
        return k


def main():
    env = gym.make(ENV)
    action = env.action_space.n
    env.observation_space
    s_node = list()
    for i in range(10000):
        s_node.append(node())
    count = 0
    env.reset()
    env.render()
    for i in range(10000):
        for j in range(action):
            env.render()
            env.set_state(node.get_key(i))
            env.render()
            s, r, done, info = env.step(j)
            env.render()
            s_node[i].action_state[j] = node.get_num(s)
            s_node[node.get_num(s)].father_nodes_list.append(i)
            if done:
                s_node[i].action_dis[j] = 0
                count = count + 1
                print(count)

    return


if __name__ == "__main__":
    main()
