import random


class Sunshine(object):

    def __init__(self):
        self.temperament = self._get_random_mood()

    def __repr__(self   ):
        return 'This is a ' + self.temperament + ' Sunshine.'

    def _get_random_mood(self):
        return random.choice(['benevolent', 'cranky', 'evil'])

    def get_sunshine_action(self):
        actions = ['burns', 'incinerates', 'warms', 'tans', 'forsakes']
        return random.choice(actions)

    def what_it_do_to_me(self):
        msg = 'The ' + self.temperament + ' Sunshine ' + self.get_sunshine_action() + ' you.'
        print msg
        return

if __name__ == '__main__':
    sunshine = Sunshine()
    print sunshine
    print sunshine.what_it_do_to_me()
