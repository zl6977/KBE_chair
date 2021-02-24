import requests 
import json

class Fuseki_updater():
    URL = "http://127.0.0.1:3030/kbe"

    """
    Use of POST with requests module:
    https://www.w3schools.com/python/ref_requests_post.asp
    """
    strTmplt_clearValue ="""
    PREFIX kbe:<http://www.my-kbe.com/shapes.owl#> 
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
    delete
    {
    ?anyvalue kbe:valueIs ?anyobj
    }
    WHERE 
    {
    ?anyvalue kbe:valueIs ?anyobj
    }
    """

    strTmplt_clearRange ="""
    PREFIX kbe:<http://www.my-kbe.com/shapes.owl#> 
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
    delete
    {
    ?anyvalue kbe:validRange ?anyobj
    } 
    WHERE 
    {
    ?anyvalue kbe:validRange ?anyobj
    }
    """

    strTmplt_insertParaSet ="""
    PREFIX kbe:<http://www.my-kbe.com/shapes.owl#> 
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
    insert 
    { 
    kbe:leg_length kbe:valueIs "500"^^<http://www.w3.org/2001/XMLSchema#float>.
    kbe:back_height kbe:valueIs "600"^^<http://www.w3.org/2001/XMLSchema#float>.
    kbe:seat_length kbe:valueIs "600"^^<http://www.w3.org/2001/XMLSchema#float>.
    kbe:seat_width kbe:valueIs "500"^^<http://www.w3.org/2001/XMLSchema#float>.
    kbe:back_tilt_angle kbe:valueIs "0"^^<http://www.w3.org/2001/XMLSchema#float>.
    kbe:top_rail_added_length kbe:valueIs "10"^^<http://www.w3.org/2001/XMLSchema#float>.
    } 
    WHERE 
    {}
    """

    strTmplt_insertParaRange ="""
    PREFIX kbe:<http://www.my-kbe.com/shapes.owl#> 
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
    insert 
    { 
    kbe:leg_length kbe:validRange "<leg_length_range>"^^<http://www.w3.org/2001/XMLSchema#string>.
    kbe:back_height kbe:validRange "<back_height_range>"^^<http://www.w3.org/2001/XMLSchema#string>.
    kbe:seat_length kbe:validRange "<seat_length_range>"^^<http://www.w3.org/2001/XMLSchema#string>.
    kbe:seat_width kbe:validRange "<seat_width_range>"^^<http://www.w3.org/2001/XMLSchema#string>.
    kbe:back_tilt_angle kbe:validRange "<back_tilt_angle_range>"^^<http://www.w3.org/2001/XMLSchema#string>.
    kbe:top_rail_added_length kbe:validRange "<top_rail_added_length_range>"^^<http://www.w3.org/2001/XMLSchema#string>.
    } 
    WHERE 
    {}
    """

    strTmplt_getValue ="""
    PREFIX kbe:<http://www.my-kbe.com/shapes.owl#> 
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
    select ?sub ?obj 
    WHERE 
    {
        ?sub kbe:valueIs ?obj 
    }
    """

    strTmplt_getRange ="""
    PREFIX kbe:<http://www.my-kbe.com/shapes.owl#> 
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
    select ?sub ?obj 
    WHERE 
    {
        ?sub kbe:validRange ?obj 
    }
    """

    def insert_paraSet(s, string_InsertPSet):
        # defining a query params 
        clearKB = {'update': s.strTmplt_clearValue} 
        insertvalue = {'update': string_InsertPSet} 
        
        # sending get request and saving the response as response object 
        r = requests.post(url = s.URL+"/update", data = clearKB) 
        r = requests.post(url = s.URL+"/update", data = insertvalue) 

        #Checking the result
        print(r.text)
        
    def insert_paraRange(s, string_InsertPRng):
        # defining a query params 
        clearKB = {'update': s.strTmplt_clearRange} 
        insertvalue = {'update': string_InsertPRng} 
        
        # sending get request and saving the response as response object 
        r = requests.post(url = s.URL+"/update", data = clearKB) 
        r = requests.post(url = s.URL+"/update", data = insertvalue) 

        #Checking the result
        if r.text.find("Update succeeded") != -1:
            print("insert to fuseki successful")
        
    def getQuery_paraSet(s, string_getValue):
        # defining a query params 
        query = {'query': string_getValue}
        # sending get request and saving the response as response object 
        r = requests.post(url = s.URL, data = query)
        #Checking the result
        jsonReturned = r.text
        # print(jsonReturned)
        y = json.loads(jsonReturned)
        # print(y)
        # print(y["results"]["bindings"][0]["sub"]["value"])
        # print(y["results"]["bindings"][0]["obj"]["value"])
        dicToReturn={}
        for i in range(6):
            paraName = y["results"]["bindings"][i]["sub"]["value"].split("#")[1]
            paraValue = y["results"]["bindings"][i]["obj"]["value"]
            dicToReturn[paraName] = paraValue
        # print(listToReturn[0][1])
        return dicToReturn
        
    def getQuery_paraRange(s, string_getRange):
        # defining a query params 
        query = {'query': string_getRange}
        # sending get request and saving the response as response object 
        r = requests.post(url = s.URL, data = query)
        #Checking the result
        jsonReturned = r.text
        # print(jsonReturned)
        y = json.loads(jsonReturned)
        # print(y)
        # print(y["results"]["bindings"][0]["sub"]["value"])
        # print(y["results"]["bindings"][0]["obj"]["value"])
        dicToReturn={}
        for i in range(6):
            paraName = y["results"]["bindings"][i]["sub"]["value"].split("#")[1]
            paraValue = y["results"]["bindings"][i]["obj"]["value"]
            dicToReturn[paraName] = paraValue
        # print(listToReturn[0][1])
        return dicToReturn
    
if __name__ == '__main__':
    fu=Fuseki_updater()
    
    fu.insert_paraRange(fu.strTmplt_insertParaRange)
    thisdic = fu.getQuery_paraRange(fu.strTmplt_getRange)
    # leg_length = thisdic["leg_length"]
    # back_height = thisdic["back_height"]
    # seat_length = thisdic["seat_length"]
    # seat_width = thisdic["seat_width"]
    # back_tilt_angle = thisdic["back_tilt_angle"]
    # top_rail_added_length = thisdic["top_rail_added_length"]
    
    leg_length_range = [0,0]
    leg_length_range = [float(thisdic["leg_length"].split(",")[0]),float(thisdic["leg_length"].split(",")[1])]
    
    print(leg_length_range)
