import numpy as np


def list_inputs(k):  # (n + 1) pts (x_i,y_i )
    l_x, l_y = [], []
    for _ in range(1, 2 * k + 3):
        if _ % 2 == 1:
            l_x.append(int(input()))
        else:
            l_y.append(int(input()))
    return l_x, l_y


def norm_vector(l1):
    # nv = []
    # for _ in range(0, len(l1) - 1):
    #    if l1[_ + 1] > l1[_]:
    #        nv.append(1)
    #    elif l1[_ + 1] < l1[_]:
    #        nv.append(-1)
    #    else:
    #        nv.append(0)
    # return nv

    nv = [np.sign(l1[_ + 1] - l1[_]) for _ in range(0, len(l1) - 1)]
    return nv


def danger(lx, ly, nx, ny):
    danger_x, danger_y = [], []
    for _ in range(1, len(nx)):
        if nx[_ - 1] * ny[_] == 1 or nx[_] * ny[_ - 1] == -1:
            danger_x.append(lx[_])
            danger_y.append(ly[_])
    return danger_x, danger_y


if __name__ == '__main__':
    n = int(input())
    x, y = list_inputs(n)
    norm_x, norm_y = norm_vector(x), norm_vector(y)
    d_x, d_y = danger(x, y, norm_x, norm_y)
    print(d_x, "\n", d_y)
    print(len(d_x))

# exclude points on the boundaries
'''
def pts_boundary(N, L_x, L_y):
    x_max, y_max = max(L_x), max(L_y)
    x_min, y_min = min(L_x), min(L_y)
    newl_x, newl_y = [], []
    for i in range(0, N + 1):
        if L_x[i] != x_max and L_x[i] != x_min and L_y[i] != y_max and L_y[i] != y_min:
            newl_x.append(l_x[i])
            newl_y.append(l_y[i])
    return newl_x, newl_y
print(n)
print(len(l_x))
l_x_1, l_y_1 = pts_boundary(n, l_x, l_y)
print(l_x_1)
print(l_y_1)
'''
