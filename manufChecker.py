#HTTP Manufacturability Checker Server/ Chair example

from http.server import BaseHTTPRequestHandler, HTTPServer
import fuseki_updater

HOST_NAME = '127.0.0.1' 
PORT_NUMBER = 4321 # Maybe set this to 1234

class RuleChecker():
    leg_length_range = [500,1000]
    back_height_range = [400,1000]
    seat_length_range = [200,600]
    seat_width_range = [300,600]
    back_tilt_angle_range = [0,20]
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
            result += "leg_length not OK<br>"
        if not back_height_flag:
            result += "back_height not OK<br>"
        if not seat_length_flag:
            result += "seat_length not OK<br>"
        if not seat_width_flag:
            result += "seat_width not OK<br>"
        if not back_tilt_angle_flag:
            result += "back_tilt_angle not OK<br>"
        if not top_rail_added_length_flag:
            result += "top_rail_added_length not OK<br>"
        if result == "":
            result="ALL OK"
        return result
        
    def compare_para_in_range(self, range, valueToCheck):
        if valueToCheck.isnumeric():
            lower=range[0]
            upper=range[1]
            flag = True if (lower <= float(valueToCheck) and upper >= float(valueToCheck)) else False
        else:
            flag = False
        return flag
        
    def range_to_string(self, range):
        lower=float(range[0])
        upper=float(range[1])
        stringToReutrn = str(lower) +","+ str(upper)
        return stringToReutrn
        
    def string_to_range(self, string):
        # print(string,"\n")
        pair = string.split("%2C")
        # print(pair)
        lower=float(pair[0])
        upper=float(pair[1])
        rangeToReturn = [lower,upper]
        return rangeToReturn
        
    def dict_to_rangeList(self, dict):
        # print(dict)
        self.leg_length_range = [float(dict["leg_length"].split(",")[0]),float(dict["leg_length"].split(",")[1])]
        self.back_height_range = [float(dict["back_height"].split(",")[0]),float(dict["back_height"].split(",")[1])]
        self.seat_length_range = [float(dict["seat_length"].split(",")[0]),float(dict["seat_length"].split(",")[1])]
        self.seat_width_range = [float(dict["seat_width"].split(",")[0]),float(dict["seat_width"].split(",")[1])]
        self.back_tilt_angle_range = [float(dict["back_tilt_angle"].split(",")[0]),float(dict["back_tilt_angle"].split(",")[1])]
        self.top_rail_added_length_range = [float(dict["top_rail_added_length"].split(",")[0]),float(dict["top_rail_added_length"].split(",")[1])]
        print("range updated from fuseki")

# Handler of HTTP requests / responses
class MyHandler(BaseHTTPRequestHandler):
    rule_checker = RuleChecker()
    fskUpdater = fuseki_updater.Fuseki_updater()
    Html_setParamsIntervals="""
<html><body><h2>set parameters range</h2>
<form action="/setParamsIntervals" method="post">
<label for="leg_length_range">Set leg_length_range:</label><br>
<input type="text" id="leg_length_range" name="leg_length_range" value="<leg_length_range>"><br><br>
<label for="back_height_range">Set back_height_range:</label><br>
<input type="text" id="back_height_range" name="back_height_range" value="<back_height_range>"><br><br>
<label for="seat_length_range">Set seat_length_range:</label><br>
<input type="text" id="seat_length_range" name="seat_length_range" value="<seat_length_range>"><br><br>
<label for="seat_width_range">Set seat_width_range:</label><br>
<input type="text" id="seat_width_range" name="seat_width_range" value="<seat_width_range>"><br><br>
<label for="back_tilt_angle_range">Set back_tilt_angle_range:</label><br>
<input type="text" id="back_tilt_angle_range" name="back_tilt_angle_range" value="<back_tilt_angle_range>"><br><br>
<label for="top_rail_added_length_range">Set top_rail_added_length_range:</label><br>
<input type="text" id="top_rail_added_length_range" name="top_rail_added_length_range" value="<top_rail_added_length_range>"><br><br>
<input type="submit" value="Submit">
</form></body></html>
"""
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
    def do_GET(s):
        """Respond to a GET request."""
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        ruleCheckerTMP = s.rule_checker
        # Check what is the path
        path = s.path
        if path.find("/setParamsIntervals") != -1:
            #TODO - change HTML accordingly
            htmlToSend = s.Html_setParamsIntervals
            htmlToSend = htmlToSend.replace("<leg_length_range>",ruleCheckerTMP.range_to_string(ruleCheckerTMP.leg_length_range))
            htmlToSend = htmlToSend.replace("<back_height_range>",ruleCheckerTMP.range_to_string(ruleCheckerTMP.back_height_range))
            htmlToSend = htmlToSend.replace("<seat_length_range>",ruleCheckerTMP.range_to_string(ruleCheckerTMP.seat_length_range))
            htmlToSend = htmlToSend.replace("<seat_width_range>",ruleCheckerTMP.range_to_string(ruleCheckerTMP.seat_width_range))
            htmlToSend = htmlToSend.replace("<back_tilt_angle_range>",ruleCheckerTMP.range_to_string(ruleCheckerTMP.back_tilt_angle_range))
            htmlToSend = htmlToSend.replace("<top_rail_added_length_range>",ruleCheckerTMP.range_to_string(ruleCheckerTMP.top_rail_added_length_range))
            s.wfile.write(bytes(htmlToSend, 'utf-8'))
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
        ruleCheckerTMP = s.rule_checker
        fskUpdaterTMP = s.fskUpdater
        print("Path: ", path)
        if path.find("/setParamsIntervals") != -1:
            #TODO - set intervals for params
            content_len = int(s.headers.get('Content-Length'))
            post_body = s.rfile.read(content_len)
            param_line = post_body.decode()
            print("Body: ", param_line)
            
            #Get the param value from webpage
            pairs = param_line.split("&")
            ruleCheckerTMP.leg_length_range = ruleCheckerTMP.string_to_range(pairs[0].split("=")[1])
            ruleCheckerTMP.back_height_range = ruleCheckerTMP.string_to_range(pairs[1].split("=")[1])
            ruleCheckerTMP.seat_length_range = ruleCheckerTMP.string_to_range(pairs[2].split("=")[1])
            ruleCheckerTMP.seat_width_range = ruleCheckerTMP.string_to_range(pairs[3].split("=")[1])
            ruleCheckerTMP.back_tilt_angle_range = ruleCheckerTMP.string_to_range(pairs[4].split("=")[1])
            ruleCheckerTMP.top_rail_added_length_range = ruleCheckerTMP.string_to_range(pairs[5].split("=")[1])
            
            #store the range in fuseki server
            str_insertParaRange = fskUpdaterTMP.strTmplt_insertParaRange
            str_insertParaRange = str_insertParaRange.replace("<leg_length_range>",ruleCheckerTMP.range_to_string(ruleCheckerTMP.leg_length_range))
            str_insertParaRange = str_insertParaRange.replace("<back_height_range>",ruleCheckerTMP.range_to_string(ruleCheckerTMP.back_height_range))
            str_insertParaRange = str_insertParaRange.replace("<seat_length_range>",ruleCheckerTMP.range_to_string(ruleCheckerTMP.seat_length_range))
            str_insertParaRange = str_insertParaRange.replace("<seat_width_range>",ruleCheckerTMP.range_to_string(ruleCheckerTMP.seat_width_range))
            str_insertParaRange = str_insertParaRange.replace("<back_tilt_angle_range>",ruleCheckerTMP.range_to_string(ruleCheckerTMP.back_tilt_angle_range))
            str_insertParaRange = str_insertParaRange.replace("<top_rail_added_length_range>",ruleCheckerTMP.range_to_string(ruleCheckerTMP.top_rail_added_length_range))
            # print(str_insertParaRange)
            fskUpdaterTMP.insert_paraRange(str_insertParaRange)
            
            #update the webpage
            htmlToSend = s.Html_setParamsIntervals
            htmlToSend = htmlToSend.replace("<leg_length_range>",ruleCheckerTMP.range_to_string(ruleCheckerTMP.leg_length_range))
            htmlToSend = htmlToSend.replace("<back_height_range>",ruleCheckerTMP.range_to_string(ruleCheckerTMP.back_height_range))
            htmlToSend = htmlToSend.replace("<seat_length_range>",ruleCheckerTMP.range_to_string(ruleCheckerTMP.seat_length_range))
            htmlToSend = htmlToSend.replace("<seat_width_range>",ruleCheckerTMP.range_to_string(ruleCheckerTMP.seat_width_range))
            htmlToSend = htmlToSend.replace("<back_tilt_angle_range>",ruleCheckerTMP.range_to_string(ruleCheckerTMP.back_tilt_angle_range))
            htmlToSend = htmlToSend.replace("<top_rail_added_length_range>",ruleCheckerTMP.range_to_string(ruleCheckerTMP.top_rail_added_length_range))
            s.wfile.write(bytes(htmlToSend, 'utf-8'))
            
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
            
            parameterSet = [leg_length[1], back_height[1], seat_length[1], seat_width[1], back_tilt_angle[1], top_rail_added_length[1]]
            # parameterSet = [int(leg_length[1]), int(back_height[1]), int(seat_length[1]), int(seat_width[1]), int(back_tilt_angle[1]), int(top_rail_added_length[1])]
            
            #fetch the range in fuseki server
            dictOfRange = fskUpdaterTMP.getQuery_paraRange(fskUpdaterTMP.strTmplt_getRange)
            print(dictOfRange)
            #update the range in ruleCheckerTMP
            ruleCheckerTMP.dict_to_rangeList(dictOfRange)
            
            check_result = ruleCheckerTMP.check_manufacutrable(parameterSet)
            
            s.wfile.write(bytes(check_result, 'utf-8'))

if __name__ == '__main__':
    server_class = HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
