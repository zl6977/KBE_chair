#HTTP Manufacturability Checker Server/ Chair example

from http.server import BaseHTTPRequestHandler, HTTPServer

HOST_NAME = '127.0.0.1' 
PORT_NUMBER = 4321 # Maybe set this to 1234

class RuleChecker():
    leg_length_range = [500,1500]
    back_height_range = [400,1500]
    seat_length_range = [200,800]
    seat_width_range = [300,800]
    back_tilt_angle_range = [0,30]
    top_rail_added_length_range = [0,400]
    def check_manufacutrable(self, ParameterSet):
        leg_length = ParameterSet[0]
        back_height = ParameterSet[1]
        seat_length = ParameterSet[2]
        seat_width = ParameterSet[3]
        back_tilt_angle = ParameterSet[4]
        top_rail_added_length = ParameterSet[5]
        #flag = ture means it is OK
        leg_length_flag = self.compare_para_in_range(self.leg_length_range, leg_length)
        back_height_flag = self.compare_para_in_range(self.back_height_range, back_height)
        seat_length_flag = self.compare_para_in_range(self.seat_length_range, seat_length)
        seat_width_flag = self.compare_para_in_range(self.seat_width_range, seat_width)
        back_tilt_angle_flag = self.compare_para_in_range(self.back_tilt_angle_range, back_tilt_angle)
        top_rail_added_length_flag = self.compare_para_in_range(self.top_rail_added_length_range, top_rail_added_length)
        
        result = ""
        if not leg_length_flag:
            result += "leg_length not OK\n"
        if not back_height_flag:
            result += "back_height_ not OK\n"
        if not seat_length_flag:
            result += "seat_length not OK\n"
        if not seat_width_flag:
            result += "seat_width not OK\n"
        if not back_tilt_angle_flag:
            result += "back_tilt_angle not OK\n"
        if not top_rail_added_length_flag:
            result += "top_rail_added_length not OK\n"
        if result == "":
            result="ALL OK"
        return result
        
    def compare_para_in_range(self, range, valueToCheck):
        lower=range[0]
        upper=range[1]
        flag = True if (lower <= valueToCheck and upper >= valueToCheck) else False
        return flag

# Handler of HTTP requests / responses
class MyHandler(BaseHTTPRequestHandler):
    rule_checker = RuleChecker()
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
            
        elif path.find("/manufCheck") != -1:

            content_len = int(s.headers.get('Content-Length'))
            post_body = s.rfile.read(content_len)
            param_line = post_body.decode()
            print("Body: ", param_line)
            
            #Get the param value
            pairs = param_line.split("&")
            leg_length = pairs[0].split("=")
            back_height = pairs[1].split("=")
            seat_length = pairs[2].split("=")
            seat_width = pairs[3].split("=")
            back_tilt_angle = pairs[4].split("=")
            top_rail_added_length = pairs[5].split("=")
            
            parameterSet = [int(leg_length[1]), int(back_height[1]), int(seat_length[1]), int(seat_width[1]), int(back_tilt_angle[1]), int(top_rail_added_length[1])]
            check_result = s.rule_checker.check_manufacutrable(parameterSet)
            
            s.wfile.write(bytes(check_result, 'utf-8'))

if __name__ == '__main__':
    server_class = HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
