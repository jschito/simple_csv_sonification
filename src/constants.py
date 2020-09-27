#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Used constants."""

__author__ = 'Joram Schito'
__copyright__ = 'Copyright 2017, ETH Zurich'
__credits__ = 'Joram Schito'
__license__ = 'MIT'
__version__ = '0.1.2'
__maintainer__ = 'Joram Schito'
__email__ = 'joram@joramschito.ch'
__status__ = 'Development'

import os


# Important paths
code_dir = os.path.dirname(__file__)
root = os.path.dirname(code_dir)
data_dir = os.path.join(root, 'res')
data_has_header = True


# Data set
input_csv_file = os.path.join(data_dir, 'data_0_all.csv')


# Sound settings
sample_rate = 44100  # Hertz
basic_frequency = 442  # Hertz
octave = 2 * basic_frequency
midi_c_5oct = 60
midi_c_7oct = 84
midi_pitch_range = midi_c_7oct - midi_c_5oct
time_to_next_note = 0.002


# Statistical analysis settings
max_std_dev_for_determining_outliers = 3
