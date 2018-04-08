#!/usr/bin/env python

"""
preproc_data.py
Preprocess the data.
"""

__version__     = "0.0.1"
__authors__     = [("David Qiu", "dq@cs.cmu.edu"),
                   ("Karthik Paga", "kpaga@andrew.cmu.edu")]
__copyright__   = "Copyright (C) 2018, Hactauton 2018 Dolan Wins Team. All rights reserved."


import numpy as np

import pdb


def proc_data(fname_in, fname_out):
  """
  Process the data.

  @param fname_in The input file name.
  @param fname_out The output file name.
  @return N The number of items processed.
  """

  N = 0

  # TODO: implementation

  return N


def main():
  fname_in = '../data/driver_behavior.csv'
  fname_out = '' # TODO: output file name

  N = proc_data(fname_in, fname_out)

  print('data has been processed (N=%d)' % (N))
  print('processed data file saved (file: %s)' % (fname_out))


if __name__ == '__main__':
  main()
