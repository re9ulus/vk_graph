import json
import urllib2

# TODO: Build user friends graph

def get_friends(user_id):
	response = None
	try:
		response = urllib2.urlopen('https://api.vk.com/method/friends.get?user_id={0}'.format(user_id)).read()
	except urllib2.HTTPError, err:
		print("HTTPError")
	except urllib2.URLError, err:
		print("URLError")
	return response

if __name__ == '__main__':
	user_id = 123456
	friends = get_friends(user_id)
	print(friends)