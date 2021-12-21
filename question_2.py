# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 01:01:33 2021

@author: hp
"""

import aima.utils
import aima.logic
import aima.utils.expr as ex
def main ():
    
         clauses = []
         
         clauses.append(ex (" read (maria , logicprogramming) & author (peter_lucas) "))
          
         clauses.append( ex("like (anyone , shopping )") )
         clauses.append( ex("(city (big , crowdy) ==> hates (kirke)) ")) 
         
         KB = aima.logic.FolKB(clauses)
         
         like_shopping = KB.ask("like(x)")
         
         
         print ("like shopping")
         
         print (like_shopping)




