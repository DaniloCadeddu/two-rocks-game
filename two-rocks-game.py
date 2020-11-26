import pygame
from pygame import mixer
import random
import time

#Set up pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Two rocks game")
icon = pygame.image.load("./images/cave-painting.png")
pygame.display.set_icon(icon)

#Background sound
mixer.music.load('./music/Shuffle_or_Boogie.mp3')
mixer.music.play(-1)

#Define functions and classes

#Create rock object 
class Rocks : 
    def __init__ (self, img, state, x, y) :
        self.img = pygame.image.load(img)
        self.state = state
        self.x = x
        self.y = y

    def change_state (self) :
        if self.state == True :
            self.state = False
            self.img = pygame.image.load('./images/cancel.png')
        else :
            pass
    
def show_rocks(arr) :
        for i in arr :
            screen.blit(i.img, (i.x, i.y))

#Creating a list of rock objects
def make_rocks(x, y) :
    rocks = []
    for i in range(10) :
        rocks.append(Rocks('./images/cave-painting.png', True, x, y))
        x += 50
    return rocks   

#Check if every element of a row is selected
def row_completed(row) :
    complete_count = 0
    for i in row :
        if i.state == False :
           complete_count += 1
        else : 
            pass
    if complete_count == 10 :
        return True
    else :
        return False

#Create font and render some text
def text(x, y, string, size) :
    font = pygame.font.Font('freesansbold.ttf', size)
    text = font.render(string, True, (0,0,0))
    screen.blit(text, (x, y))

#Change the state rocks when the related button is clicked
def handle_up_rocks() :
    for i in up_rocks :
            if i.state == True :
                i.change_state()
                break
            else :
                pass
# There is surely a better way to do it
def handle_down_rocks() :
     for i in down_rocks :
            if i.state == True :
                i.change_state()
                break
            else :
                pass    

def handle_both_rocks() :
    if row_completed(up_rocks) or row_completed(down_rocks) :
            pass
    else :
        for i in up_rocks :
            if i.state == True :
                i.change_state()
                break
            else :
                pass
        for i in down_rocks :
            if i.state == True :
                i.change_state()
                break
            else :
                pass

def user_turn(events) :
   
    if events[0] : #1 from up 0 from down
        handle_up_rocks()
    if events[1] : # 0 from up 1 from down
        handle_down_rocks()
    if events[2] : #1 from up 1 from down
        handle_both_rocks()

#The enemy play random 
########### Future implement: the enemy is an AI ###########
def enemy_turn() :
    global turns
    if turns % 2 != 0 and events[3] :
        random_choice = random.randint(1, 3)
        
        if row_completed(up_rocks) :
            random_choice = 2
        
        if row_completed(down_rocks) :
            random_choice = 1
        
        if random_choice == 1 :
            handle_up_rocks()
            
        if random_choice == 2 :
            handle_down_rocks()
            
        if random_choice == 3 :
            handle_both_rocks()
            
        turns += 1

#Define variables
up_rocks   = make_rocks(160, 170)
down_rocks = make_rocks(160, 280)
button_one   = pygame.Rect(200, 450, 100, 50)
button_two   = pygame.Rect(350, 450, 100, 50)
button_three = pygame.Rect(500, 450, 100, 50)
enemy_button = pygame.Rect(350, 530, 100, 50)
turns = 0
play_button_click = pygame.Rect(360, 300, 64, 64)
play_button = pygame.image.load('./images/play-button.png')
running = False

#Initial frame
while not running :
    screen.fill((150, 160, 150))
    text(150, 95, 'Two rocks game', 65)
    text(25, 180, "(There are two piles of ten rocks. In each turn, you may either take one rock from a single pile,", 17)
    text(28, 210,  ' or one rock from both piles. The player that takes the last rock wins the game.)', 17)
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN : 
            if play_button_click.collidepoint(event.pos) :
                running = True
                break
    screen.blit(play_button, (360, 300))
    pygame.display.update()


#Main function
while running :
    
    screen.fill((210, 214, 211))
    text(150, 30, 'Two rocks game', 65)
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            exit()
        #Controlling the mouse position and dectect an event
        if event.type == pygame.MOUSEBUTTONDOWN :
            events = [button_one.collidepoint(event.pos), button_two.collidepoint(event.pos), button_three.collidepoint(event.pos), enemy_button.collidepoint(event.pos)]
            if turns % 2 == 0 :
                user_turn(events)
                turns += 1
            
    enemy_turn()  
    
    #Show turns
    if turns % 2 == 0 :
        text(350, 360, 'Your turn', 20)
    else :
        text(335, 360, 'Enemy\'s turn', 20)

    #Win and lose text
    if row_completed(up_rocks) and row_completed(down_rocks) and turns % 2 != 0 :
        screen.fill((210, 214, 211))
        text(266, 360, 'You Win!', 65)
        
    if row_completed(up_rocks) and row_completed(down_rocks) and turns % 2 == 0 :
        screen.fill((210, 214, 211))
        text(250, 360, 'You Lose...', 65)
       
    #Draw buttons
    if row_completed(up_rocks) :
        pygame.draw.rect(screen, [210, 214, 211], button_one) 
        pygame.draw.rect(screen, [210, 214, 211], button_three)

    else :
        pygame.draw.rect(screen, [70, 70, 255], button_one)
        text(245, 452, '1', 19)
        text(245, 474, '0', 19)
        
        pygame.draw.rect(screen, [70, 70, 255], button_three)
        text(545, 452, '1', 19)
        text(545, 474, '1', 19)
    
    if row_completed(down_rocks) :
        pygame.draw.rect(screen, [210, 214, 211], button_two)    
        pygame.draw.rect(screen, [210, 214, 211], button_three)
    
    else :
        pygame.draw.rect(screen, [70, 70, 255], button_two)
        text(395, 452, '0', 19)
        text(395, 474, '1', 19)
    
    #Enemy button
    if row_completed(up_rocks) and row_completed(down_rocks) :
        pygame.draw.rect(screen, [210, 214, 211], enemy_button)
    else :
        pygame.draw.rect(screen, [143, 10, 32], enemy_button)
        text(353, 530, 'Let enemy', 18)
        text(380, 552, 'play', 18)

    show_rocks(up_rocks)
    show_rocks(down_rocks)
    
    pygame.display.update()
