import os
import sys
import wx
from win32gui import GetPath

import clipper


class MyFrame(wx.Frame):

    def execute_clipper (self, event):

        country_boundarys = self.ctry_boundary_input.GetPath()
        buffers = int(self.buffer_val_input.GetValue())
        raster_maps = self.raster_map_input.GetPaths()

        # Progress

        progressdialog = wx.MessageBox("Conversion in progress.....")

        # Iterating through raster maps

        for rasters in raster_maps:

            base_name = os.path.basename(rasters)
            # Split the base name into name and extension
            opfilename, ext = os.path.splitext(base_name)
            output_files = self.output_path_input.GetPath() + "/" + opfilename + "_clipped.asc"


            clipper.clipper(country_boundary=country_boundarys, buffer_dist=buffers, raster_map=rasters,
                            output_file=output_files)

        wx.MessageBox("Done. Click OK to view Output Folder", "Conversion done.", wx.OK | wx.ICON_INFORMATION)

        os.startfile(self.output_path_input.GetPath())

    def rasterfilepicker (self, event):
        self.raster_map_input = wx.FileDialog(self.panel,
                                              message="Select a tiff file",
                                              wildcard="Raster files (*.tiff)|*.tiff|(*.asc)|*.asc",
                                              style=wx.FLP_OPEN | wx.FD_MULTIPLE | wx.FD_FILE_MUST_EXIST)
        self.raster_map_input.ShowModal()

        file_paths = self.raster_map_input.GetPaths()

        selected_file_nums = wx.StaticText(self.panel, label= str (len(file_paths)) + " Files Selected", pos=(450, 150))

    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)

        # Create a self.panel in the frame
        self.panel = wx.Panel(self)

        # Create a text control on the self.panel

        heading = wx.StaticText(self.panel, label="Fill the required fields!", pos=(10, 10))
        font = wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD)
        heading.SetFont (font)

        ctry_boundary = wx.StaticText(self.panel, label="Select Country Boundary (kml/shp)", pos=(10, 50))
        self.ctry_boundary_input = wx.FilePickerCtrl(self.panel,
                          message="Select a Boundary file",
                          wildcard="Boundary files (*.kml)|*.kml|(*.shp)|*.shp",
                          style=wx.FLP_OPEN | wx.FLP_USE_TEXTCTRL,
                          pos=(300, 50))

        buffer_val = wx.StaticText(self.panel, label="Enter Buffer Distance", pos=(10, 100))
        self.buffer_val_input = wx.TextCtrl(self.panel, value="", pos=(300, 100))

        raster_map = wx.StaticText(self.panel, label="Select Raster Map (tiff/asc)", pos=(10, 150))
        rasterpickbtn = wx.Button(self.panel, label="Select Files", pos=(300, 150))

        rasterpickbtn.Bind(wx.EVT_BUTTON, self.rasterfilepicker)


        output_path = wx.StaticText(self.panel, label="Select Output Folder", pos=(10, 200))
        self.output_path_input = wx.DirPickerCtrl(self.panel,
                                           message="Select an Output Folder",
                                           style=wx.DIRP_USE_TEXTCTRL,
                                           pos=(300, 200))


        gobtn = wx.Button(self.panel, label="Convert!", pos=(250, 300))

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

    # Finalizing qgs

    clipper.finalizeqgs()



if __name__=="__main__":

    # Initializing qgs

    clipper.initqgs("C:\\Program Files\\QGIS 3.22.16")

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