#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=line-too-long, invalid-name
"""
DML exciter library
250603 : typo in kr of DAEX25VT4, was 0.003, correction kr = 0.0003 as per parameters extractions.
"""

def get_exciter(excitertype):
    """
    return the model parameters associated to excitertype
    Parameters are defined as :
        BL, Re, Le, Mms, Cms, Rms (Rv), xr, xi, kr, ki, fv, nv (Wright/Thorborg model)
    """
    exciterdict = {
        "DAEX25FHE4_A": [3.67, 4.47, 0, 0.001235, 0.00041, 0.041, 0.89, 0.79, 0.0001, 0.0007, 181, 1],
        "DAEX25FHE4_C": [3.63, 4.5, 0, 0.00127, 0.00044, 0.038, 0.86, 0.8, 0.00012, 0.00066, 199, 1],
        "DAEX25FHE4": [3.65, 4.3, 0, 0.00125, 0.00043, 0.041, 0.87, 0.8, 0.0001, 0.0007, 190, 1.],
        "DAEX25VT4": [4.2, 3.5, 0, 0.0016, 0.00037, 0.1, 0.82, 0.74, 0.0003, 0.0013, 215, 0.9],
        "XT25_4": [3.8, 3, 0, 0.0017, 0.00014, 0.01, 0.76, 0.74, 0.005, 0.0012, 1700, 0.7],
        "XT32_4": [4, 3, 0, 0.0022, 0.00012, 0.13, 0.86, 0.8, 0.0014, 0.0006, 360, 1.1],
        "Ideal exciter": [4, 4, 0, 0., 1e6, 0, 0, 0, 0, 0, 0, 0],
        "Test": [4, 4, 0, 0.00166, 0.00021, 0, 0, 0, 0, 0, 0, 0]
    }

    return exciterdict[excitertype]
