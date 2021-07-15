import application
import platform
import sys
sys.dont_write_bytecode=True
if platform.system()!="Darwin":
	f=open("errors.log","a")
	sys.stderr=f
import shutil
import os
if os.path.exists(os.path.expandvars("%temp%\gen_py"))==True:
	shutil.rmtree(os.path.expandvars("%temp%\gen_py"))
# Bye foo!
import wx
app = wx.App(redirect=False)

import globals
globals.load()
import speak
import sound
from GUI import ask, main
if len(sys.argv)>1:
	url=sys.argv[1]
else:
	url=ask.ask(None,"Enter a URL","URL")
urls=[url]
urls=sound.get_audio_urls(urls)
if len(urls)>0:
	a=urls[0]['func'](urls[0]['url'])
	sound.play_url(a)
main.window.Show()
app.MainLoop()