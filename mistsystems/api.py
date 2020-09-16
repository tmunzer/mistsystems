'''
Written by: Thomas Munzer (tmunzer@juniper.net)
Github repository: https://github.com/tmunzer/mistsystems/
'''
import logging
import requests
import json
import weakref
from getpass import getpass

from mistsystems.__req import Req
from mistsystems.models.privileges import Privileges

from mistsystems.requests.api_calls import Orgs, Sites


clouds = [
    {
        "short": "US",
        "host": "api.mist.com",
        "cookies_ext": ""
    },
    {
        "short": "EU",
        "host": "api.eu.mist.com",
        "cookies_ext": ".eu"
    },
    {
        "short": "GCP",
        "host": "api.gc1.mist.com",
        "cookies_ext": ".gc1"
    }
]

#### PARAMETERS #####


class MistSystems():
    """
    Initialize the Mist session, and validate the credentials. The session information can be passed as parameters,
    loaded from the config file, or loaded from a saved session.
    Parameters:
        host: String (api.mist.com, api.eu.mist.com, ...)
        email: String (user email for authentication)
        password: String (user password to be used with the email address)
        apitoken: String (apitoken for authentication, instead of login/pwd)
        session_file: String (file containing a previous saved session)
        settings_file: String (file containing configuration. Only used if host and email/pwd or apitoken are not specified)
        auto_login: Boolean (if the script has to validate the credentials automatically)
    """

    def __init__(self, host=None, email="", password="", apitoken=None, session_file=None, settings_file=None, auto_login=True):
        self._session = _MistSession(
            host, email, password, apitoken, session_file, settings_file, auto_login)
        self.privileges = Privileges(self._session.privileges)
        self.orgs = Orgs(self._session)
        self.sites = Sites(self._session)

    def __str__(self):
        return self._session.__str__()

    def login(self):
        if self._session.login():
            self.privileges = Privileges(self._session.privileges)

    def logout(self):
        if self._session.logout():
            self.privileges = []


class _MistSession(Req):
    """
    Initialize the Mist session, and validate the credentials. The session information can be passed as parameters,
    loaded from the config file, or loaded from a saved session.
    Parameters:
        host: String (api.mist.com, api.eu.mist.com, ...)
        email: String (user email for authentication)
        password: String (user password to be used with the email address)
        apitoken: String (apitoken for authentication, instead of login/pwd)
        session_file: String (file containing a previous saved session)
        settings_file: String (file containing configuration. Only used if host and email/pwd or apitoken are not specified)
        auto_login: Boolean (if the script has to validate the credentials automatically)
    """

    def __init__(self, host=None, email="", password="", apitoken=None, session_file=None, settings_file=None, auto_login=True):

        self.session = requests.session()
        # user and https session parameters
        self.host = host
        self.email = email
        self.password = password
        self.privileges = []
        self.tags = []
        self.authenticated = False
        self.csrftoken = ""
        self.apitoken = apitoken
        if session_file != None:
            self._restore_session(session_file)
        if self.authenticated == False:
            self._create_session(settings_file)
        # Try to log in
        if (auto_login):
            self.login()

    def login(self):
        """
        Required when "auto_login=False" is used. Will validate the credentials and retrieve the session cookies when login/pwd is used.
        """
        if self.email and self.password:
            logging.info("Login/Pwd authentication used")
            uri = "/api/v1/login"
            body = {
                "email": self.email,
                "password": self.password
            }
            resp = self.session.post(self._url(uri), json=body)
            if resp.status_code == 200:
                logging.info("authenticated")
                self._set_session(True)
            elif resp.status_code == 400:
                logging.error("not authenticated: {0}".format(
                    resp.json["detail"]))
                return False
            else:
                try:
                    logging.error(resp.json["detail"])
                except:
                    logging.error(resp.text)
                finally:
                    return False
        # if successfuly authenticated or API Token used
        if (self.get_auth_status()):
            return self.getself()
        # if authentication failed, exit with error code 255
        else:
            logging.error("Authentication failed... Exiting...")

    def logout(self):
        """
        Logout from the Mist Cloud. This will mainly clear the session information.
        """
        uri = "/api/v1/logout"
        resp = self.mist_post(uri)
        if resp['status_code'] == 200:
            logging.warning("Logged out")
            self._set_session(False)
            self.privileges = []
            return True
        else:
            try:
                logging.error(resp.json()["detail"])
            except:
                logging.error(resp.text)

    def __str__(self):
        fields = ["email", "first_name", "last_name", "phone", "via_sso",
                  "privileges", "session_expiry", "tags", "authenticated"]
        string = ""
        for field in fields:
            if hasattr(self, field) and getattr(self, field) != "":
                string += "{0}:\r\n".format(field)
                if field == "privileges":
                    string += Privileges(self.privileges).__str__()
                    string += "\r\n"
                elif field == "tags":
                    for tag in self.tags:
                        string += "  -  {0}\r\n".format(tag)
                elif field == "authenticated":
                    string += "{0}\r\n".format(self.get_auth_status())
                else:
                    string += "{0}\r\n".format(getattr(self, field))
                string += "\r\n"
        return string

    def _restore_session(self, file):
        logging.debug("Loading session...")
        try:
            with open(file, 'r') as f:
                for line in f:
                    line = line.replace('\n', '')
                    line = json.loads(line)
                    if "cookie" in line:
                        cookie = line["cookie"]
                        self.session.cookies.set(**cookie)
                    elif "host" in line:
                        self.host = line["host"]
            logging.info("Session restored from file {0}".format(file))
            logging.debug("Cookies > {0}".format(self.session.cookies))
            logging.debug("Host > {0}".format(self.host))
        except:
            logging.warning("Unable to load session...")

    def _select_cloud(self):
        loop = True
        resp = "x"
        while loop:
            i = 0
            print("\r\nAvailable Clouds:")
            for cloud in clouds:
                print("{0}) {1} (host: {2})".format(
                    i, cloud["short"], cloud["host"]))
                i += 1
            resp = input(
                "\r\nSelect a Cloud (0 to {0}, or q to exit): ".format(i))
            if resp == "q":
                exit(0)
            elif resp == "i":
                return "api.mistsys.com"
            else:
                try:
                    resp_num = int(resp)
                    if resp_num >= 0 and resp_num <= i:
                        loop = False
                        return clouds[resp_num]["host"]
                    else:
                        print(
                            "Please enter a number between 0 and {0}.".format(i))
                except:
                    print("Please enter a number.")

    def _create_session(self, settings_file=None):
        self.session = requests.session()

        if settings_file:
            try:
                with open(settings_file, 'r') as credentials:
                    logging.info("Configuration file found.")
                    if "host" in credentials:
                        self.host = credentials["host"]
                    if "apitoken" in credentials:
                        self.apitoken = credentials["apitoken"]
                    elif "email" in credentials:
                        self.email = credentials["email"]
                        if "password" in credentials:
                            self.password = credentials["password"]
                    else:
                        logging.error(
                            "Credentials invalid... Can't use the information from config.py...")
                        raise ValueError
            except:
                logging.info(
                    "Unable to load the configuration file. Asking for Login/Password")
        if not self.host:
            self.host = self._select_cloud()
        if self.apitoken:
            self._set_apitoken(self.apitoken)
        else:
            if not self.email:
                self.email = input("Login: ")
            if self.email and not self.password:
                self.password = getpass("Password: ")

    def _set_apitoken(self, apitoken):
        logging.info("API Token authentication used")
        self.apitoken = apitoken
        self.session.headers.update({'Authorization': "Token " + apitoken})

    def _set_session(self, value):
        if value == True:
            self.authenticated = True
            if not self.apitoken:
                try:
                    cookies_ext = next(item["cookies_ext"]
                                       for item in clouds if item["host"] == self.host)
                except:
                    cookies_ext = ""
                self.csrftoken = self.session.cookies['csrftoken' + cookies_ext]
                self.session.headers.update({'X-CSRFToken': self.csrftoken})
        elif value == False:
            self.authenticated = False
            self.csrftoken = ""
            self.session = requests.session()

    def get_auth_status(self):
        """
        Return the current authentication status.
        Return True if login/pwd session is established or API Token is used
        """
        return self.authenticated or self.apitoken != None

    def get_api_tokens(self):
        """
        Retrieve the user's API token from the Mist Cloud
        """
        uri = "https://{0}/api/v1/self/apitokens".format(self.host)
        resp = self.session.get(uri)
        return resp

    def create_api_token(self):
        """
        Create a new API token for the current user
        """
        uri = "https://{0}/api/v1/self/apitokens".format(self.host)
        resp = self.session.post(uri)
        return resp

    def delete_api_token(self, token_id):
        """
        Delete the specified user's API token from the Mist Cloud
        parameter:
            token_id: String (ID of the API token to remove. can be retrieved with get_api_tokens() function)
        """
        uri = "https://{0}/api/v1/self/apitokens/{1}".format(
            self.host, token_id)
        resp = self.session.delete(uri)
        return resp

    def _two_factor_authentication(self, two_factor):
        uri = "/api/v1/login"
        body = {
            "email": self.email,
            "password": self.password,
            "two_factor": two_factor
        }
        resp = self.session.post(self._url(uri), json=body)
        if resp.status_code == 200:
            logging.info("2FA authentication successed")
            self._set_session(True)
            return True
        else:
            logging.error("2FA authentication failed")
            logging.error("Error code: {0}".format(resp.status_code))
            return False

    def _two_factor_authentication_token(self, two_factor):
        uri = "/api/v1/login/two_factor"
        body = {"two_factor": two_factor}
        resp = self.session.post(self._url(uri), json=body)
        if resp.status_code == 200:
            logging.info("2FA authentication successed")
            self._set_session(True)
            return True
        else:
            logging.error("2FA authentication failed")
            logging.error("Error code: {0}".format(resp.status_code))
            exit(255)
            return False

    def getself(self):
        """
        Retrieve information about the current user and store them in the current object.
        Params: none
        Return: none
        """
        uri = "/api/v1/self"
        resp = self.mist_get(uri)
        if resp != None and 'result' in resp:
            # Deal with 2FA if needed
            if (
                "two_factor_required" in resp['result']
                and resp['result']['two_factor_required'] == True
                and "two_factor_passed" in resp['result']
                and resp['result']['two_factor_passed'] == False
            ):
                two_factor = input("Two Factor Authentication code:")
                if (self.apitoken):
                    if (self._two_factor_authentication_token(two_factor) == True):
                        self.getself()
                elif (self._two_factor_authentication(two_factor) == True):
                    self.getself()
            # Get details of the account
            else:
                for key, val in resp['result'].items():
                    if key == "privileges":
                        self.privileges = resp['result']["privileges"]
                    if key == "tags":
                        for tag in resp['result']["tags"]:
                            self.tags.append(tag)
                    else:
                        setattr(self, key, val)
                return True
        else:
            logging.error("Authentication not valid...")
            resp = input(
                "Do you want to try with new credentials for {0} (y/N)? ".format(self.host))
            if resp.lower() == "y":
                self._create_session(settings_file=None)
                return self.getself()
            else:
                exit(0)

    def save_session(self, file_path="./session.py"):
        """
        Save the current session cookies to a file. Can be loaded afterward.
        Only useful with login/pwd
        parameter:
            file_path: String (path to the file where to store the session)
        """
        if self.apitoken != None:
            logging.error("API Token used. There is no cookies to save...")
        else:
            logging.warning(
                "This will save in clear text your session cookies!")
            sure = input("Are you sure? (y/N)")
            if sure.lower() == "y":
                with open(file_path, 'w') as f:
                    for cookie in self.session.cookies:
                        cookie_json = json.dumps(
                            {"cookie": {"domain": cookie.domain, "name": cookie.name, "value": cookie.value}})
                        f.write("{0}\r\n".format(cookie_json))
                    host = json.dumps({"host": self.host})
                    f.write("{0}\r\n".format(host))
                logging.info("session saved.")
