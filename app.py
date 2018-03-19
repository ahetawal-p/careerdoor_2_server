from toapi import Api
from items.companies import Companies
from items.questions import Questions
from items.questionDetail import QuestionDetail
from items.topics import Topics
from items.dailycron import DailyCron
from settings import MySettings

api = Api(None, settings=MySettings)
api.register(Companies)
api.register(Questions)
api.register(QuestionDetail)
api.register(Topics)
api.register(DailyCron)

if __name__ == '__main__':
    api.serve()
