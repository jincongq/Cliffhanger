"""
The Cliffhanger Summative Project
ICS3U1-01
Mr.Cope
May 23, 2015
Pamela Zeng and Jessica Ip

In this game, the player is hanging from a cliff. The objective of the game is to
hang on as long as possible while trying to avoid getting hit by a hammer. 

"""

#function definitions 

def game_intro():  #menu of game 
        
    passed_variable=True  #determine whether or not to exit game 
    intro = True    #determine whether user is still on menu page 
    clock = pygame.time.Clock()   
    while intro:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == QUIT:   #if user chooses quit
                passed_variable=False   #exit game
                
                intro=False        #exit menu 

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()   #get mouse positions
                x=mouse_position[0]
                y=mouse_position[1]
                if x>= 750 and x <=970 and y >= 325 and y <=425:  #if user click play 
                    intro = False      #move onto next function 
                    
                elif x>= 750 and x <=970 and y >= 465 and y <=565:  #if user clicks instructions
                    passed_variable=instructions()  #determine whether or not to exit game in instructions function 
                    if passed_variable==False:   #if exit game:
                        intro=False              #exit menu 
    
        

        #load and draw menu backgound
        img = pygame.image.load("gamemenu.png").convert()    
        screen.blit(img, (0,0))   

        #draw buttons
        pygame.draw.rect(screen, GREEN, (750, 325, 220, 100))  
        pygame.draw.rect(screen, RED, (750, 465, 220, 100))

        #set fonts
        font1 = pygame.font.SysFont("comicsansms", 36)    
        font2 = pygame.font.SysFont("comicsansms", 24)
        
        text1 = font1.render("PLAY", True, BLACK)
        text2 = font2.render("INSTRUCTIONS", True, BLACK)

        #draw words
        screen.blit(text1, (815, 350))  
        screen.blit(text2, (765, 495))

        pygame.display.flip()  #update screen
    
    return passed_variable   #determine whether or not user wants to exit game 


def instructions():
    
    #load images for instructions
    instructions_1=pygame.image.load("Instructions Page 1.png").convert()    
    instructions_2=pygame.image.load("Instructions Page 2.png").convert()
    instructions_3=pygame.image.load("Instructions Page 3.png").convert()
    instructions_4=pygame.image.load("Instructions Page 4.png").convert()

    instructions=[instructions_1, instructions_2, instructions_3, instructions_4]  #list of pages

    count=0
    passed_variable=2
    image=instructions[count]
    screen.blit(image, (0,0))
    pygame.display.flip()
    clock = pygame.time.Clock()
    while passed_variable==2:
        clock.tick(30)
        for ev in pygame.event.get():
            if ev.type == QUIT:
                passed_variable=False
                
                
            elif ev.type == MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()  #get position of mouse
                x=mouse_position[0]
                y=mouse_position[1]
                if (x>25) and (x<200) and (y>25) and (y<100):  #back to menu 
                    passed_variable=True
                    
                elif (x>428) and (x<489) and (y>530) and (y<573):#left arrow coordinates:
                    if count>0:   #not on first page 
                        count-=1  #back to previous page 

                elif (x>514) and (x<573) and (y>525) and (y<573):#right arrow coordinates:
                    if count<3:  #not on last page
                        count+=1  #into next page 
                        
        image=instructions[count]
        screen.blit(image, (0,0))   #draw image
        pygame.display.flip()     #update screen

    return passed_variable   


def start_condition():
    
    done = False
    clock = pygame.time.Clock()
    passed_variable=True

    while not done:
        pygame.event.pump() #used to catch events
        clock.tick(30)
        keys = pygame.key.get_pressed()  #list of conditions of all keyboard events 

        if keys[K_a] and keys[K_s] and keys[K_d] and keys[K_j] and keys[K_k] and keys[K_l]:  #if the user is pressing down a,s,d,j,k,l together
            done = True   #start countdown 
        
        for event in pygame.event.get():
            if event.type == QUIT:
                done = True
                passed_variable=False

        #load and draw background   
        background = pygame.image.load("gamebackground1.png").convert()  #load and draw background
        screen.blit(background,(0,0))

        #set font and draw text 
        font = pygame.font.SysFont("comicsansms", 36)
        text = font.render("Please Press Down on All Keys (A,S,D,J,K,L) to Begin", True, BLACK)
        screen.blit(text, (60,20))

        pygame.display.flip()  #update screen

    return passed_variable


def intro_counter():  #countdown before game starts 

    done = False
    counter = 0   #count frames
    clock = pygame.time.Clock() 
    background = pygame.image.load("gamebackground1.png").convert()  
    passed_variable=True
    
    while not done:
        
        clock.tick(30)
        font = pygame.font.SysFont("comicsansms", 72)
        
        if counter <=30:   #in the first second (as there are 30 frames per second)
            text = font.render("3", True, BLACK)  #draw "3"
        elif counter <=60:
            text = font.render("2", True, BLACK)
        elif counter <=90:
            text = font.render("1", True, BLACK)
        elif counter <=95:
            text = font.render("GOGOGO", True, BLACK)
        elif counter > 95:  #after 3 seconds
            done = True    #countdown is done

        counter +=1
        screen.blit(background,(0,0)) 
        
        screen.blit(text,(500-text.get_width()//2,40))  #draw text in the middle of screen 
        pygame.display.flip()
        
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                done = True
                passed_variable=False
            elif ev.type == KEYDOWN:
                if ev.key == K_SPACE:  #press spacebar to end game 
                    done = True
    return passed_variable


def fingers(bent_R2,bent_R3, bent_R4, bent_L4, bent_L3, bent_L2, straight_L4, straight_L3,straight_L2, straight_R2,straight_R3, straight_R4, hit_L4, hit_L3, hit_L2, hit_R2, hit_R3, hit_R4, dead_index,left_hand, right_hand,no_hand, background,person):
                
    #finger functionality 
    #left hand has a,s,d
    #right hand has j,k,l
    #fingers are assigned a value of 0-5 from left to right
    pygame.event.pump()
    keys = pygame.key.get_pressed()
         
    screen.blit(background, (0,0))

    #dead index is a list of dead fingers
     
    if 0 in dead_index and 1 in dead_index and 2 in dead_index:  #if all three fingers on the left hand are dead
        Left=False   #the left hand falls

    #if two fingers are dead and one finger is lifted up
    elif 0 in dead_index and 1 in dead_index and keys[K_d] == 0: 
        Left = False
    elif 0 in dead_index and 2 in dead_index and keys[K_s] == 0:
        Left = False
    elif 1 in dead_index and 2 in dead_index and keys[K_a] == 0:
        Left = False

    #if one finger is dead and two fingers are lifted up
    elif 0 in dead_index and keys[K_s]==0 and keys[K_d] == 0:
        Left = False
    elif 1 in dead_index and keys[K_a]==0 and keys[K_d] == 0:
        Left = False
    elif 2 in dead_index and keys[K_a]==0 and keys[K_s] == 0:
        Left = False

    #if all three fingers are lifted up
    elif keys[K_a]==0 and keys[K_s]==0 and keys[K_d] == 0:
        Left= False
    else:
        Left=True  #otherwise the left hand is still holding on 
        
    #checking the same in the right hand       
    if 3 in dead_index and 4 in dead_index and 5 in dead_index:
        Right=False
    elif 3 in dead_index and 4 in dead_index and keys[K_l] == 0:
            Right = False
    elif 3 in dead_index and 5 in dead_index and keys[K_k] == 0:
        Right = False
    elif 4 in dead_index and 5 in dead_index and keys[K_j] == 0:
        Right = False
    elif 3 in dead_index and keys[K_k]==0 and keys[K_l] == 0:
        Right = False
    elif 4 in dead_index and keys[K_j]==0 and keys[K_l] == 0:
        Right = False
    elif 5 in dead_index and keys[K_j]==0 and keys[K_k] == 0:
        Right = False
    elif keys[K_j]==0 and keys[K_k]==0 and keys[K_l] == 0:
        Right= False

    else:
        Right=True
        
               
    if Left==True:  #if the left hand is still holding on
        
        
            
        if keys[K_a] == 1:  #if "a" is pressed down 
            if 0 in dead_index:  #check if the finger is dead
                screen.blit(hit_L4,(0,0))  #draw a dead finger if it is 
            else:
                screen.blit(bent_L4, (0,0)) #draw a bent and alive finger

        if keys[K_s] == 1:
            if 1 in dead_index:
                screen.blit(hit_L3, (0,0))
            else:
                screen.blit(bent_L3, (0,0))

        if keys[K_d] == 1:
            if 2 in dead_index:
                screen.blit(hit_L2, (0,0))
            else:
                screen.blit(bent_L2, (0,0))
        if keys[K_a] == 0:
            if 0 in dead_index:
                screen.blit(hit_L4, (0,0))
            else:
                screen.blit(straight_L4,(0,0))        
        if keys[K_s] == 0:
            if 1 in dead_index:
                screen.blit(hit_L3, (0,0))
            else:
                screen.blit(straight_L3, (0,0))
        if keys[K_d] == 0:
            if 2 in dead_index:
                screen.blit(hit_L2, (0,0))
            else:
                screen.blit(straight_L2, (0,0))

    if Right== True:  #if the right hand is still holding on
        
            
        if keys[K_j] == 1:  #if "j" is pressed down 
            if 3 in dead_index:  #check if the finger is dead
                screen.blit(hit_R2, (0,0))  #if it is draw a dead finger
            else:
                screen.blit(bent_R2, (0,0))   #if not draw a bent and alive finger

        if keys[K_k] == 1:
            if 4 in dead_index:
                screen.blit(hit_R3, (0,0))
            else:
                screen.blit(bent_R3, (0,0))

        if keys[K_l] == 1:
            if 5 in dead_index:
                screen.blit(hit_R4, (0,0))
            else:
                screen.blit(bent_R4, (0,0))
                
        if keys[K_j] == 0:
            if 3 in dead_index:
                    screen.blit(hit_R2, (0,0))
            else:
                screen.blit(straight_R2,(0,0))

        if keys[K_k] == 0:
            if 4 in dead_index:
                screen.blit(hit_R3, (0,0))
            else:
                screen.blit(straight_R3, (0,0))

        if keys[K_l] == 0:
            if 5 in dead_index:
                screen.blit(hit_R4, (0,0))
            else:
                screen.blit(straight_R4,(0,0))

    if Left== True and Right == True:  #if both hands are still holding on
        screen.blit(person, (0,0))  #draw person with two hands
    elif Left == False and Right == False:  #if both hands are not holding on
        screen.blit(no_hand,(0,0))   #draw person with no hands
    elif Left== False:  #if the left hand is not holding on
        screen.blit(right_hand, (0,0))  #draw person with only right hand
    elif Right == False:  #if the right hand is not holding on
        screen.blit(left_hand, (0,0))  #draw person with left hand
    

    pygame.display.flip()
    return [Left, Right]  #return true or false for the condition of the left and right hands


def game():

    #loading images
    background = pygame.image.load("game_background.png").convert()

    person = pygame.image.load("person.png").convert_alpha()
    hammer_up = pygame.image.load("hammer_up.png").convert_alpha()
    hammer_down = pygame.image.load("hammer_down.png").convert_alpha()



    #fingers_bent
    bent_R2 = pygame.image.load("fingers_bentR2.png").convert_alpha()
    bent_R3 = pygame.image.load("fingers_bentR3.png").convert_alpha()
    bent_R4 = pygame.image.load("fingers_bentR4.png").convert_alpha()

    bent_L2 = pygame.image.load("fingers_bentL2.png").convert_alpha()
    bent_L3 = pygame.image.load("fingers_bentL3.png").convert_alpha()
    bent_L4 = pygame.image.load("fingers_bentL4.png").convert_alpha()

    #fingers_straight
    straight_R2 = pygame.image.load("fingers_straightR2.png").convert_alpha()
    straight_R3 = pygame.image.load("fingers_straightR3.png").convert_alpha()
    straight_R4 = pygame.image.load("fingers_straightR4.png").convert_alpha()

    straight_L2 = pygame.image.load("fingers_straightL2.png").convert_alpha()
    straight_L3 = pygame.image.load("fingers_straightL3.png").convert_alpha()
    straight_L4 = pygame.image.load("fingers_straightL4.png").convert_alpha()

    #fingers_hit
    hit_L4 = pygame.image.load("fingers_hitL4.png").convert_alpha()
    hit_L3 = pygame.image.load("fingers_hitL3.png").convert_alpha()
    hit_L2 = pygame.image.load("fingers_hitL2.png").convert_alpha()
    hit_R2 = pygame.image.load("fingers_hitR2.png").convert_alpha()
    hit_R3 = pygame.image.load("fingers_hitR3.png").convert_alpha()
    hit_R4 = pygame.image.load("fingers_hitR4.png").convert_alpha()
    hit_img=[hit_L4, hit_L3, hit_L2, hit_R2, hit_R3, hit_R4]

    warning= pygame.image.load("Game Warning Sign.png").convert_alpha()
    
    left_hand= pygame.image.load("left hand.png").convert_alpha()
    right_hand= pygame.image.load("right hand.png").convert_alpha()
    no_hand = pygame.image.load("no hands.png").convert_alpha()

    #loading sounds
    warning_sound = pygame.mixer.Sound("beep_sound.wav")
    hammer_sound = pygame.mixer.Sound("hammer_sound.wav")

    font = pygame.font.SysFont("comicsansms", 24)
    
    finished=False
    
    dead_index=[]  #list of indexes of dead fingers
    finger_list = [K_a, K_s, K_d, K_j, K_k, K_l]  
    index=[0,1,2,3,4,5]  #finger index list
    hit_counter = 2 #number of hammer hits per turn
    round_counter=0 #count the number of rounds with the same number of hits 
    score=0  #will count score
    passed_variable=True

    while not finished:
                        
        fingers_hit = []  #list of fingers about to be hit 
        
        for count in range (0, hit_counter): #for each hit 
            use=False  
            while use==False:
                    random_=random.choice(index)  #choose a random finger index
                    if random_ not in dead_index:  #if the finger index is not does not point to a dead finger
                            use=True   #use that index
                
            fingers_hit.append (random_)  #add it to the fingers_hit list

        #WARNING   
        warning_position= [(195,30), (270,30),(345, 30),(595,30),(680,30),(760,30)]  #list of positions to draw warning signs corrosponding to finger indexes

        done = False
        clock = pygame.time.Clock()
        counter_index=0 #the the index of fingers in fingers_hit 
        count_time=0 #variable to keep track of frames
        
        while not done:
            clock.tick(30)

            score+=1  #add score for every frame
            Left_Right=fingers(bent_R2,bent_R3, bent_R4, bent_L4, bent_L3, bent_L2, straight_L4, straight_L3,straight_L2, straight_R2,straight_R3, straight_R4, hit_L4, hit_L3, hit_L2, hit_R2, hit_R3, hit_R4, dead_index,left_hand, right_hand,no_hand, background,person)
            hit_text = font.render("Number of Hits: " + str(hit_counter), True, WHITE)
            screen.blit(hit_text, (30, 20))

            score_text = font.render("Score: "+str(score), True, WHITE)
            screen.blit(score_text, (850, 20))
            #fingers return a list of conditions of the left and right hands
            if Left_Right[0]==False:  #if the left hand is not holding on 
                    dead_index.append(0)  #add all its fingers to dead_index
                    dead_index.append(1)
                    dead_index.append(2)
            if Left_Right[1]== False: #if the right hand is not holding on
                    dead_index.append (3)  #add all its fingers to dead_index
                    dead_index.append (4)
                    dead_index.append (5)
            if fingers_hit[counter_index]in dead_index:  #if the finger that is about to be hit is inoperational 
                done=True   #stop hitting 
            if count_time<15:
                warning_sound.play()  #play warning sound
                screen.blit(warning, warning_position[fingers_hit[counter_index]])  #draw warning sign
                
                count_time+=1
            elif count_time>=15 and count_time<26:
                count_time+=1
                
            elif count_time>=26:  
                count_time=0  #reset the frames to zero 
                counter_index+=1  #move on to the next item in fingers_hit 

            pygame.display.flip()

            if counter_index== len(fingers_hit):  #if warning signs have been drawn above all the fingers in fingers_hit  
                done=True  #stop drawing 
            if 0 in dead_index and 1 in dead_index and 2 in dead_index and 3 in dead_index and 4 in dead_index and 5 in dead_index:  #if all fingers are inoperational
                done= True
                finished=True   #exit game()

            for ev in pygame.event.get():
                    if ev.type==QUIT:
                        done=True
                        finished=True   
                        passed_variable=False
                    elif ev.type==KEYDOWN:
                        if ev.key == K_SPACE:
                            done=True
                            finished=True
                            passed_variable=False


        #HAMMER
        hammer_position = [(160,0), (240,0),(330, -10),(595,0),(680,0),(760,0)] #list of positions to draw hammer

        done = False
        clock = pygame.time.Clock()
        counter_index=0  #counts the index of fingers in fingers_hit 
        count_time=0   #counts the number of frames
        if not finished:
            while not done:
                pygame.event.pump()
                keys = pygame.key.get_pressed()
                clock.tick(30)

                score+=1
                #fingers return a list of true or false values for the left and right hands
                Left_Right=fingers(bent_R2,bent_R3, bent_R4, bent_L4, bent_L3, bent_L2, straight_L4, straight_L3,straight_L2, straight_R2,straight_R3, straight_R4, hit_L4, hit_L3, hit_L2, hit_R2, hit_R3, hit_R4, dead_index,left_hand, right_hand,no_hand, background,person)

                #draw the number of hits and score onscreen
                hit_text = font.render("Number of Hits: " + str(hit_counter), True, WHITE)
                screen.blit(hit_text, (30, 20))
                score_text = font.render("Score: "+str(score), True, WHITE)
                screen.blit(score_text, (850, 20))
                

                #check conditions of hands. if the hands are not holding on, add the fingers on the hand to dead_index
                if Left_Right[0]==False:  
                        dead_index.append(0)
                        dead_index.append(1)
                        dead_index.append(2)

                if Left_Right[1]== False:
                        dead_index.append (3)
                        dead_index.append (4)
                        dead_index.append (5)


                

                if fingers_hit[counter_index] in dead_index: #if the finger that is about to be hit is already dead 
                    done=True   #stop hitting 
                if count_time<=5:   #for the first 5 frames
                    screen.blit(hammer_up, hammer_position[fingers_hit[counter_index]])  #draw the hammer in the up position
                    count_time+=1  #increase the number of frames
                    
                elif count_time> 5 and count_time<12: #for these frames
                    hammer_sound.play()  #play hammering sound
                    count_time+=1
                    screen.blit(hammer_down, hammer_position[fingers_hit[counter_index]])  #draw hammer in down position 

                    
                elif count_time>=12 and count_time<17:
                    count_time+=1
                    if keys[finger_list[fingers_hit[counter_index]]] == 1:  #if the finger was pressed down when the hammer was down 
                        dead_index.append(index[fingers_hit[counter_index]]) #add the finger to dead_index

                        done= True  #go back to the top
                        
                        

                elif count_time>=17:
                    count_time=0
                    counter_index+=1   #move onto next finger in fingers_hit 

                pygame.display.flip()
                if counter_index== len(fingers_hit):  #if all fingers in fingers_hit have been gone through 
                    done=True  


                for ev in pygame.event.get():
                    if ev.type==QUIT:
                        done=True
                        finished=True
                        passed_variable=False
                        
                    elif ev.type==KEYDOWN:
                        if ev.key == K_SPACE:
                            done=True
                            finished=True
                            passed_variable=False
                            
                        
        if 0 in dead_index and 1 in dead_index and 2 in dead_index and 3 in dead_index and 4 in dead_index and 5 in dead_index: #if all fingers are dead
            
            finished=True

        round_counter+=1  #increase the number of rounds by one
        if round_counter==2:  #if there were already two rounds
            hit_counter+=1   #increase the number of hits by one 
            round_counter=0   #set the number of rounds with the new number of hits to zero 

    return [passed_variable,score]

def game_over_sequence():

    passed_variable = True
    #load images
    fall1 = pygame.image.load("falling1.png").convert_alpha()
    fall2 = pygame.image.load("falling2.png").convert_alpha()
    fall3 = pygame.image.load("falling3.png").convert_alpha()
    fall4 = pygame.image.load("falling4.png").convert_alpha()

    #load sounds
    splash = pygame.image.load("water_splash_end.png").convert()
    splash_sound = pygame.mixer.Sound("splash_sound.wav")
    scream_sound = pygame.mixer.Sound("scream_sound.wav")
    scream_sound.play() #play screaming sound
    done = False
    counter = 0
    clock = pygame.time.Clock() 
    background = pygame.image.load("game_background.png").convert()
    
    while not done:
        clock.tick(30)
        screen.blit(background, (0,0))       

        #draw a different image of person falling according to where the counter is 
        if counter <=10:
            screen.blit(fall1, (0,0))
        elif counter <20:
            screen.blit(fall2, (0,0))
        elif counter <=30:
            screen.blit(fall3, (0,0))
        elif counter <=40:
            screen.blit(fall4, (0,0))
        elif counter <=80:
            splash_sound.play() #play splash sound
            screen.blit(splash, (0,0))   #draw water splashing 
        elif counter > 80:
            done = True 
        counter +=1
        
        pygame.display.flip()
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                passed_variable = False
                done = True
    return passed_variable             
def game_end(score, score_list):

    background = pygame.image.load("game_background.png").convert()
    clock = pygame.time.Clock() 
    done = False
    passed_variable = True
    
    
    
    while not done:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == QUIT:
                passed_variable = False
                done = True
                
                
                
            elif event.type == MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()  #get mouse positions
                x=mouse_position[0]
                y=mouse_position[1]
                if x >= 200 and x <= 420 and y >= 450 and y <= 550:  #if user click in this region
                    
                    passed_variable = False  #exit game
                    done = True
                    
                elif x >= 600 and x <= 820 and y >= 450 and y <= 550:  #if user click in this region
                    done = True  #will loop back to begining (play again)
                    
                elif x >= 400 and x <= 620 and y >= 300 and y <= 400:  #if user click in this region
                    passed_variable=Score_display(score_list)  #use the function Scre_display to display high score onscreen 
                    if passed_variable==False:
                        done=True
                    
                    
        screen.blit(background,(0,0))

        #set fonts and text
        font = pygame.font.SysFont("comicsansms", 72)
        smallfont = pygame.font.SysFont("comicsansms", 32)
        medfont = pygame.font.SysFont("comicsansms", 42)
        
        text = font.render("Game Over", True, BLUE)
        text1 = smallfont.render("QUIT", True, BLACK)
        text2 = smallfont.render("PLAY AGAIN", True, BLACK)
        text3 = smallfont.render("SCOREBOARD", True, BLACK)
        text4 = medfont.render("Your score: "+str(score), True, BLUE) 
                
        #draw buttons
        pygame.draw.rect(screen, RED, (200, 450, 220, 100))
        pygame.draw.rect(screen, GREEN, (600, 450, 220, 100))
        pygame.draw.rect(screen, YELLOW, (400, 300, 220, 100))

        #draw text
        screen.blit(text,(500-text.get_width()//2,20))  #will display in the middle of the screen
        screen.blit(text1, (260, 475))
        screen.blit(text2, (610, 475))
        screen.blit(text3, (405, 325))
        screen.blit(text4, (500-text.get_width()//2, 110))

        pygame.display.flip()
        
    return passed_variable


def Scoreboard(score):

    file=open("GAME SCORES.txt", "a+")  
    file_text=file.read()
    file.close()
    if len(file_text)>0:  #if there are values in the file 
        word=""  #set value for word
        scores_list=[]

        for character in file_text:
            if character==" " or character==(chr(10)):  #if there is a space or newline 
                if "." in word:   
                    word=""
                elif "." not in word:  #if there isn't a period
                    scores_list.append(word)  #add word to score _list
                    word=""
                
            else:
                word+=character  #add the character to the word
        if word!="": #if word is not empty
            scores_list.append(word)  #add to scores_list

        

        for count in range (0, len(scores_list)):   #for every item in list
            scores_list[count]=int (scores_list[count])  #convert to integer values

        for count in range (0, len(scores_list)): 

            if scores_list[count]<score:     #if the score is more than a score in the score_list
                scores_list.insert(count,score)  #insert the score in the place of the smaller score
                break

        
        if len(scores_list)<10:  #if there are less than 10 scores
                if score not in scores_list:  #if the score is not in the list 
                    scores_list.append(score)  #add them all to the score_list

                
        if len(scores_list)>10:     #if there are more than 10
            del scores_list[10]   #delete the 11th score
        
        
        Highscores=[]  #empty list for high scores
        
        file=open("GAME SCORES.txt", "w")

        for count in range (0, len(scores_list)):
            string=str(count+1)+". "+str(scores_list[count])+chr(10) #string of place, score and newline character 
            file.write(string)  #write the string into file 
            string=string[0:int(len(string))-1] #cut out the newline character at the end
            Highscores.append(string)   #add to high scores list
        file.close()

    elif len(file_text)==0:  #if there is no score in the file 
        file=open("GAME SCORES.txt", "w")
        string="1. "+str(score)   #set the score as the 1st one
        file.write(string)  #write it to the file 
        file.close()  
        scores_list=[score]  #add score to score_list

    pygame.display.flip()
    
    return scores_list  #return top 10 scores


def Score_display(scores_list):

    passed_variable=2  #used to determine whether user wanta to quit or not 
    background=pygame.image.load("Scoreboard Page.png").convert()
    screen.blit(background, (0,0))
    Score_Font= pygame.font.SysFont("comicsansms", 25)  #set font
    Display=Score_Font.render("HIGHSCORES",True, WHITE) #set displat 
    screen.blit (Display, (450, 0))
    Highscores=[]

    for count in range (0, len(scores_list)):
            string=str(count+1)+". "+str(scores_list[count])+chr(10) 
            string=string[0:int(len(string))-1]
            Highscores.append(string)
    
    y=30
    for item in Highscores:
        Score_Display= Score_Font.render(item, True, WHITE)  #display item 
        y+=30   #move the y-axis down 30 pixels so the next score will be diaplayed under it 
        screen.blit (Score_Display, (450, y))
    pygame.display.flip()

    while passed_variable==2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  #if user wants to quit
                passed_variable = False    #set to false, which will exit loop

            elif event.type == MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()  #get position of mouse
                x=mouse_position[0]
                y=mouse_position[1]
                if (x>25) and (x<200) and (y>25) and (y<100):  #if user clicks the "BACK" button
                    passed_variable=True   #go back to game_end screen 


            
    return passed_variable


def loop():

    keep_going = True

    game_sound = pygame.mixer.Sound("game_sound.ogg")  #load background music
    game_sound.set_volume(0.7) #set volume
    game_sound.play(-1)  #play background music on repeat
    passed_variable=True  #used to check if user wanted to quit game 
    while keep_going:

        #exit check for game_intro()
        if passed_variable==True:
            passed_variable=game_intro()
        if passed_variable==False: #if they want to quit 
            keep_going=False  #exit the game 
        
        #exit check for start_condition()
        if passed_variable==True:
            passed_variable = start_condition()
        if passed_variable == False:
            keep_going = False

        #exit check for intro_counter()
        if passed_variable==True:
            passed_variable = intro_counter()
        if passed_variable == False:
            keep_going = False        

        #exit check for game()
        if passed_variable== True:
            passed=game()  #game returns two variables
            passed_variable=passed[0]
            score=passed[1]
            score_list=Scoreboard(score) #score is used for Scoreboard()
        if passed_variable== False:
            keep_going=False

        #exit check for game_over_sequence()
        if passed_variable==True:
            passed_variable = game_over_sequence()

        if passed_variable == False:
            keep_going = False

        #sxit check for game_end()
        if passed_variable == True:
            passed_variable = game_end(score, score_list)
            

                
        if passed_variable == False:
            keep_going = False

    game_sound.stop() #stop music 
                    

                        
            
            
#importing modules        
import pygame
import random 
from pygame.locals import *
pygame.mixer.pre_init(44100, -16, 2, 1024)  #initiating sound
pygame.init()  #initiating pygame
size = (1000, 600)  #setting screen 
screen = pygame.display.set_mode(size)

#RGB colour values
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
YELLOW   = ( 255, 255,   0)

loop()  #run the game 

pygame.quit()  #exit the screen if the game is finished
