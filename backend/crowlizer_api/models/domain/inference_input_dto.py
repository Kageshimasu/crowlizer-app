import datetime


class InferenceInputDto:

    def __init__(self):
        self.target_amount: int = 0
        self.current_amount: int = 0
        self.method: str = ''
        self.category: str = ''
        self.start_date: datetime.datetime = datetime.datetime.now()
        self.end_date: datetime.datetime = datetime.datetime.now()
        self.images: int = 0
        self.videos = 0
        self.twitter_existence = False
