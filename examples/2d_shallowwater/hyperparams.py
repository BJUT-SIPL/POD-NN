"""Default hyperparameters for 2D inviscid Shallow Water Equations."""

import numpy as np
import tensorflow as tf


HP = {}
HP["mesh_idx"] = ([0], [1, 2], [4, 6, 7])
# Dimension of u(x, t, mu)
HP["n_v"] = len(HP["mesh_idx"][2])
# Time
HP["n_t"] = 1
# Snapshots count
HP["n_s"] = 300
# HP["n_s"] = 100
# POD stopping param
HP["eps"] = 1e-10
# Train/val split
HP["train_val_ratio"] = 0.5
# Deep NN hidden layers topology
HP["h_layers"] = [64, 64]
# Setting up the TF SGD-based optimizer
HP["epochs"] = 200000
HP["lr"] = 0.005
HP["decay"] = 0.
HP["lambda"] = 1e-8
# Frequency of the logger
HP["log_frequency"] = 1000

np.random.seed(1111)
tf.random.set_seed(1111)
