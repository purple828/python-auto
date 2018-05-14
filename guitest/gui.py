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

#***********************************************绝对坐标实现弹出窗口
# app = wx.App()
# frame = wx.Frame(None,title="Simple Editor",size=(410,335))
# loadButton = wx.Button(frame,label="open",pos=(225,5),size=(80,25))
# savaButton = wx.Button(frame,label="save",pos=(315,5),size=(80,25))
# filename = wx.TextCtrl(frame,pos=(5,5),size=(210,25))
# content = wx.TextCtrl(frame,pos=(5,5),size=(390,260),style=wx.TE_MULTILINE|wx.HSCROLL)
# frame.Show()
# app.MainLoop()

#**********************************实现效果和上式一样，但是是使用的相对坐标
# app = wx.App()
# win = wx.Frame(None,title="simple Editor" ,size=(410,335))
# bkg = wx.Panel(win)
# loadButton = wx.Button(bkg,label="open")
# saveButton = wx.Button(bkg,label="save")
# filename = wx.TextCtrl(bkg)
# contents = wx.TextCtrl(bkg,style=wx.TE_MULTILINE|wx.HSCROLL)
#
# #水平布局器
# hbox = wx.BoxSizer()
# hbox.Add(filename,proportion=1,flag = wx.EXPAND)
# hbox.Add(loadButton,proportion = 0,flag=wx.LEFT,border=5)
# hbox.Add(saveButton,proportion=0,flag=wx.LEFT,border=5)
# #垂直布局器
# vbox = wx.BoxSizer(wx.VERTICAL)
# vbox.Add(hbox,proportion=0,flag = wx.EXPAND|wx.ALL,border=5)
# vbox.Add(contents,proportion=1,flag=wx.EXPAND|wx.LEFT|wx.BOTTOM|wx.RIGHT,border=5)
#
# bkg.SetSizer(vbox)
# win.Show()
# app.MainLoop()

#************************绑定事件
# def load(event):
#     file = open(filename.GetValue(),"r")
#     contents.SetValue(file.read())
#     file.close()
# def save(event):
#     file = open(filename.GetValue(),"w")
#     file.write(contents.GetValue())
#     file.close()
#
# app = wx.App()
# win = wx.Frame(None,title="simple Editor" ,size=(410,335))
# bkg = wx.Panel(win)
# loadButton = wx.Button(bkg,label="open")
# loadButton.Bind(wx.EVT_BUTTON,load)
# saveButton = wx.Button(bkg,label="save")
# saveButton.Bind(wx.EVT_BUTTON,save)
# filename = wx.TextCtrl(bkg)
# contents = wx.TextCtrl(bkg,style=wx.TE_MULTILINE|wx.HSCROLL)
#
# hbox = wx.BoxSizer()
# hbox.Add(filename,proportion=1,flag = wx.EXPAND)
# hbox.Add(loadButton,proportion = 0,flag=wx.LEFT,border=5)
# hbox.Add(saveButton,proportion=0,flag=wx.LEFT,border=5)
# #垂直布局器
# vbox = wx.BoxSizer(wx.VERTICAL)
# vbox.Add(hbox,proportion=0,flag = wx.EXPAND|wx.ALL,border=5)
# vbox.Add(contents,proportion=1,flag=wx.EXPAND|wx.LEFT|wx.BOTTOM|wx.RIGHT,border=5)
#
# bkg.SetSizer(vbox)
# win.Show()
# app.MainLoop()






