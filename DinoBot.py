from PIL import ImageGrab
import time 
import pyautogui

#Variáveis da box de identificacao de obstaculo
X = 280.0
Y1 = 384
Y2 = 450

#Método para retornar a tela
def capture_screen():
    screen = ImageGrab.grab()
    return screen

#Método para detectar obstaculos
def detect_enemy(screen):
    aux_color = screen.getpixel((int(X),Y1))
    for x in range(int(X),int(X+15)):
        for y in range(Y1, Y2):
            color = screen.getpixel((x,y))
            if color != aux_color:
                return True
            else:
                aux_color = color

#Método para pular 
def jump():
    global X
    pyautogui.keyUp("down")
    pyautogui.keyDown("up")
    time.sleep(0.2)
    pyautogui.keyUp("up")
    pyautogui.keyDown("down")
    #Aumentar a variavel X a cada pulo para o dino se adaptar ao aumento de velocidade do jogo
    X+=3.2

print("Começa em 3 segundos...")
time.sleep(3)

pyautogui.keyDown("down")
#Loop para o dino não parar de desviar
while True:
    screen = capture_screen()
    if detect_enemy(screen):
        jump()