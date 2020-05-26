class SoundClass:
    count = 0

    def __init__(self, chat):
        self.sound = chat
        SoundClass.count += 1

    def getSound(self):
        return self.sound

sound = SoundClass('Music 01')
print('COUNT:', sound.count)
print('SOUND:', sound.getSound())