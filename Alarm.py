import time
from playsound import playsound
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((815,600))

background = pygame.image.load("alarmbackground.jpg")
background = pygame.transform.scale(background, (815,600))

base_font = pygame.font.Font(None,50)
user_text = ''
user_text2 = ''
input_rect_one =  pygame.Rect(565,360,190,50)
input_rect_two = pygame.Rect(530,420,190,50)


color_active = pygame.Color('lightskyblue3')
color_passive = pygame.Color('gray15')
color = color_passive


def main():
    global user_text
    global user_text2

    alarm_min = int(user_text2)
    alarm_hour = int(user_text)
    alarm_seconds = 0
    if alarm_min == 0:
        alarm_seconds = ((alarm_hour * 60) * 60) 

    if alarm_hour == 0:
        alarm_seconds = alarm_min * 60

    else:
        alarm_seconds = ((alarm_hour * 60) * 60) + alarm_min * 60

    seconds = 0

    while alarm_seconds != seconds:
        time.sleep(1)
        seconds += 1

 
    for x in range(0,45):
        playsound("alarmsound.wav")

active = False
active2 = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect_one.collidepoint(event.pos):

                active1 = True
                active2 =False
                
            
            if input_rect_two.collidepoint(event.pos):
                active2 = True
                active1 = False
            
        if event.type == pygame.KEYDOWN:
            if active1 == True:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                            
                else:
                    user_text += event.unicode

        if event.type == pygame.KEYDOWN:
            if active2 == True:
                if event.key == pygame.K_BACKSPACE:
                    user_text2 = user_text2[:-1]
                                
                else:
                    user_text2 += event.unicode 

    screen.blit(background,(0,0))


    pygame.draw.rect(screen,color,input_rect_one,2)
    text_surface = base_font.render(user_text, True, (225,225,225))
    screen.blit(text_surface,input_rect_one)

    pygame.draw.rect(screen,color,input_rect_two,2)
    text_surface2 = base_font.render(user_text2, True, (225,225,225))
    screen.blit(text_surface2,input_rect_two)

    text_surface3 = base_font.render("Hours:", True, (225,225,225))
    screen.blit(text_surface3,(450,360))

    text_surface4 = base_font.render("Min:", True, (225,225,225))
    screen.blit(text_surface4,(450,420))

    input_rect_one.w = max(200,text_surface.get_width() + 10)
    input_rect_two.w = max(200,text_surface2.get_width() + 10)


    pygame.display.update()  
    if user_text != "" and user_text2 != "":
        main()
        break

        





