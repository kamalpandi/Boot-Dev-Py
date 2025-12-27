class Notification:
    def __init__(self, recipient):
        self.recipient = recipient

    def get_message(self):
        return "Notification for " + self.recipient


class EmailNotification(Notification):
    def __init__(self, recipient, subject):
        self.recipient = recipient
        self.subject = subject

    def get_message(self):
        return f"Email to {self.recipient}: " + self.subject


class SMSNotification(Notification):
    def __init__(self, recipient):
        self.recipient = recipient
        

    def get_message(self):
        return f"SMS to {self.recipient}: short alert"


def format_notifications(notifications):
    result = []
    for notification in notifications:
        result.append(notification.get_message())
    return result
