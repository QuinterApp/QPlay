import wx
def alert(message, caption = "", parent=None):
	dlg = wx.MessageDialog(parent, message, caption, wx.OK)
	dlg.ShowModal()
	dlg.Destroy()

