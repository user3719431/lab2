import numpy as np
import math
from time import timeit


def modul(a, n):
    t.repeat()
	while (a > n): #тут функція порівняння використовується
		a = a - n
	return a
    

def gcd(a, b):
    t.repeat()
	if (b = 0):
		return a
	elif:
		a = modul(a, b)
		return gcd(b, a)
		
def lcd(a, b):
    t.repeat()
	temp = longmul(a, b)
	c = longdiv(temp, gcd(a, b))
	return c
	
def addmodul(a, b, n):
    t.repeat()
	a1 = modul(a, n)
	b1 = modul(b, n)
	c = modul(a + b, n)
	return c
	
def submodul(a, b, n):
    t.repeat()
	a1 = modul(a, n)
	b1 = modul(b, n)
	c = longsub(a, b)
	if (c > 0):
		c = modul(c, n)
		return c
	elif (c = 0):
		return 0
	else:
		while (c < 0):
			c = c + n
			return (c + n)
			
def mulmodul(a, b):
    t.repeat()
	a = modul(a, n)
	b = modul(b, n)
	c = longmul(a, b)
	c = modul(c, n)
	return c
	
def stepmodul(a, d, n):
    t.repeat()
	n = 1
	c = 0
	while no != (n + 1):
		c = modul((c * a), n)
		no = no + 1
	return c
	
t = timeit.Timer('char in text', setup='text = "sample string"; char = "g"')
t.timeit()
