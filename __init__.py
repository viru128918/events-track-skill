from mycroft import MycroftSkill, intent_file_handler


class EventsTrack(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('track.events.intent')
    def handle_track_events(self, message):
        self.speak_dialog('track.events')


def create_skill():
    return EventsTrack()

