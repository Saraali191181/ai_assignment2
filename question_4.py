# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 01:06:48 2021

@author: hp
"""

import aima.utils
import aima.logic
import aima.utils.expression as ex
 def main ():
     
     clauses = []
     clauses.append(ex("(women(jia) & man(john) & healthy (john) & healthy (jia) & wealthy (john) ))")
     
     clauses.append(ex("(healthy(anyone) & wealthy (anyone) ==> traveler (anyone)" ) )
      
     clauses.append(ex(" traveler (anyone) ==>  travel (anyone)"))
      
     KB = aima.logic.FolKB(clauses)
     
          
     # get infoemation from KB with ask 
     
     travel=KB.ask(ex("travel(x)"))
     
     healthy_and_wealthy = KB.ask(ex ("healthy(x) & wealthy(x)"))
      
     print (" travel")
     print (travel)
     
     print ("healthy_and_wealthy")
     
     
     print (healthy_and_wealthy)


     
        
      
    