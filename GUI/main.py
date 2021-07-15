import wx
import os
import platform
import sys
import application
import globals
import speak
class MainGui(wx.Frame):
	def __init__(self, title):
		wx.Frame.__init__(self, None, title=title,size=(800,600))
		self.Center()
		self.Bind(wx.EVT_CLOSE, self.OnClose)
		self.panel = wx.Panel(self)
		self.main_box = wx.BoxSizer(wx.VERTICAL)
		self.menuBar = wx.MenuBar()
		if platform.system()!="Darwin":
			ctrl="control"
		else:
			ctrl="command"

		menu = wx.Menu()
		m_close = menu.Append(wx.ID_EXIT, "exit", "exit")
		self.Bind(wx.EVT_MENU, self.OnClose, m_close)
		self.menuBar.Append(menu, "&Application")
		menu2 = wx.Menu()
		m_volup = menu2.Append(-1, "Volume up (up)", "volup")
		self.Bind(wx.EVT_MENU, self.OnVolup, m_volup)
		m_voldown = menu2.Append(-1, "Volume down (down)", "voldown")
		self.Bind(wx.EVT_MENU, self.OnVoldown, m_voldown)
		self.menuBar.Append(menu2, "&Playback")
		self.SetMenuBar(self.menuBar)
		accel=[]
		accel.append((wx.ACCEL_ALT, ord('X'), m_close.GetId()))
		accel_tbl=wx.AcceleratorTable(accel)
		self.SetAcceleratorTable(accel_tbl)
		self.panel.Layout()

	def OnVolup(self, event=None):
		if globals.prefs.volume<1.0:
			globals.prefs.volume+=0.1
			globals.prefs.volume=round(globals.prefs.volume,1)
			if sound.player!=None:
				sound.player.volume=globals.prefs.volume

	def OnVoldown(self, event=None):
		if globals.prefs.volume>0.0:
			globals.prefs.volume-=0.1
			globals.prefs.volume=round(globals.prefs.volume,1)
			if sound.player!=None:
				sound.player.volume=globals.prefs.volume

	def OnClose(self, event=None):
		self.Destroy()
		sys.exit()

global window
window=MainGui(application.name+" "+application.version)