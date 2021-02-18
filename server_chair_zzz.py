#HTTP Server template / Chair example

from http.server import BaseHTTPRequestHandler, HTTPServer
import os, requests

HOST_NAME = '10.24.10.83' 
PORT_NUMBER = 1234

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
        if path.find("/") != -1 and len(path) == 1:
            s.wfile.write(bytes('<html><head><title>Cool interface.</title></head>', 'utf-8'))
            s.wfile.write(bytes("<body><p>Current path: " + path + "</p>", "utf-8"))
            s.wfile.write(bytes('<p><a style="font-size:100%;", href="'+str(HOST_NAME)+':'+str(PORT_NUMBER)+'/orderChair'+'">orderChair</a></p>',"utf-8"))
            s.wfile.write(bytes('</body></html>', "utf-8"))
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
            
            s.wfile.write(bytes('<html><body><h2>Chair</h2>', 'utf-8'))
            s.wfile.write(bytes('<form action="/orderChair" method="post">', 'utf-8'))
            
            s.wfile.write(bytes('<p>The following parameters have arrived: ' + str(leg_length[1]) + ', ' + str(back_height[1]) + ', ' + str(seat_length[1]) + ', ' + str(seat_width[1]) + ', ' +str(back_tilt_angle[1]) +', ' + str(top_rail_added_length[1]) + '</p>', 'utf-8'))
            
            s.wfile.write(bytes('<label for="leg_length">leg_length:</label><br>', 'utf-8'))
            s.wfile.write(bytes('<input type="text" id="leg_length" name="leg_length" value="' + str(leg_length[1]) + '"><br><br>', 'utf-8'))
            s.wfile.write(bytes('<label for="back_height">back_height</label><br>', 'utf-8'))
            s.wfile.write(bytes('<input type="text" id="back_height" name="back_height" value="' + str(back_height[1]) + '"><br><br>', 'utf-8'))
            s.wfile.write(bytes('<label for="seat_length">seat_length</label><br>', 'utf-8'))
            s.wfile.write(bytes('<input type="text" id="seat_length" name="seat_length" value="' + str(seat_length[1]) + '"><br><br>', 'utf-8'))
            s.wfile.write(bytes('<label for="seat_width">seat_width</label><br>', 'utf-8'))
            s.wfile.write(bytes('<input type="text" id="seat_width" name="seat_width" value="' + str(seat_width[1]) + '"><br><br>', 'utf-8'))
            s.wfile.write(bytes('<label for="back_tilt_angle">back_tilt_angle</label><br>', 'utf-8'))
            s.wfile.write(bytes('<input type="text" id="back_tilt_angle" name="back_tilt_angle" value="' + str(back_tilt_angle[1]) + '"><br><br>', 'utf-8'))
            s.wfile.write(bytes('<label for="top_rail_added_length">top_rail_added_length</label><br>', 'utf-8'))
            s.wfile.write(bytes('<input type="text" id="top_rail_added_length" name="top_rail_added_length" value="' + str(top_rail_added_length[1]) + '"><br><br>', 'utf-8'))
            
            s.wfile.write(bytes('<input type="submit" value="Submit">', 'utf-8'))
            s.wfile.write(bytes('</form></body></html>', 'utf-8'))
            
            update_template(leg_length[1],back_height[1],seat_length[1],seat_width[1],back_tilt_angle[1],top_rail_added_length[1])
#-------------
        elif path.find("/orderChair") != -1:
            s.wfile.write(bytes('<html><body><h2>Chair</h2>', 'utf-8'))
            s.wfile.write(bytes('<form action="/orderChair" method="post">', 'utf-8'))
            
            s.wfile.write(bytes('<img src="https://raw.githubusercontent.com/zl6977/KBE_chair/main/chair_demo.png" alt="demo" style="float:right;width:670px;height:464px;">', 'utf-8'))
            s.wfile.write(bytes('<label for="leg_length">leg_length:</label><br>', 'utf-8'))
            s.wfile.write(bytes('<input type="text" id="leg_length" name="leg_length" value="500"><br><br>', 'utf-8'))
            s.wfile.write(bytes('<label for="back_height">back_height</label><br>', 'utf-8'))
            s.wfile.write(bytes('<input type="text" id="back_height" name="back_height" value="600"><br><br>', 'utf-8'))
            s.wfile.write(bytes('<label for="seat_length">seat_length</label><br>', 'utf-8'))
            s.wfile.write(bytes('<input type="text" id="seat_length" name="seat_length" value="600"><br><br>', 'utf-8'))
            s.wfile.write(bytes('<label for="seat_width">seat_width</label><br>', 'utf-8'))
            s.wfile.write(bytes('<input type="text" id="seat_width" name="seat_width" value="500"><br><br>', 'utf-8'))
            s.wfile.write(bytes('<label for="back_tilt_angle">back_tilt_angle</label><br>', 'utf-8'))
            s.wfile.write(bytes('<input type="text" id="back_tilt_angle" name="back_tilt_angle" value="0"><br><br>', 'utf-8'))
            s.wfile.write(bytes('<label for="top_rail_added_length">top_rail_added_length</label><br>', 'utf-8'))
            s.wfile.write(bytes('<input type="text" id="top_rail_added_length" name="top_rail_added_length" value="10"><br><br>', 'utf-8'))
            
            s.wfile.write(bytes('<input type="submit" value="Load Default" formaction="/orderChair" formmethod="get">', 'utf-8'))
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
        if path.find("/orderChair") != -1:
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
            
            s.wfile.write(bytes('<html><body><h2>Chair</h2>', 'utf-8'))
            s.wfile.write(bytes('<form action="/orderChair" method="post">', 'utf-8'))
            
            s.wfile.write(bytes('<img src="https://raw.githubusercontent.com/zl6977/KBE_chair/main/chair_demo.png" alt="demo" style="float:right;width:670px;height:464px;">', 'utf-8'))
            s.wfile.write(bytes('<label for="leg_length">leg_length:</label><br>', 'utf-8'))
            s.wfile.write(bytes('<input type="text" id="leg_length" name="leg_length" value="' + str(leg_length[1]) + '"><br><br>', 'utf-8'))
            s.wfile.write(bytes('<label for="back_height">back_height</label><br>', 'utf-8'))
            s.wfile.write(bytes('<input type="text" id="back_height" name="back_height" value="' + str(back_height[1]) + '"><br><br>', 'utf-8'))
            s.wfile.write(bytes('<label for="seat_length">seat_length</label><br>', 'utf-8'))
            s.wfile.write(bytes('<input type="text" id="seat_length" name="seat_length" value="' + str(seat_length[1]) + '"><br><br>', 'utf-8'))
            s.wfile.write(bytes('<label for="seat_width">seat_width</label><br>', 'utf-8'))
            s.wfile.write(bytes('<input type="text" id="seat_width" name="seat_width" value="' + str(seat_width[1]) + '"><br><br>', 'utf-8'))
            s.wfile.write(bytes('<label for="back_tilt_angle">back_tilt_angle</label><br>', 'utf-8'))
            s.wfile.write(bytes('<input type="text" id="back_tilt_angle" name="back_tilt_angle" value="' + str(back_tilt_angle[1]) + '"><br><br>', 'utf-8'))
            s.wfile.write(bytes('<label for="top_rail_added_length">top_rail_added_length</label><br>', 'utf-8'))
            s.wfile.write(bytes('<input type="text" id="top_rail_added_length" name="top_rail_added_length" value="' + str(top_rail_added_length[1]) + '"><br><br>', 'utf-8'))
            
            s.wfile.write(bytes('<input type="submit" value="Load Default" formaction="/orderChair" formmethod="get">', 'utf-8'))
            s.wfile.write(bytes('<input type="submit" value="Submit">', 'utf-8'))
            
            # s.wfile.write(bytes('<p>The following parameters have arrived: ' 
                                # + str(leg_length[1]) + ', ' + str(back_height[1]) + ', ' 
                                # + str(seat_length[1]) + ', ' + str(seat_width[1]) + ', ' 
                                # +str(back_tilt_angle[1]) +', ' + str(top_rail_added_length[1]) + '</p>', 'utf-8'))
            s.wfile.write(bytes('<p>The following parameters have arrived: ' 
                                + leg_length[1] + ', ' + back_height[1] + ', ' 
                                + seat_length[1] + ', ' + seat_width[1] + ', ' 
                                + back_tilt_angle[1] +', ' + top_rail_added_length[1] + '</p>', 'utf-8'))
            #manufacurable check-query the result from the manufChecker.py server
            # dataToSend = "leg_length="+str(leg_length[1])+"&back_height="+str(back_height[1])+"&seat_length="+str(seat_length[1])
            # dataToSend += "&seat_width="+str(seat_width[1])+"&back_tilt_angle="+str(back_tilt_angle[1])+"&top_rail_added_length="+str(top_rail_added_length[1])
            dataToSend = [leg_length,back_height,seat_length,seat_width,back_tilt_angle,top_rail_added_length]
            rulecheckResult= check_manufacutrable("http://127.0.0.1:4321/manufCheck", dataToSend)
            s.wfile.write(bytes('<p style="color:DodgerBlue;">The rule check result: <br>' + rulecheckResult[1] + '</p>', 'utf-8'))
            if rulecheckResult[0]:
                update_template(leg_length[1],back_height[1],seat_length[1],seat_width[1],back_tilt_angle[1],top_rail_added_length[1])
            
            s.wfile.write(bytes('</form></body></html>', 'utf-8'))

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
