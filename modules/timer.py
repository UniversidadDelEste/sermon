#!/usr/bin/
# -*- coding: utf-8 -*-

""" 
   timer.py - clase para timer no bloqueante (threads)
   
   Copyright 2016 - Diego Codevilla - <dcodevilla@pioix.edu.ar>
   
   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.
   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.
   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  
"""

from threading import Timer

class tick_timer():
    def __init__(self, inte, fnc, arg):     
        self.intervalo = inte
        self.argumentos = arg
        self.funcion = fnc
        self.contando = 1
    
    def timeout(self):
        self.contando = 0
        self.funcion(*self.argumentos)
        self.timer = Timer(self.intervalo,self.timeout)
        self.timer.daemon = True
        self.timer.start()
        self.contando = 1
        
    def start(self):
        self.timeout()
        
    def stop(self):
        if self.contando == 1:
            self.timer.cancel()
            self.contando = 1

#def proceso(a, b):
        #print a * b

#def otro(x, y, z):
        #print "otro->", x+y+z


#if __name__ == '__main__':
    #a = 95
    #c = 2.36
    
    #x=tick_timer(0.5,proceso, [a, c])
    #x.start()
     
    #x2=tick_timer(3,otro, [5, 2, c])
    #x2.start() 
    
    #a = ''
    #while a != 'x':
        #a = raw_input('>')
        #print "-------", a
        
    #x.stop()
    #x2.stop()