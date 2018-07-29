import numpy as np

ENV = 'Acrobot-v1'
import gym


class node:

    def __init__(self):
        # self.father_nodes_list = list()
        self.child_nodes_list = list()
        self.action_result_state = list()
        self.level = 10001

    def get_key(num):
        return [-np.pi + 2 * np.pi / 10 * (num % 10), -np.pi + 2 * np.pi / 10 * ((num / 10) % 10),
                -4 * np.pi + 8 * np.pi / 10 * ((num / (10 * 10)) % 10),
                -9 * np.pi + 18 * np.pi / 10 * ((num / (10 * 10 * 10)) % 10)]

    def get_num(dim: list):
        k = int((dim[0] + np.pi - 0.0001) * 10 / (2 * np.pi)) + int(
            (dim[1] + np.pi - 0.0001) * 10 / (2 * np.pi)) * 10 + int(
            (dim[2] + 4 * np.pi - 0.0001) * 10 / (8 * np.pi)) * 100 + int(
            (dim[3] + 9 * np.pi - 0.0001) * 10 / (18 * np.pi)) * 1000
        # if k > 1000:
        #    print("dim", dim)
        # print(k)
        return k


def set_level(node_list: list, base_level):
    print(base_level)
    for t_node in node_list:
        if base_level + 1 < t_node.level:
            t_node.level = base_level + 1
            set_level(t_node.child_nodes_list, t_node.level)


def main():
    env = gym.make(ENV)
    action = env.action_space.n
    env.observation_space
    s_node = list()
    for i in range(10000):
        s_node.append(node())
    count = 0
    env.reset()
    # env.render()
    for i in range(10000):
        for j in range(action):
            # env.render()
            env.set_state(node.get_key(i))
            # env.render()
            s, r, done, info = env.step(j)
            # env.render()
            s_node[i].action_result_state.append(s_node[node.get_num(s)])
            s_node[node.get_num(s)].child_nodes_list.append(s_node[i])
            if done:
                s_node[i].level = 0
                count = count + 1
                # print(count)
            # print(i)
    for i in range(10000):
        if s_node[i].level == 0:
            t_node = s_node[i]
            set_level(t_node.child_nodes_list, 0)
    for i in range(10000):
        if s_node[i].level != 0:
            print(i, s_node[i].level)

    s = env.reset()
    count = 0
    while True:
        min_level = 10002
        min_i = -1
        print(node.get_num(s),s_node[node.get_num(s)].level)
        for i in range(action):
            if s_node[node.get_num(s)].level < min_level:
                min_level = s_node[node.get_num(s)].level
                min_i = i
        s, r, done, info = env.step(min_i)
        env.render()
        count = count + 1
        if done:
            print(count)
            count = 0
            s = env.reset()

    return


if __name__ == "__main__":
    main()
