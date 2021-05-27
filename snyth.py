Python 3.7.5 (tags/v3.7.5:5c02a39a0b, Oct 15 2019, 00:11:34) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from synthesizer import Player, Synthesizer, Waveform
import pygame
pygame.init()

screen_width = 500
screen_height = 500

screen = pygame.display.set_mode([screen_width, screen_height])

font = pygame.font.SysFont("comicsanssms", 20)
text = font.render("Press Q,W,E,R,T,Y,U,I,O,P,A,S,D,F,G,H,J,K,or 5. 0 TO QUIT", True, (255,255,255))


player = Player()
player.open_stream()
synthesizer = Synthesizer(osc1_waveform=Waveform.sine,osc1_volume=1.0, use_osc2=False)

chord = [261.628, 329.628, 391.996]

def G2():
    player.play_wave(synthesizer.generate_constant_wave(97.999,.2))
    
def C3():
    player.play_wave(synthesizer.generate_constant_wave(130.81,.2))

def D3():
    player.play_wave(synthesizer.generate_constant_wave(146.83,.2))

def F3():
    player.play_wave(synthesizer.generate_constant_wave(174.61,.2))
    
def G3():
    player.play_wave(synthesizer.generate_constant_wave(196.00,.2))

def Gb3():
    player.play_wave(synthesizer.generate_constant_wave(207.65,.2))

def A4():
    player.play_wave(synthesizer.generate_constant_wave(440.00,.2))
    
def B4():
    player.play_wave(synthesizer.generate_constant_wave(493.88,.2))

def Bb4():
    player.play_wave(synthesizer.generate_constant_wave(554.37,.2))

def F4():
    player.play_wave(synthesizer.generate_constant_wave(349.23,.2))

def FS4(): # F#4
    player.play_wave(synthesizer.generate_constant_wave(311.13,.2))

def G4(): 
    player.play_wave(synthesizer.generate_constant_wave(392.00,.2))

def C5():
    player.play_wave(synthesizer.generate_constant_wave(523.25,.2))

def D5():
    player.play_wave(synthesizer.generate_constant_wave(587.33,.2))

def E5():
    player.play_wave(synthesizer.generate_constant_wave(659.26,.2))
    
def G5():
    player.play_wave(synthesizer.generate_constant_wave(783.99,.2))

def A5():
    player.play_wave(synthesizer.generate_constant_wave(880.00,.2))

def B5():
    player.play_wave(synthesizer.generate_constant_wave(987.77,.2))

def playChord():
    player.play_wave(synthesizer.generate_chord(chord, 3.0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                G2()
            if event.key == pygame.K_w:
                C3()
            if event.key == pygame.K_e:
                D3()
            if event.key == pygame.K_r:
                F3()
            if event.key == pygame.K_t:
                G3()
            if event.key == pygame.K_y:
                Gb3()
            if event.key == pygame.K_u:
                A4()   
            if event.key == pygame.K_i:
                B4()
            if event.key == pygame.K_o:
                Bb4()
            if event.key == pygame.K_p:
                F4()
            if event.key == pygame.K_a:
                FS4()
            if event.key == pygame.K_s:
                G4()
            if event.key == pygame.K_d:
                C5()
            if event.key == pygame.K_f:
                D5()
            if event.key == pygame.K_g:
                E5()
            if event.key == pygame.K_h:
                G5()
            if event.key == pygame.K_j:
                A5()
            if event.key == pygame.K_k:
                B5()
            if event.key == pygame.K_5:
                playChord()
            if event.key == pygame.K_0:
                pygame.quit()
    screen.fill((0, 0 , 0))
    screen.blit(text,(250 - text.get_width() // 2, 250 - text.get_height() // 2))
    pygame.display.flip()
