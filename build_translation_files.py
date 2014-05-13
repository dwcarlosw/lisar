#!/usr/bin/env python
import sys, os, time, threading
import logging, logging.handlers
from subprocess import Popen, PIPE, STDOUT


app_dirs = ['project_lisar', 'bobthings', 'translate']

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

#logging
# logger = logging.getLogger('build_translation_files')
# handler = logging.handlers.RotatingFileHandler('', maxBytes=5242880, backupCount=5)
# formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
# handler.setFormatter(formatter)
# logger.addHandler(handler)
# logger.setLevel(logging.ERROR)

def build_translation_files( base_dir, app_name ):
    app_dir = os.path.join(BASE_DIR, app_name)
    app_admin = os.path.join(BASE_DIR, app_name+"/django-admin.py")

    if not os.path.isdir(app_dir):
        print "App " + app_name + " doesn't exist."
        return

    if not os.path.isfile(app_admin):
        p = Popen(['sudo', 'cp', os.path.join(BASE_DIR, "django-admin.py"), app_dir], stdout=PIPE, stderr=PIPE)
        out, err = p.communicate()


    p = Popen(['sudo', app_admin, 'makemessages', '--all'], stdout=PIPE, cwd=app_dir)
    out, err = p.communicate()

    print out


    p = Popen(['sudo', app_admin, 'compilemessages'], stdout=PIPE, cwd=app_dir)
    out, err = p.communicate()

    print out

print "    ****** BUILDING STATIC CONTENTS ******    "
for app in app_dirs:
    print "Making translation files for " + app + ":"
    build_translation_files( BASE_DIR, app )
