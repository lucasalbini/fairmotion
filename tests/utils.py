# Copyright (c) Facebook, Inc. and its affiliates.

# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import numpy as np
from fairmotion.utils import constants
from fairmotion.utils import conversions


def get_random_Q():
    Q = np.random.rand(4)
    Q = Q / np.linalg.norm(Q)
    return Q


def get_random_R():
    Q = get_random_Q()
    return conversions.Q2R(Q)


def get_random_T():
    R = get_random_R()
    p = np.random.rand(3)
    T = constants.eye_T()
    T[:3, :3] = R
    T[:3, 3] = p
    return T
