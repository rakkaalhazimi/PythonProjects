import pygame

musicfile = r"C:\Users\Lenovo\Downloads\Music\Claris - Connect.mp3"

class player:
    def play(self, musicfile):
        pygame.mixer.init()
        pygame.mixer.music.load(musicfile)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

if __name__ == '__main__':
    player.play(musicfile)