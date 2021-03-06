#!/usr/bin/env python 

from socket import gethostbyname,gethostname
from random import randint
from sys import argv
import RPi.GPIO as GPIO 
from time import sleep

gpio_led = 7 
#Set to .2 for my bad morse skills. 
#morse_dot = float(.02)
morse_dot = float(.2)
morse_dash = morse_dot * 3
morse_pause_elements = morse_dot
morse_pause_char = morse_dot * 3
morse_pause_words = morse_dot * 7
DEBUG = "false" 
#DEBUG = "true" 
CODE = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
     	'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',
        
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.',

        '.' : '.-.-.-', ',' : '--..--', ':' : '---...',
        '?' : '..--..', "'" : '.----.', '-' : '-....-',
    	'/' : '-..-.',  '@' : '.--.-.', '=' : '-...-',
        '.': '-.-.-.',
        }

#Setup GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(gpio_led, GPIO.OUT) 

def blink_morse(the_code):
 for c in the_code:
   if c == ".":
      if DEBUG == "true":
        print "its a dot"
      GPIO.output(gpio_led, True)
      sleep(morse_dot)
      GPIO.output(gpio_led, False)
      sleep(morse_pause_elements)
   elif c == "-":
      if DEBUG == "true":
        print "its a dash" 
      GPIO.output(gpio_led, True)
      sleep(morse_dash)
      GPIO.output(gpio_led, False)
      sleep(morse_pause_elements)
   else:
      print "its not a %r or a %r." % (".", "-")

 sleep(morse_pause_elements)

 if DEBUG == "true":
   print "EOL"

def word_2_elements(word):
   for c in word:
     if c == ' ':
       if DEBUG == "true":
         print "its a space"
       sleep(morse_pause_words)
     else:   
       blink_morse(CODE[c.upper()])

#Get ip address of host and blink it out. 
def blink_ip():
  myip = gethostbyname(gethostname())
  if '127.0' in myip:
    print "ohoh, Looks like /etc/hosts has a localhost/hostname entry, %r" %  myip
    exit()
  if DEBUG == "true":
    print myip
  word_2_elements(myip)

#Get ip address of host and blink it out. 
def blink_hostname():
  myname = gethostname()
  if DEBUG == "true":
    print myname
  print myname
  word_2_elements(myname)


#If no args are provided blink hostname. 
if len(argv) > 1:
  word_2_elements(argv[1])
else:
  blink_hostname()
