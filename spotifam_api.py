import fire
import requests

base_url = "https://api.spotifam.com"

class SpotifamAPI(object):

    def empty(object):
        result = requests.get(base_url)
        print result.text

    def getqueue(self, room_code):
        request_url = base_url + "/getqueue/?room_code=" + str(room_code)
        result = requests.get(request_url)
        print result.text

    def createroom(self, api_auth_token):
        request_url = base_url + "/createroom?auth_token=" + api_auth_token
        result = requests.get(request_url)
        print result.text

    def addsong(self, room_code, song_uid):
        request_url = base_url + "/addsong/"
        print "THIS IS NOT BUILT YET"


# RUN --------------------------------------------------------------------------

if __name__ == '__main__':
    fire.Fire(SpotifamAPI)
