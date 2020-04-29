import urllib.error
import urllib.request
import json
import ast


def go(date):
    data = {
        "Inputs": {
            "input1":
            [
                {
                    'Date': date,
                }
            ],
        },
        "GlobalParameters":  {}
    }

    body = str.encode(json.dumps(data))

    # Replace this with the URI and API Key for your web service
    url = 'https://ussouthcentral.services.azureml.net/subscriptions/b0707550dad348bf9bbedd4529b65e0f/services/a79ba95060bc4daf9e38871c2827928a/execute?api-version=2.0&format=swagger'
    api_key = '+Em94oRHVYYnoZqzd51CqAxxKPC2lFG58IdhV81jlNJtkz7csCgzF4p5VlIEpWd3HF1L+UAYpzMIOQWJg9b09w=='
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    # "urllib.request.Request(url, body, headers)" for Python 3.X
    req = urllib.request.Request(url, body, headers)
    print('DEBUG1')
    try:
        response = urllib.request.urlopen(req)
        result = response.read()
        print(result)
    # "urllib.error.HTTPError as error" for Python 3.X
    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))
        # Print the headers - they include the request ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(json.loads(error.read()))
    #
    result_str = result.decode()
    return ast.literal_eval(result_str)