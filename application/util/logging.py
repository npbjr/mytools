class Color:
    MESSAGE str: ""
    HEADER = '\033[95m'+MESSAGE
    OKBLUE = '\033[94m'+MESSAGE
    OKCYAN = '\033[96m'+MESSAGE
    OKGREEN = '\033[92m'+MESSAGE
    WARNING = '\033[93m'+MESSAGE
    FAIL = '\033[91m'+MESSAGE
    ENDC = '\033[0m'+MESSAGE
    BOLD = '\033[1m'+MESSAGE
    UNDERLINE = '\033[4m'+MESSAGE

    def __init__(self, message):
        self.MESSAGE = message
        