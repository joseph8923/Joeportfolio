#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 17:43:06 2019

@author: josepht
"""

STN_POS = ['661',
           '663',
           '741',
           '742',
           '743',
           '751',
           '752',
           '753',
           '761',
           '762',
           '763',
           '771',
           '772',
           '773',
           '781',
           '782',
           '783',
           '791',
           '792',
           '793',
           '801',
           '802',
           '803',
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