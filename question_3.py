# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 01:33:18 2021

@author: hp
"""

import aima.utils
import aima.logic
import aima.utils.expression as ex
def main ():
    
         clauses = []
         
          clauses.append(ex("( hates (x,y ) & hates (y,x)==> enimes (x,y)"))
          
          clauses.append(ex(" q(x) & r(x) ==> p(x) "))


