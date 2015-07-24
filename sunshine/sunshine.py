import random

class Sunshine(object):

    def __init__():
        self.temperament = self._get_random_mood()

    def __repr__():
        return '<This is a ' + self.temperament + ' Sunshine.>'

    def _get_random_mood(self):
        return random.choice(['benevolent','cranky','evil'])

    def get_sunshine_action(self):
        actions = ['burns','incinerates','warms','tans','forsakes']
        return random.choice(actions)

if __name__=='__main__':
    sunshine = Sunshine()
    print sunshine
