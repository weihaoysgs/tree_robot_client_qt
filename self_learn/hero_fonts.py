# -*- coding:utf-8 -*-
'''
file    : hero_fonts
author  : weihaoysgs@gmail.com
des     : $
date    : 2021-09-27 21:21
IDE     : PyCharm
'''
from pyfiglet import Figlet ,FigletFont
f = Figlet(font='slant')
print(f.renderText('HLL Super Hero'))

# from pyfiglet import Figlet, FigletFont
#
print(FigletFont().getFonts())
# f = Figlet(font='5x8')
# print(f.renderText('HLL Super Hero'))