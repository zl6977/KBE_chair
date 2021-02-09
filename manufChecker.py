#HTTP Manufacturability Checker Server/ Chair example

from http.server import BaseHTTPRequestHandler, HTTPServer

HOST_NAME = '127.0.0.1' 
PORT_NUMBER = 4321 # Maybe set this to 1234

sidePairUp = 2000
sidePairLow = 500
depthPairUp = 2000
depthPairLow = 500
heightPairUp = 2000
heightPairLow = 500
widthPairUp = 2000
widthPairLow = 500

class RuleChecker():
    def manufCheck():
        pass

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
        
        # Check what is the path
        path = s.path
        if path.find("/setParamsIntervals") != -1:
            #TODO - change HTML accordingly
            s.wfile.write(bytes('<html><body><h2>Chair</h2>', 'utf-8'))
            s.wfile.write(bytes('<form action="/orderChair" method="post">', 'utf-8'))
            
            s.wfile.write(bytes('<label for="sidePairUp">Set Side of the chair (outer)_max:</label><br>', 'utf-8'))
            s.wfile.write(bytes('<input type="text" id="sidePairUp" name="sidePairUp" value="1500"><br><br>', 'utf-8'))
            s.wfile.write(bytes('<label for="depthPairUp">Set Depth for the seat_max:</label><br>', 'utf-8'))
            s.wfile.write(bytes('<input type="text" id="depthPairUp" name="depthPairUp" value="1100"><br><br>', 'utf-8'))
            s.wfile.write(bytes('<label for="heightPairUp">Set Height for the seat_max:</label><br>', 'utf-8'))
            s.wfile.write(bytes('<input type="text" id="heightPairUp" name="heightPairUp" value="1100"><br><br>', 'utf-8'))
            s.wfile.write(bytes('<label for="widthPairUp">Set Width of the seat_max:</label><br>', 'utf-8'))
            s.wfile.write(bytes('<input type="text" id="widthPairUp" name="widthPairUp" value="1100"><br><br>', 'utf-8'))
            
            s.wfile.write(bytes('<label for="sidePairLow">Set Side of the chair (outer)_min:</label><br>', 'utf-8'))
            s.wfile.write(bytes('<input type="text" id="sidePairLow" name="sidePairLow" value="1500"><br><br>', 'utf-8'))
            s.wfile.write(bytes('<label for="depthPairLow">Set Depth for the seat_min:</label><br>', 'utf-8'))
            s.wfile.write(bytes('<input type="text" id="depthPairLow" name="depthPairLow" value="1100"><br><br>', 'utf-8'))
            s.wfile.write(bytes('<label for="heightPairLow">Set Height for the seat_min:</label><br>', 'utf-8'))
            s.wfile.write(bytes('<input type="text" id="heightPairLow" name="heightPairLow" value="1100"><br><br>', 'utf-8'))
            s.wfile.write(bytes('<label for="widthPairLow">Set Width of the seat_min:</label><br>', 'utf-8'))
            s.wfile.write(bytes('<input type="text" id="widthPairLow" name="widthPairLow" value="1100"><br><br>', 'utf-8'))
            
            s.wfile.write(bytes('<input type="submit" value="Submit">', 'utf-8'))
            s.wfile.write(bytes('</form></body></html>', 'utf-8'))
        else:
            s.wfile.write(bytes('<html><head><title>Cool interface.</title></head>', 'utf-8'))
            s.wfile.write(bytes("<body><p>The path: " + path + "</p>", "utf-8"))
            s.wfile.write(bytes('</body></html>', "utf-8"))
            
            
    def do_POST(s):
        global sidePairUp, sidePairLow, depthPairUp, depthPairLow, heightPairUp,  heightPairLow, widthPairUp, widthPairLow
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        
        # Check what is the path
        path = s.path
        print("Path: ", path)
        if path.find("/setParamsIntervals") != -1:
            #TODO - set intervals for params
            content_len = int(s.headers.get('Content-Length'))
            post_body = s.rfile.read(content_len)
            param_line = post_body.decode()
            print("Body: ", param_line)
            
            #Get the param value
            pairs = param_line.split("&")
            sidePairUp = pairs[0].split("=")
            depthPairUp = pairs[1].split("=")
            heightPairUp = pairs[2].split("=")
            widthPairUp = pairs[3].split("=")
            sidePairLow = pairs[4].split("=")
            depthPairLow = pairs[5].split("=")
            heightPairLow = pairs[6].split("=")
            widthPairLow = pairs[7].split("=")
            
            s.wfile.write(bytes('<html><body><h2>Chair</h2>', 'utf-8'))
            s.wfile.write(bytes('<form action="/orderChair" method="post">', 'utf-8'))
            
            s.wfile.write(bytes('<label for="sidePairUp">Set Side of the chair (outer)_max:</label><br>', 'utf-8'))
            s.wfile.write(bytes('<input type="text" id="sidePairUp" name="sidePairUp" value="1500"><br><br>', 'utf-8'))
            s.wfile.write(bytes('<label for="depthPairUp">Set Depth for the seat_max:</label><br>', 'utf-8'))
            s.wfile.write(bytes('<input type="text" id="depthPairUp" name="depthPairUp" value="1100"><br><br>', 'utf-8'))
            s.wfile.write(bytes('<label for="heightPairUp">Set Height for the seat_max:</label><br>', 'utf-8'))
            s.wfile.write(bytes('<input type="text" id="heightPairUp" name="heightPairUp" value="1100"><br><br>', 'utf-8'))
            s.wfile.write(bytes('<label for="widthPairUp">Set Width of the seat_max:</label><br>', 'utf-8'))
            s.wfile.write(bytes('<input type="text" id="widthPairUp" name="widthPairUp" value="1100"><br><br>', 'utf-8'))
            
            s.wfile.write(bytes('<label for="sidePairLow">Set Side of the chair (outer)_min:</label><br>', 'utf-8'))
            s.wfile.write(bytes('<input type="text" id="sidePairLow" name="sidePairLow" value="1500"><br><br>', 'utf-8'))
            s.wfile.write(bytes('<label for="depthPairLow">Set Depth for the seat_min:</label><br>', 'utf-8'))
            s.wfile.write(bytes('<input type="text" id="depthPairLow" name="depthPairLow" value="1100"><br><br>', 'utf-8'))
            s.wfile.write(bytes('<label for="heightPairLow">Set Height for the seat_min:</label><br>', 'utf-8'))
            s.wfile.write(bytes('<input type="text" id="heightPairLow" name="heightPairLow" value="1100"><br><br>', 'utf-8'))
            s.wfile.write(bytes('<label for="widthPairLow">Set Width of the seat_min:</label><br>', 'utf-8'))
            s.wfile.write(bytes('<input type="text" id="widthPairLow" name="widthPairLow" value="1100"><br><br>', 'utf-8'))
            
            s.wfile.write(bytes('<input type="submit" value="Submit">', 'utf-8'))
            s.wfile.write(bytes('</form></body></html>', 'utf-8'))
            
            s.wfile.write(bytes('<p>The max values was set to ' + str(sidePairUp[1]) + str(depthPairUp[1]) + str(heightPairUp[1]) + str(widthPairUp[1])  + '</p>', 'utf-8'))
            s.wfile.write(bytes('<p>The min values was set to ' + str(sidePairLow[1]) + str(depthPairLow[1]) + str(heightPairLow[1]) + str(widthPairLow[1])  + '</p>', 'utf-8'))
            
            s.wfile.write(bytes('</form></body></html>', 'utf-8'))
            
        elif path.find("/orderChair") != -1:

            content_len = int(s.headers.get('Content-Length'))
            post_body = s.rfile.read(content_len)
            param_line = post_body.decode()
            print("Body: ", param_line)
            
            #Get the param value
            pairs = param_line.split("&")
            sidePair = pairs[0].split("=")
            depthPair = pairs[1].split("=")
            heightPair = pairs[2].split("=")
            widthPair = pairs[3].split("=")
            
            if (sidePair < sidePairUp) and (sidePair > sidePairDown)) and
                (depthPair < sidePairUp) and (depthPair > sidePairDown)) and
                (sidePair < sidePairUp) and (sidePair > sidePairDown)) and
                (sidePair < sidePairUp) and (sidePair > sidePairDown)):
                s.wfile.write(bytes('OK', 'utf-8'))
            else:
            s.wfile.write(bytes('NOK', 'utf-8'))

            
            
 
if __name__ == '__main__':
    server_class = HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
