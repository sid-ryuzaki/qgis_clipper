import sys
import wx
import clipper


class MyFrame(wx.Frame):

    def execute_clipper (self, event):

        country_boundarys = self.ctry_boundary_input.GetPath()
        buffers = int(self.buffer_val_input.GetValue())
        raster_maps = self.raster_map_input.GetPath()
        output_files = self.output_path_input.GetPath() + "/" + self.output_name_input.GetValue()

        
        clipper.clipper(country_boundary=country_boundarys, buffer_dist=buffers, raster_map=raster_maps,
                        output_file=output_files)

        wx.MessageBox("Done", "Conversion done. Check " + output_files + " for the result!", wx.OK | wx.ICON_INFORMATION)


    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)

        # Create a panel in the frame
        panel = wx.Panel(self)

        # Create a text control on the panel

        heading = wx.StaticText(panel, label="Fill the required fields!", pos=(10, 10))
        font = wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD)
        heading.SetFont (font)

        ctry_boundary = wx.StaticText(panel, label="Select Country Boundary (kml)", pos=(10, 50))
        #self.ctry_boundary_input = wx.TextCtrl(panel, value="", pos=(200, 50))
        self.ctry_boundary_input = wx.FilePickerCtrl(panel,
                          message="Select a KML file",
                          wildcard="Text files (*.kml)|*.kml",
                          style=wx.FLP_OPEN | wx.FLP_USE_TEXTCTRL,
                          pos=(300, 50))

        buffer_val = wx.StaticText(panel, label="Enter Buffer Distance", pos=(10, 100))
        self.buffer_val_input = wx.TextCtrl(panel, value="", pos=(300, 100))

        raster_map = wx.StaticText(panel, label="Select Raster Map (tiff)", pos=(10, 150))
        self.raster_map_input = wx.FilePickerCtrl(panel,
                          message="Select a tiff file",
                          wildcard="Text files (*.tiff)|*.tiff",
                          style=wx.FLP_OPEN | wx.FLP_USE_TEXTCTRL,
                          pos=(300, 150))

        output_path = wx.StaticText(panel, label="Select Output Folder", pos=(10, 200))
        self.output_path_input = wx.DirPickerCtrl(panel,
                                           message="Select an Output Folder",
                                           style=wx.DIRP_USE_TEXTCTRL,
                                           pos=(300, 200))

        output_name = wx.StaticText(panel, label="Select Output File name (ending with .asc)", pos=(10, 250))
        self.output_name_input = wx.TextCtrl(panel, value="", pos=(300, 250))

        gobtn = wx.Button(panel, label="Convert!", pos=(250, 300))

        gobtn.Bind(wx.EVT_BUTTON, self.execute_clipper)

        # Set up the frame
        self.SetTitle("Clipper And Converter")
        self.SetSize((640, 480))
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

    gui()

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

    #clipper.clipper(country_boundary=country_boundary, buffer_dist=buffer, raster_map=raster_map, output_file=output_file)
    #gui()