class ReadFile:
    @staticmethod
    def read_message(path):
        with open(path) as f:
            content = f.readlines()
        message = ""
        for i in range(len(content)):
            message += content[i]
        message += "\n"
        return message
