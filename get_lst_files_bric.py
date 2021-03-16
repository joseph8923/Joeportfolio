#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 16:33:42 2019

@author: josepht
"""

import os


STN_POS = ['661',
           '662',
           '671',
           '672',
           '673',
           '681',
           '682',
           '683',
           '691',
           '692',
           '693',
           '701',
           '702',
           '703',
           '711',
           '712',
           '713',
           '721',
           '722',
           '723',
           '731',
           '732',
           '733'
        ]

distance = [0,
            2.5,
            5,
            10,
            15,
            22.5,
            30,
            40,
            50,
            60,
            70,
            80,
            90,
            100,
            110,
            120,
            130,
            137.5,
            145,
            150,
            155,
            157.5,
            160
            ]

with open("stn.lst","w+") as f_stn:
    for istn in range(len(STN_POS)):
        f_stn.write(str(STN_POS[istn])+"\n")
        
with open("loc.lst","w+") as f_loc:
    for iloc in range(len(distance)):
        f_loc.write(str(distance[iloc])+"\n")