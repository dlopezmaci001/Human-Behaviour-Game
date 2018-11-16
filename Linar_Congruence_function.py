# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 22:19:50 2018

@author: Daniel
"""
    
def linear_congruence (seed):
     i=0
     i = (22695477*(seed)+1)%(2**32)
     return(int(i))
     
