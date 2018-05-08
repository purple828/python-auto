import wx
# app = wx.App()
# app.MainLoop()

#显示窗口
# app = wx.App()
# frame = wx.Frame(None)
# frame.Show()#显示窗口
# app.MainLoop()

#在窗口（框架）增加按钮
# app = wx.App()
# frame = wx.Frame(None)
# btn = wx.Button(frame)
# frame.Show()
# app.MainLoop()

# app = wx.App()
# frame = wx.Frame(None,title="Simple Editor")
# loadButton = wx.Button(frame,label='open')
# saveButton = wx.Button(frame,label='save')
# frame.Show()
# app.MainLoop()

app = wx.App()
frame = wx.Frame(None,title="Simple Editor",size=(410,335))
loadButton = wx.Button(frame,label="open",pos=(225,5),size=(80,25))
savaButton = wx.Button(frame,label="save",pos=(315,5),size=(80,25))
filename = wx.TextCtrl(frame,pos=(5,5),size=(210,25))
content = wx.TextCtrl(frame,pos=(5,5),size=(390,260),style=wx.TE_MULTILINE|wx.HSCROLL)
frame.Show()
app.MainLoop()
