# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 21:00:20 2017

@author: Revant
"""

import data_parser

file_path = 'KB8024/data/globular_signal_tm_3state.txt'
out_path = 'KB8024/project/input'
window_size = 3

data_parser.signalP_parser(file_path, out_path, window_size)