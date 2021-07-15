import sys
import shutil
import platform
from GUI import main
import tweak
import os
prefs=None
confpath=""

def  load():
#	utils.cfu()
	global confpath
	global prefs
	prefs=tweak.Config(name="QPlay",autosave=True)
	confpath=prefs.user_config_dir
	if platform.system()=="Darwin":
		try:
			f=open(confpath+"/errors.log","a")
			sys.stderr=f
		except:
			pass
	prefs.volume=prefs.get("volume",1.0)
