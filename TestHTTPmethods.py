import requests
method_list=['GET', 'POST', 'UPDATE', 'DELETE', 'PUT', 'TRACE', 'OPTIONS']
for method in method_list:
    req = requests.request(method, 'Enter any URL, which you want to test')
    print(method, req.status_code, req.reason, req.is_redirect, req.url, req.headers)

#if method == "TRACE" and "TRACE" in req.text:
    #print ("Cross Site Tracing  possible")
#else:
     #print("Not Possible")