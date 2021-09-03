from mycroft import MycroftSkill, intent_file_handler


class Midicontrol(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('midicontrol.intent')
    def handle_midicontrol(self, message):
        self.speak_dialog('midicontrol')


def create_skill():
    return Midicontrol()

