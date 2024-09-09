
import sys

from qgis.core import *

#qgs = QgsApplication([], False)
#qgs.initQgis()

sys.path.append('C:\\Program Files\\QGIS 3.22.16\\apps\\qgis-ltr\\python\\plugins')

import plugins.processing
from qgis.analysis import QgsNativeAlgorithms
from plugins.processing.core.Processing import Processing


from plugins.processing.tools import dataobjects

#

from plugins.processing.modeler.ModelerDialog import ModelerDialog
from plugins.processing import  *

class MyFeedBack(QgsProcessingFeedback):

    def setProgressText(self, text):
        print(text)

    def pushInfo(self, info):
        print(info)

    def pushCommandInfo(self, info):
        print(info)

    def pushDebugInfo(self, info):
        print(info)

    def pushConsoleInfo(self, info):
        print(info)

    def reportError(self, error, fatalError=False):
        print(error)

def clipper():

    print ("In clipper")

    # Supply path to qgis install location
    QgsApplication.setPrefixPath("C:\\Program Files\\QGIS 3.22.16", True)

    # Create a reference to the QgsApplication.  Setting the
    # second argument to False disables the GUI.
    qgs = QgsApplication([], False)

    # Load providers
    qgs.initQgis()

    # Write your code here to load some layers, use processing
    # algorithms, etc.


    dlg = ModelerDialog ()
    #dlg.loadModel('C:/Users/Admin/OneDrive - wind-pioneers.com/Documents/Value Added/Raster clipping and '
                  #'Conversion.model3')

    dlg.loadModel('C:/Users/Admin/OneDrive - wind-pioneers.com/Documents/Value Added/Raster clipping'
                  '.model3')

    Processing.initialize()

    QgsApplication.processingRegistry().addProvider(QgsNativeAlgorithms())



    model = dlg.model()


   # model =  QgsProcessingModelAlgorithm('C:/Users/Admin/OneDrive - wind-pioneers.com/Documents/Value Added/Raster clipping and Conversion.model3')

    context = dataobjects.createContext()
    context.setInvalidGeometryCheck(QgsFeatureRequest.GeometryNoCheck)

    result = plugins.processing.run(model, {'country_boundary':'W:/08 Projects/160 Iberdrola/001 Australia(SA)/07 Exports/Boundary/WP-SA-Boundary.kml', 'buffer_distance':1  ,'raster_map':'C:/Users/Admin/Downloads/IRENA_vortex_M.140.year.tiff', 'final_clipped_raster':r'S:/QGIS_Clipper/QGIS_Clipper/output.asc', 'OPTIONS': 'FORMAT=AAIGrid' }, feedback=MyFeedBack(), context=context)

    clippedoutput = result['CHILD_RESULTS']['gdal:cliprasterbymasklayer_1']['OUTPUT']

    params = {
        'INPUT': clippedoutput,  # Input raster file
        'TARGET_CRS': None,  # CRS transformation (optional)
        'OUTPUT': 'S:/QGIS_Clipper/QGIS_Clipper/output.asc',  # Output ASCII file
        'OPTIONS': 'FORMAT=AAIGrid'  # GDAL translate options for ASCII format
    }

    ascii_out = plugins.processing.run("gdal:translate", params, feedback=MyFeedBack(), context=context)

    # Finally, exitQgis() is called to remove the
    # provider and layer registries from memory
    qgs.exitQgis()


def testfunc ():
    print("adsasd")
