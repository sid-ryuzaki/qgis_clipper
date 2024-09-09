import sys
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

    '''
    country_boundary = 'W:/08 Projects/160 Iberdrola/001 Australia(SA)/07 Exports/Boundary/WP-SA-Boundary.kml'
    buffer = 1
    raster_map = 'C:/Users/Admin/Downloads/IRENA_vortex_M.140.year.tiff'
    output_file = 'S:/QGIS_Clipper/QGIS_Clipper/output.asc'
    '''

    # Reading cmdline args

    country_boundary = sys.argv[1]
    buffer = int(sys.argv[2])
    raster_map = sys.argv[3]
    output_file = sys.argv[4]

    clipper.clipper(country_boundary=country_boundary, buffer_dist=buffer, raster_map=raster_map, output_file=output_file)
    #gui()