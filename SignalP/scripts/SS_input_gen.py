# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 21:00:20 2017

@author: Revant
"""

import SS_parser

filepath = '''/KB8024/KB8024/data/globular_signal_tm_3state.txt'''
outpath = '''/KB8024/KB8024/SignalP/input/Window_3'''
window_size = 3

SS_parser.skl_inp_gen(filepath, outpath, window_size, False)



