#!/usr/biny/env python

"""
plot_train.py
Plot the learning curve.
"""

__version__     = "0.0.1"
__authors__     = [("David Qiu", "dq@cs.cmu.edu"),
                   ("Karthik Paga", "kpaga@andrew.cmu.edu")]
__copyright__   = "Copyright (C) 2018, Hactauton 2018 Dolan Wins Team. All rights reserved."


import os.path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import pdb


def main():
  fname_train = '../data/value_model_train.log'

  loss_curve = []
  with open(fname_train, 'r') as f:
    while True:
      line = f.readline()
      if line:
        loss_curve.append(float(line))
      else:
        break

  plt.plot([epoch for epoch in range(len(loss_curve))], loss_curve)
  #plt.plot(loss_curve)
  plt.ylabel('loss')
  plt.xlabel('epoch')
  plt.show()


if __name__ == '__main__':
  main()

