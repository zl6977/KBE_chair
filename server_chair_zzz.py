#HTTP Server template / Chair example

from http.server import BaseHTTPRequestHandler, HTTPServer
import os, requests
from os import curdir, sep

HOST_NAME = '10.24.10.83' 
PORT_NUMBER = 1234

class ParameterSet():
    leg_length = ["leg_length","500"]
    back_height = ["back_height","600"]
    seat_length = ["seat_length","600"]
    seat_width = ["seat_width","500"]
    back_tilt_angle = ["back_tilt_angle","0"]
    top_rail_added_length = ["top_rail_added_length","10"]
    def loadInput(s,pairs):
        #pairs is list[6] of string like : [leg_length=500]*6
        s.leg_length = pairs[0].split("=")
        s.back_height = pairs[1].split("=")
        s.seat_length = pairs[2].split("=")
        s.seat_width = pairs[3].split("=")
        s.back_tilt_angle = pairs[4].split("=")
        s.top_rail_added_length = pairs[5].split("=")

# Handler of HTTP requests / responses
class MyHandler(BaseHTTPRequestHandler):
    Html_orderChair="""
<html>
<body>
    <h2>Chair</h2>
    <form action="/orderChair" method="post"> <img src="<imgURI>" alt="demo" style="float:right;width:983px;height:564px;">
        <label for="leg_length">leg_length:</label>
        <br>
        <input type="text" id="leg_length" name="leg_length" value="<leg_length>">
        <br>
        <br>
        <label for="back_height">back_height</label>
        <br>
        <input type="text" id="back_height" name="back_height" value="<back_height>">
        <br>
        <br>
        <label for="seat_length">seat_length</label>
        <br>
        <input type="text" id="seat_length" name="seat_length" value="<seat_length>">
        <br>
        <br>
        <label for="seat_width">seat_width</label>
        <br>
        <input type="text" id="seat_width" name="seat_width" value="<seat_width>">
        <br>
        <br>
        <label for="back_tilt_angle">back_tilt_angle</label>
        <br>
        <input type="text" id="back_tilt_angle" name="back_tilt_angle" value="<back_tilt_angle>">
        <br>
        <br>
        <label for="top_rail_added_length">top_rail_added_length</label>
        <br>
        <input type="text" id="top_rail_added_length" name="top_rail_added_length" value="<top_rail_added_length>">
        <br>
        <br>
        <input type="submit" value="Load Default" formaction="/orderChair" formmethod="get">
        <input type="submit" value="Submit"> </form>
        <Placeholder for manuf check result>
</body>
</html>
"""
    markToReplace = "<Placeholder for manuf check result>"
    imgURI = "https://raw.githubusercontent.com/zl6977/KBE_chair/main/chair_demo.png"
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
    def do_GET(s):
        """Respond to a GET request."""
        # Check what is the path
        path = s.path
        if path == "/" or path.find("/orderChair") != -1:
            #Get the param value
            pSet = ParameterSet()
            
            htmlToSend = s.Html_orderChair
            htmlToSend = htmlToSend.replace("<imgURI>", s.imgURI)
            htmlToSend = htmlToSend.replace("<leg_length>", str(pSet.leg_length[1]))
            htmlToSend = htmlToSend.replace("<back_height>", str(pSet.back_height[1]))
            htmlToSend = htmlToSend.replace("<seat_length>", str(pSet.seat_length[1]))
            htmlToSend = htmlToSend.replace("<seat_width>", str(pSet.seat_width[1]))
            htmlToSend = htmlToSend.replace("<back_tilt_angle>", str(pSet.back_tilt_angle[1]))
            htmlToSend = htmlToSend.replace("<top_rail_added_length>", str(pSet.top_rail_added_length[1]))
            #send response for dynamic html
            s.send_response(200)
            s.send_header("Content-type", "text/html")
            s.end_headers()
            s.wfile.write(bytes(htmlToSend, 'utf-8'))
        elif path.find("/zzztest") != -1:
            param_line=path
            print("Body: ", param_line)
            
            #Get the param value
            pairs = param_line.split("&")
            leg_length = pairs[0].split("=")
            back_height = pairs[1].split("=")
            seat_length = pairs[2].split("=")
            seat_width = pairs[3].split("=")
            back_tilt_angle = pairs[4].split("=")
            top_rail_added_length = pairs[5].split("=")
            
            htmlToSend = s.Html_orderChair
            htmlToSend = htmlToSend.replace("<imgURI>", s.imgURI)
            htmlToSend = htmlToSend.replace("<leg_length>", str(leg_length[1]))
            htmlToSend = htmlToSend.replace("<back_height>", str(back_height[1]))
            htmlToSend = htmlToSend.replace("<seat_length>", str(seat_length[1]))
            htmlToSend = htmlToSend.replace("<seat_width>", str(seat_width[1]))
            htmlToSend = htmlToSend.replace("<back_tilt_angle>", str(back_tilt_angle[1]))
            htmlToSend = htmlToSend.replace("<top_rail_added_length>", str(top_rail_added_length[1]))
            update_template(leg_length[1],back_height[1],seat_length[1],seat_width[1],back_tilt_angle[1],top_rail_added_length[1])
            #send response for dynamic html
            s.send_response(200)
            s.send_header("Content-type", "text/html")
            s.end_headers()
            s.wfile.write(bytes(htmlToSend, 'utf-8'))

        #send response for other media
        # https://github.com/tanzilli/playground/blob/master/python/httpserver/example2.py
        try:
            #Check the file extension required and
            #set the right mime type
            sendReply = False
            if path.endswith(".html"):
                mimetype='text/html'
                sendReply = True
            if path.endswith(".jpg"):
                mimetype='image/jpg'
                sendReply = True
            if path.endswith(".png"):
                mimetype='image/png'
                sendReply = True
            if path.endswith(".gif"):
                mimetype='image/gif'
                sendReply = True
            if path.endswith(".js"):
                mimetype='application/javascript'
                sendReply = True
            if path.endswith(".css"):
                mimetype='text/css'
                sendReply = True

            if sendReply == True:
                #Open the static file requested and send it
                f = open(curdir + sep + path,"rb") 
                # print(curdir + sep + path)
                s.send_response(200)
                s.send_header("Content-type", mimetype)
                s.end_headers()
                s.wfile.write(f.read())
                f.close()
            return
        except IOError:
            s.send_error(404,'File Not Found: %s' % path)
            
    def do_POST(s):
        # Check what is the path
        path = s.path
        print("Path: ", path)
        if path.find("/orderChair") != -1:
            content_len = int(s.headers.get('Content-Length'))
            post_body = s.rfile.read(content_len)
            param_line = post_body.decode()
            print("Body: ", param_line)
            
            #Get the param value
            pairs = param_line.split("&")
            pSet = ParameterSet()
            pSet.loadInput(pairs)
            
            htmlToSend = s.Html_orderChair
            htmlToSend = htmlToSend.replace("<leg_length>", str(pSet.leg_length[1]))
            htmlToSend = htmlToSend.replace("<back_height>", str(pSet.back_height[1]))
            htmlToSend = htmlToSend.replace("<seat_length>", str(pSet.seat_length[1]))
            htmlToSend = htmlToSend.replace("<seat_width>", str(pSet.seat_width[1]))
            htmlToSend = htmlToSend.replace("<back_tilt_angle>", str(pSet.back_tilt_angle[1]))
            htmlToSend = htmlToSend.replace("<top_rail_added_length>", str(pSet.top_rail_added_length[1]))
            
            strToReplace = '<p>The following parameters have arrived: ' \
                                + pSet.leg_length[1] + ', ' + pSet.back_height[1] + ', ' \
                                + pSet.seat_length[1] + ', ' + pSet.seat_width[1] + ', ' \
                                + pSet.back_tilt_angle[1] +', ' + pSet.top_rail_added_length[1] + '</p>\n'
            #manufacurable check-query the result from the manufChecker.py server
            dataToSend = [pSet.leg_length,pSet.back_height,pSet.seat_length,
                            pSet.seat_width,pSet.back_tilt_angle,pSet.top_rail_added_length]
            rulecheckResult = check_manufacutrable("http://127.0.0.1:4321/manufCheck", dataToSend)
            
            strToReplace += '<p style="color:DodgerBlue;">The rule check result: <br>' + rulecheckResult[1] + '</p>'
            htmlToSend = htmlToSend.replace(s.markToReplace, strToReplace)
            
            if rulecheckResult[0]:
                update_template(pSet.leg_length[1], pSet.back_height[1], pSet.seat_length[1],
                                pSet.seat_width[1], pSet.back_tilt_angle[1], pSet.top_rail_added_length[1])
                try:
                    result = requests.get("http://127.0.0.1:54321/exportImage", params = "imgName=KBEChair.png")
                    imgURITMP = result.text
                except requests.exceptions.ConnectionError:
                    imgURITMP = s.imgURI
                    print("ConnectionError found")
                htmlToSend = htmlToSend.replace("<imgURI>", imgURITMP)
            else:
                htmlToSend = htmlToSend.replace("<imgURI>", s.imgURI)
            
            s.send_response(200)
            s.send_header("Content-type", "text/html")
            s.end_headers()
            s.wfile.write(bytes(htmlToSend, 'utf-8'))

def update_template(leg_length,back_height,seat_length,seat_width,back_tilt_angle,top_rail_added_length):
    f = open(os.path.dirname(os.path.abspath(__file__))+"\\templates\\chair_zzz.dfa","r")
    fileContent = f.read()
    f.close()

    fileContent = fileContent.replace("<PARA_leg_length>",str(leg_length))
    fileContent = fileContent.replace("<PARA_leg_back_height>",str(back_height))
    fileContent = fileContent.replace("<PARA_seat_length>",str(seat_length))
    fileContent = fileContent.replace("<PARA_seat_width>",str(seat_width))
    fileContent = fileContent.replace("<PARA_back_tilt_angle>",str(back_tilt_angle))
    fileContent = fileContent.replace("<PARA_top_rail_added_length>",str(top_rail_added_length))

    ftowrite = open(os.path.dirname(os.path.abspath(__file__))+"\\chair_zzz.dfa","w")
    ftowrite.write(fileContent)
    ftowrite.close()
    
def check_manufacutrable(url, dataToSend):
    x = requests.post(url, data = dataToSend)
    #print the response text (the content of the requested file):
    resultToReturn = [False,""]
    if x.text == "ALL OK":
        resultToReturn = [True, x.text]
    else: resultToReturn = [False, x.text]
    return resultToReturn

if __name__ == '__main__':
    server_class = HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
