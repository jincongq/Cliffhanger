
The Cliffhanger Summative Project
ICS3U1-01
Mr.Cope
May 23, 2015
Pamela Zeng and Jessica Ip

In this game, the player is hanging from a cliff. The objective of the game is to
hang on as long as possible while trying to avoid getting hit by a hammer. 



### Text files ###

Cliffhanger_program.txt -> the main program containing all functions of the game and the game loop 

GAME SCORES.txt => a text file that stores the scores of players and is read from to display the top ten scores of the game onscreen



### Graphics ###

gamemenu.png => image of the menu that is used in game_intro() function 

Instructions Page x.png => images of the instruction pages that explains the game to the player. Used in the instructions() function


game_background.png => used to display the background image for the game and is called in most functions 

gamebackground1.png => used to display the background image used in the start_condition() and intro_counter() functions which includes an image of the player


person.png => used to display image of player without their fingers shown when the player has both hands on the cliff. Used in the game() and fingers() functions

left hand.png => used to display image of player without their fingers shown when the player has only their left hand on the cliff. Used in the game() and fingers() functions

right hand.png => used to display image of player without their fingers shown when the player has only their right hand on the cliff. Used in the game() and fingers() functions

no hands.png => used to display image of player without their fingers shown when the player has no hands on the cliff. Used in the game() and fingers() functions



fingers_bentxx.png => series of images of individual fingers used in fingers() function that is displayed when a key is pressed while the finger is operational

fngers_straightxx,png => series of images of individual fingers used in fingers() function that is displayed when a key is lifted while the finger is operational

fingers_hitxx,png => series of images of individual fingers used in fingers() function that is displayed when a finger is inoperational 



Game Warning Sign.png => the warning sign image used in the game() function that is displayed on top of a finger that is about to be hit by the hammer

hammer_up.png => the image of the hammer in an upright position before it hits the finger. Used in game() function to show the player where the hammer is 

hammer_down.png => the image of the hammer in its lowest position when it hits the finger. Used in game() function to show player when the hammer is hitting 



fallingx => used to display a series of images used in game_over_sequence() function that shows the player falling 

water_splash_end.png => used to display an image used in game_over_sequence() function to show that the player has fallen into the water



### Sounds ###

game_sound.ogg => the background music of the game that is called in the loop() function and is played throughout the game

beep_sound.wav => the sound that is played when the warning sign appears on the screen. Used in the game() function right before drawing the warning sign image 

hammer_sound.wav => the sound that is played when the hammer hits the finger. Used in the game() function right before drawing the hammer_down image 

scream_sound.wav => the sound that is played when the player is falling after all their fingers are inoperational. USed in the game_over_sequence() function 

splash_sound.wav => the sound that is played along with the water_splash_end.png image when the player falls into the water. Used in the game_over_sequence() function



 