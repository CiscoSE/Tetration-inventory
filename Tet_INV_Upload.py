from tetpyclient import MultiPartOption, RestClient
import json

API_ENDPOINT="https://your-url"

#__sources__ = "Chris McHenry, Robert Bukosfer, and Tetration OpenAPI documentation"
#__copyright__ = "Copyright (c) 2018 Cisco and/or its affiliates."
#__license__ = "Cisco Sample Code License, Version 1.0"

# ``verify`` is an optional param to disable SSL server authentication.
# By default, |product| appliance dashboard IP uses self signed cert after
# deployment. Hence, ``verify=False`` might be used to disable server
# authentication in SSL for API clients. If users upload their own
# certificate to |product| appliance (from ``Settings > Company`` Tab)
# which is signed by their enterprise CA, then server side authentication
# should be enabled.
# credentials.json looks like:
# {
#   "api_key": "<hex string>",
#   "api_secret": "<hex string>"
# }


# followed by API calls, for example API to retrieve list of agents.
# API can be passed /openapi/v1/sensors or just /sensors.


def main():
    restclient = RestClient(API_ENDPOINT,
                credentials_file='api_credentials.json',
                verify=False)


    file_path = '/your-path-to-file/upload.csv'
    root_app_scope_name = 'your-root-scope'
    req_payload = [MultiPartOption(key='X-Tetration-Oper', val='add')]
    restclient.upload(file_path, '/assets/cmdb/upload/' + root_app_scope_name, req_payload)

    # Basic Error handling
    if resp.status_code != 200:
        print("Unsuccessful request returned code: {} , response: {}".format(resp.status_code, resp.text))
        exit(-1)
    results = resp.json()

    # check if results were returned, if so print them out,
    #  sometimes the list is inside the json as result other times raw return.
    if hasattr(results, 'results'):
        print(json.dumps(results["results"], indent=2))
    else:
        print(json.dumps(results, indent=2))
    return

if __name__ == '__main__':
    main()
