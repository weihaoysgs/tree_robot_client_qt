# -*- coding:utf-8 -*-
'''
file    : parameters
author  : weihaoysgs@gmail.com
des     : $
date    : 2021-09-01 14:00
IDE     : PyCharm
'''
class ServoParam(object):
    YawServo_ID = 1
    PitchBottomServo_ID = 2
    PitchMidServo_ID = 3
    PitchUpServo_ID = 4
    GrabServo_ID = 5

    YawInit_Value = 1754
    PitchBottomInit_Value = 1883
    PitchMidInit_Value = 1826
    PitchUpInit_Value = 1889
    GrabInit_Value = 1910

    Grab_GrabCompareValue = 1910
    Grab_OpenCompareValue = 1865

    def __init__(self):
        pass