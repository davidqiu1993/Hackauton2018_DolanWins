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


def proc_data(fname_in, fname_out_info, fname_out_env, fname_out_drv):
  """
  Process the data.

  @param fname_in The input file name.
  @param fname_out_info The info data file name.
  @param fname_out_env The environment data file name.
  @param fname_out_drv The driver data file name.
  @return N The number of items processed.
  """

  N = 0

  fields_info = [('rawdata_id', 1, 'id'), 
                 ('vehicle_id', 2, 'id'), 
                 ('driver_id', 3, 'id'), 
                 ('extract_start_date', 4, 'date')]
  
  fields_env = [('totaldistance', 5, 'scalar'),
                ('weight', 6, 'scalar'),
                ('weight_calculation_type', 7, 'class')] # TODO: fill all the fields
  
  fields_drv = [('overrpmtime', 11, 'scalar')] # TODO: fill all the fields

  # TODO: implementation

  return N


def main():
  fname_in = '../data/driver_behavior.csv'
  fname_out_info = '' # TODO: output file name
  fname_out_env = '' # TODO: output file name
  fname_out_drv = '' # TODO: output file name

  N = proc_data(fname_in, fname_out_info, fname_out_env, fname_out_drv)

  print('data has been processed (N=%d)' % (N))
  print('processed info data file saved (file: %s)' % (fname_out_info))
  print('processed environment data file saved (file: %s)' % (fname_out_env))
  print('processed driver data file saved (file: %s)' % (fname_out_drv))


if __name__ == '__main__':
  main()
