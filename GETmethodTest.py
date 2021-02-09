import requests
# sending get request and saving the response as response object
# URL_post="http://127.0.0.1:1234/orderChair?"
# # URL_get="http://127.0.0.1:1234/zzztest?"
# PARAMS="leg_length=500&back_height=600&seat_length=600&seat_width=500&back_tilt_angle=5&top_rail_added_length=100"
# #http://127.0.0.1:1234/zzztest?leg_length=600&back_height=600&seat_length=600&seat_width=500&back_tilt_angle=5&top_rail_added_length=10
# r = requests.post(url = URL_post, data = PARAMS)
# # r = requests.get(url = URL_get, params = PARAMS)
# #Checking the result
# print("Result:\n", r.text)
# # Parse the string r.text
# # index_tmp = r.text.rfind("lbs.") #the last "lbs." as keyword to find the "Adjusted ASD Capacity"
# # string_result = r.text[index_tmp-5 : index_tmp]
# # string_tmp = ""


# httpTest.py 
# import requests

#the required first parameter of the 'get' method is the 'url':
url = 'http://127.0.0.1:4321/manufCheck'
# x = requests.post(url, data = 'a=1111&b=1234&c=1500&d=1600')

# #print the response text (the content of the requested file):
# print(x.text)

dataToSend = "leg_length=600&back_height=600&seat_length=600&seat_width=500&back_tilt_angle=5&top_rail_added_length=10"
x = requests.post(url, data = dataToSend)
#print the response text (the content of the requested file):
print(x.text)