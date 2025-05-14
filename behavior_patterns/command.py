class Command:
    def execute(self):
        pass

class LightOnCommand(Command):
    def execute(self):
        print("Свет включен")

class RemoteControl:
    def __init__(self):
        self._command = None

    def set_command(self, command):
        self._command = command

    def press_button(self):
        self._command.execute()

remote = RemoteControl()
remote.set_command(LightOnCommand())
remote.press_button()