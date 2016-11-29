class ReadFile:
    @staticmethod
    def read_message():
        with open("invite.hdr") as f:
            content = f.readlines()
        message = ""
        for i in range(content.__sizeof__()):
            message += content[i]
            message += "\n"
        message += "\n"
        return message
