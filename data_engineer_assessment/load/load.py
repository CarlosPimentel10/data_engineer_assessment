from config.config import BASE_URL

class Load():

    def __init__(self) -> None:
        self.url = BASE_URL
    
    def load_data(self):

        with open('filename', 'r') as f:
            data = f.read()
