import requests


class QueryDrill():
    auth_cookie = {}
    drill_base_url = ""

    def __init__(self, drill_base_url):
        self.drill_base_url = drill_base_url
        self.auth_cookies = self.auth_get_cookies()

    def auth_get_cookies(self):
        url = self.drill_base_url+"/j_security_check"

        payload = "j_username=mapr&j_password=ue3q8PjHQ%7DaqMDUH"
        headers = {
            'cache-control': "no-cache",
            'content-type': "application/x-www-form-urlencoded"
            }

        results = requests.request("POST", url, data=payload, headers=headers)
        if results.status_code != 200:
            raise requests.ConnectionError("Expected status code 200, but got {}".format(results.status_code))
        else:
            return results.cookies

    def run_query(self, query):
        return self._run_query(query, self.auth_cookies)

    def _run_query(self, query, auth_cookies):
        url = self.drill_base_url+"/query.json"

        payload = '{ "queryType" : "SQL", "query" : "'+query+'" }'
        headers = {
            'content-type': "application/json",
            'cache-control': "no-cache"
            }
        results = requests.request("POST", url, data=payload, headers=headers, cookies=auth_cookies)

        # if results.status_code != 200:
        #     raise requests.ConnectionError("Expected status code 200, but got {}".format(results.status_code))
        # else:
        return results.json()

if __name__ == "__main__":
    drill = QueryDrill("http://data-node002:8047")
    print drill.run_query("select * from `MDB.exponea`.`customers` limit 10")

