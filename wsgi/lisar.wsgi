# -*- coding:utf-8 -*-

import os, sys

#Add path into sys.path
p1 = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
p2 = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(p1)
sys.path.append(p2)

  
#redirect output to stderr, any print call will output into error.log of apache
sys.stdout = sys.stderr
#print sys.path
  
#settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'LISAR.settings'
  
import django.core.handlers.wsgi 
  
application = django.core.handlers.wsgi.WSGIHandler()
  