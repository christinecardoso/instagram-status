from InstagramAPI import InstagramAPI


class InstaLogin(object):
    def __init__(self, username, password):
        self.API = InstagramAPI(username, password)
        self.API.login()

    def get_followers(self):
        return self.API.getTotalSelfFollowers()

    def get_followings(self):
        return self.API.getTotalSelfFollowings()

    def get_self_profile(self):
        self.API.getProfileData()
        return self.API.LastJson

    def unfollow(self, username):
        self.API.searchUsername(username)
        self.API.unfollow(self.API.LastJson['user']['pk'])

    def logout(self):
        self.API.logout()
