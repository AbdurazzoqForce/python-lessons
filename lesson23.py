# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 19:41:16 2024

@author: пк
"""


#klass va obyekt


class komputer:
     def __init__(self, ram, hdd, gpu, cpu):
        self.ram=ram
        self.hdd=hdd
        self.gpu=gpu
        self.cpu=cpu
        
        def info(self):
            inf=f"{self.model}, RAM:{self.ram}, SSD{self.hdd}, CPU{self.cpu}"
            return inf
        
macbook=komputer( "Apple macbook", "8GB", "512GM", "M1", "M1")























































