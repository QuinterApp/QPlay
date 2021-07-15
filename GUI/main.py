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
		self.SetMenuBar(self.menuBar)
		accel=[]
		accel.append((wx.ACCEL_ALT, ord('X'), m_close.GetId()))
		accel_tbl=wx.AcceleratorTable(accel)
		self.SetAcceleratorTable(accel_tbl)
		self.panel.Layout()

	def OnClose(self, event=None):
		self.Destroy()
		sys.exit()

global window
window=MainGui(application.name+" "+application.version)