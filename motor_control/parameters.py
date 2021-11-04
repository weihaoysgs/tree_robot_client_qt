# -*- coding:utf-8 -*-
'''
file    : parameters
author  : weihaoysgs@gmail.com
des     : $
date    : 2021-10-25 18:58
IDE     : PyCharm
'''

class Parameter(object):
    MOTOR1_ID = 0x01
    MOTOR2_ID = 0x02
    RESET_CMD = 0x03
    SET_POSITION_CMD = 0x04

    TAIL1 = 0x11
    TAIL2 = 0xFF

    MOTOR1_INIT_SPEED = -1000
    MOTOR2_INIT_SPEED = -1000
