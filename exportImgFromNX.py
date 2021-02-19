# NX 1957
# Journal created by lianz on Fri Feb 19 12:19:03 2021 W. Europe Standard Time
#
import math
import NXOpen
import NXOpen.Gateway

from http.server import BaseHTTPRequestHandler, HTTPServer

HOST_NAME = '127.0.0.1' 
PORT_NUMBER = 54321

def exportImage(imgName) : 

    theSession  = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display
    workPart.RuleManager.Reload(True)
    
    # ----------------------------------------------
    #   Menu: File->Export->Image...
    # ----------------------------------------------
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    theUI = NXOpen.UI.GetUI()
    
    imageExportBuilder1 = theUI.CreateImageExportBuilder()
    
    imageExportBuilder1.RegionMode = False
    
    regiontopleftpoint1 = [None] * 2 
    regiontopleftpoint1[0] = 0
    regiontopleftpoint1[1] = 0
    imageExportBuilder1.SetRegionTopLeftPoint(regiontopleftpoint1)
    
    imageExportBuilder1.RegionWidth = 1
    
    imageExportBuilder1.RegionHeight = 1
    
    imageExportBuilder1.FileFormat = NXOpen.Gateway.ImageExportBuilder.FileFormats.Png
    
    imageExportBuilder1.FileName = "C:\\GitRepo\\KBE_chair\\" + imgName
    
    imageExportBuilder1.BackgroundOption = NXOpen.Gateway.ImageExportBuilder.BackgroundOptions.Original
    
    imageExportBuilder1.EnhanceEdges = False
    
    nXObject1 = imageExportBuilder1.Commit()
    
    theSession.DeleteUndoMark(markId1, "Export Image")
    
    imageExportBuilder1.Destroy()
    
    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------
    
# Handler of HTTP requests / responses
class MyHandler(BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
    def do_GET(s):
        """Respond to a GET request."""
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        
        path = s.path
        print("Body: ", path)
        #Get the param value
        pairs = path.split("&")
        imgName = pairs[0].split("=")
        
        # Check what is the path
        if path.find("/exportImage") != -1:
            #TODO - change HTML accordingly
            exportImage(imgName[1])
            s.wfile.write(bytes(imgName[1], "utf-8"))
        else:
            s.wfile.write(bytes('<html><head><title>Image from NX</title></head>', 'utf-8'))
            s.wfile.write(bytes("<body><p>The path: " + path + "</p>", "utf-8"))
            s.wfile.write(bytes('</body></html>', "utf-8"))
            
if __name__ == '__main__':
    server_class = HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()