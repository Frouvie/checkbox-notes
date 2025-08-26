from data import DataModel
from ui import ApplicationUI

class Application(ApplicationUI):
    def __init__(self):
        super().__init__()

        self.data = DataModel()