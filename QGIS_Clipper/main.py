
import wx
import clipper


class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)

        # Create a panel in the frame
        panel = wx.Panel(self)

        # Create a text control on the panel
        text = wx.TextCtrl(panel, value="Hello, wxPython!", pos=(10, 10))

        # Set up the frame
        self.SetTitle("Simple wxPython Window")
        self.SetSize((300, 200))
        self.Centre()


class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, wx.ID_ANY, "")
        frame.Show()
        return True

def gui ():
    app = MyApp (False)
    app.MainLoop()



if __name__=="__main__":
    print("Test")
    clipper.clipper()

    #clipper()
    #gui()