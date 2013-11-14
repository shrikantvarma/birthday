__author__ = 'i813463'


import facebook

#
#
#oauth_access_token = 'CAACEdEose0cBAODApiTtq0ADSasMdP2WW6y1TLafovYHziVMmAHY68aUZAQs0NCy80H9Fu0rZCSCShmwFOGeMrNFo6uyuNcMmxZAEy4EUaq1uZBe0zHqPZBBz7lIwFMmSMqHJZCPjoghxfaFwhaEG1ZCnoL47mZAgpbzT7fsBh4tBP85TZAME3a3vN2MMoCSvLPud4NBu5Svi5QZDZD'
#graph = facebook.GraphAPI(oauth_access_token)
#profile = graph.get_object("me")
#friends = graph.get_connections("me", "friends")
#graph.put_object("me", "feed", message="I am writing on my wall via FB api")



import web
from facepy import GraphAPI
from urlparse import parse_qs

url = ('/', 'index')



app_id = "390489417748163"
app_secret = "6f0d7497c832894c5dcf7b4187073065"
post_login_url = "http://birthdaywisher:8080/"

class index:
    def GET(self):
        user_data = web.input(code=None)
        code = user_data.code

        if not code:
			dialog_url = ( "http://www.facebook.com/dialog/oauth?" + "client_id=" + app_id + "&redirect_uri=" + post_login_url + "&scope=publish_stream" )
			return "<script>top.location.href='" + dialog_url + "'</script>"
		else:
            token_url = ( "https://graph.facebook.com/oauth/access_token?" +"client_id=" + app_id + "&redirect_uri=" + post_login_url + "&client_secret=" + app_secret + "&code=" + code )
            response = requests.get(token_url).content

            params = {}
            result = response.split("&", 1)
            for p in result:
                (k,v) = p.split("=")
                params[k] = v

            access_token = params['access_token']

            graph_url = ( "https://graph.facebook.com/me/photos?" +
                          "access_token=" + access_token )

            return ( '<html><body>' + '\n' +
                     '<form enctype="multipart/form-data" action="' +
                     graph_url + ' "method="POST">' + '\n' +
                     'Please choose a photo: ' + '\n' +
                     '<input name="source" type="file"><br/><br/>' + '\n' +
                     'Say something about this photo: ' + '\n' +
                     '<input name="message" type="text" value=""><br/><br/>' + '\n' +
                     '<input type="submit" value="Upload"/><br/>' + '\n' +
                     '</form>' + '\n' +
                     '</body></html>' )

if __name__ == "__main__":
    app = web.application(url, globals())
    app.run()
#user_data = web.input(code=None)
#
#if not user_data.code:
#    dialog_url = ( "http://www.facebook.com/dialog/oauth?" +
#                               "client_id=" + app_id +
#                               "&redirect_uri=" + post_login_url +
#                               "&scope=publish_stream" )
#
#    return "<script>top.location.href='" + dialog_url + "'</script>"
#else:
#    graph = GraphAPI()
#    response = graph.get(
#        path='oauth/access_token',
#        client_id=app_id,
#        client_secret=app_secret,
#        redirect_uri=post_login_url,
#        code=code
#    )
#    data = parse_qs(response)
#    graph = GraphAPI(data['access_token'][0])
#    graph.post(path = 'me/feed', message = 'Your message here')



