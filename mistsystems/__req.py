import logging
import requests
from requests.exceptions import HTTPError

import json



class Req:

    def __init__(self):
        self.host = ""
        self.session = requests.session()
        self.privileges = ""


    def _url(self, uri):
        """Generate the url with the host (in the object) and the uri
        Params: uri
        Return: url"""
        return "https://{0}{1}".format(self.host, uri)


    def _response(self, resp, uri="", multi_pages_result=None):
        if resp.status_code == 200:
            if multi_pages_result == None:
                result = resp.json()
            else:
                result = multi_pages_result
            error = ""
            logging.debug("Response Status Code: {0}".format(resp.status_code))
        else:
            result = ""
            error = resp.json()
            logging.debug("Response Status Code: {0}".format(resp.status_code))
            logging.debug("Response: {0}".format(error))
        return {"result": result, "status_code": resp.status_code, "error": error, "uri":uri}

    def mist_get(self, uri, query={}, page=None, limit=None):
        """GET HTTP Request
        Params:
            uri: String (ex: /api/v1/self)
            query: Dict (HTTP Query)
            page: Int (pagination page)
            limit: Int (pagination limit)
        Return: HTTP response"""
        try:
            url = self._url(uri)
            html_query = "?"
            if not query == {}:
                for query_param in query:
                    html_query += "{0}={1}&".format(query_param, query[query_param])
            if limit: html_query += "limit={0}&".format(limit)
            if page: html_query += "page={0}".format(page)
            url += html_query
            logging.debug("Request > GET {0}".format(url))
            resp = self.session.get(url)
            resp.raise_for_status()
        except HTTPError as http_err:
            logging.error(f'HTTP error occurred: {http_err}')  # Python 3.6
            logging.error(f'HTTP error description: {resp.json()}')
        except Exception as err:
            logging.error(f'Other error occurred: {err}')  # Python 3.6
        else:
            if "X-Page-Limit" in resp.headers:
                content = resp.json()
                x_page_limit = int(resp.headers["X-Page-Limit"])
                x_page_page = int(resp.headers["X-Page-Page"])
                x_page_total = int(resp.headers["X-Page-Total"])
                if x_page_limit * x_page_page < x_page_total:
                    content+=self.mist_get(uri, query, page + 1, limit)["result"]
                return self._response(resp, uri, content)
            else:
                return self._response(resp, uri)

    def mist_post(self, uri, body={}):
        """POST HTTP Request
        Params:
            uri: String (ex: /api/v1/self)
            body: Dict (HTTP Body)
        Return: HTTP response"""
        try:
            url = self._url(uri)
            headers = {'Content-Type': "application/json"}
            logging.debug("Request > POST {0}".format(url))
            logging.debug("Request body: \r\n{0}".format(body))
            if type(body) == str:
                resp = self.session.post(url, data=body, headers=headers)
            elif type(body) == dict:
                resp = self.session.post(url, json=body, headers=headers)
            else:
                resp = self.session.post(url, json=body, headers=headers)
            resp.raise_for_status()
        except HTTPError as http_err:
            logging.error(f'HTTP error occurred: {http_err}')  # Python 3.6
            logging.error(f'HTTP error description: {resp.json()}')
        except Exception as err:
            logging.error(f'Other error occurred: {err}')  # Python 3.6
        else:
            return self._response(resp, uri)

    def mist_put(self, uri, body={}):
        """PUT HTTP Request
        Params:
            uri: String (ex: /api/v1/self)
            body: Dict (HTTP Body)
        Return: HTTP response"""
        try:
            url = self._url(uri)
            logging.debug("Request > PUT {0}".format(url))
            logging.debug("Request body: \r\n{0}".format(body))
            if type(body) == str:
                resp = self.session.put(url, data=body)
            elif type(body) == dict:
                resp = self.session.put(url, json=body)
            else:
                resp = self.session.put(url, json=body)
            resp.raise_for_status()
        except HTTPError as http_err:
            logging.error(f'HTTP error occurred: {http_err}')  # Python 3.6
            logging.error(f'HTTP error description: {resp.json()}')
        except Exception as err:
            logging.error(f'Other error occurred: {err}')  # Python 3.6
        else:
            return self._response(resp, uri)


    def mist_delete(self, uri):
        """DELETE HTTP Request
        Params:
            uri: String (ex: /api/v1/self)
        Return: HTTP response"""
        try:
            url = self._url(uri)
            logging.debug("Request > DELETE {0}".format(url))
            resp = self.session.delete(url)
            resp.raise_for_status()
        except HTTPError as http_err:
            logging.error(f'HTTP error occurred: {http_err}')  # Python 3.6
        except Exception as err:
            logging.error(f'Other error occurred: {err}')  # Python 3.6
        else:
            return self._response(resp, uri)


    def mist_post_file(self, uri, files=None):
        """POST HTTP Request with file
        Params:
            uri: String (ex: /api/v1/self)
            files: String (path to the files)
        Return: HTTP response"""
        try:
            url = self._url(uri)
            logging.debug("Request > POST {0}".format(url))
            resp = self.session.post(url, files=files)
            resp.raise_for_status()
        except HTTPError as http_err:
            logging.error(f'HTTP error occurred: {http_err}')  # Python 3.6
            logging.error(f'HTTP error description: {resp.json()}')
            return resp
        except Exception as err:
            logging.error(f'Other error occurred: {err}')  # Python 3.6
        else:
            return self._response(resp, uri)
