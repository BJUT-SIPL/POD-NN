import os
import sys
import time
import pandas as pd
import numpy as np


def create_linear_mesh(x_min, x_max, n_x,
                       y_min=0, y_max=0, n_y=0,
                       z_min=0, z_max=0, n_z=0):
    dim = 1
    n_xyz = n_x

    x = np.linspace(x_min, x_max, n_x).reshape((n_x, 1))

    if n_y > 0:
        dim += 1
        n_xyz *= n_y
        y = np.linspace(y_min, y_max, n_y).reshape((n_y, 1))

        if n_z > 0:
            dim += 1
            n_xyz *= n_z
            z = np.linspace(z_min, z_max, n_z).reshape((n_z, 1))

            X, Y, Z = np.meshgrid(x, y, z)
            Xflat = X.reshape((n_xyz, 1))
            Yflat = Y.reshape((n_xyz, 1))
            Zflat = Z.reshape((n_xyz, 1))
            idx = np.array(range(1, n_xyz + 1)).reshape((n_xyz, 1))
            return np.hstack((idx, Xflat, Yflat, Zflat))

        X, Y = np.meshgrid(x, y)
        Xflat, Yflat = X.reshape((n_xyz, 1)), Y.reshape((n_xyz, 1))
        idx = np.array(range(1, n_xyz + 1)).reshape((n_xyz, 1))
        return np.hstack((idx, Xflat, Yflat))

    idx = np.array(range(1, n_xyz + 1)).reshape((n_xyz, 1))
    return np.hstack((idx, x))


def read_space_sol_input_mesh(n_s, idx, x_u_mesh_path, mu_mesh_path):
    st = time.time()
    print("Loading " + mu_mesh_path + "")
    X_v = np.loadtxt(mu_mesh_path)[:, 0:1]

    print("Loading " + x_u_mesh_path + "")
    x_u_mesh = pd.read_table(x_u_mesh_path,
                             header=None,
                             delim_whitespace=True).to_numpy()
    print(f"Loaded in {time.time() - st} sec.")

    idx_i = idx[0]
    idx_x = idx[1]
    idx_u = idx[2]
    n_xyz = int(x_u_mesh.shape[0] / n_s)
    x_mesh = x_u_mesh[:n_xyz, idx_i + idx_x]
    u_mesh = x_u_mesh[:, idx_u]

    return x_mesh, u_mesh, X_v


if __name__ == "__main__":
    print(create_linear_mesh(0, 1, 10))
    print(create_linear_mesh(0, 1, 10, 1, 2, 5))
    print(create_linear_mesh(0, 1, 2, 1, 2, 5, 2, 3, 3))
