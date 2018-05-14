# -*- coding: utf-8 -*-

import re 
import random

def get_password():

    f=open('password_element.txt', 'r')
    str_main =f.read()
	
	#Choose a random word from the file password_element.txt
    random_word = random.choice([str(s) for s in str_main.split() if s.isalpha()])
	
	#Choose a random number from the file password_element.txt
    random_digit = str(random.choice([int(s) for s in str_main.split() if s.isdigit()]))
	
	#Select a random character from the file password_element.txt
    random_symbol = random.choice(str(' '.join(re.findall(r'[!#=*-]', str_main))).split())
	
    list_main = [random_word,random_digit,random_symbol]
    random_password = ''.join(random.sample(list_main, len(list_main)))
	
    f.close()
	
    return random_password