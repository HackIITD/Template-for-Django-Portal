from math import floor
from random import random
def randomProfile():
	Profile_picture=["https://help.github.com/assets/images/help/profile/identicon.png","https://github.com/identicons/jasonlong.png","https://raw.githubusercontent.com/sehrgut/node-retricon/master/examples/images/github.png","https://avatars2.githubusercontent.com/u/163800"]
	a = floor(random()*len(Profile_picture))
	profile = Profile_picture[int(a)]
	return profile
