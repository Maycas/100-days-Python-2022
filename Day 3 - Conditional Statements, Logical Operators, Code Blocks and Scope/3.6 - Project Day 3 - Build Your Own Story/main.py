# ASCII art
treasure_chest = '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
'''

orc = '''
                        _,.---''```````'-.
                    ,-'`                  `-._
                 ,-`                   __,-``,\ 
                /             _       /,'  ,|/ \ 
              ,'         ,''-<_`'.    |  ,' |   \ 
             /          / _    `  `.  | / \ |\  |
             |         (  |`'-,---, `'  \_|/ |  |
             |         |`  \  \|  /  __,    _ \ |
             |         |    `._\,'  '    ,-`_\ \|
             |         |        ,----      /|   )
             \         \       / --.      {/   /|
              \         | |       `.\         / |
               \        / `-.                 | /
                `.     |     `-        _,--V`)\/        _,-
                  `,   |           /``V_,.--`  \.  _,-'`
                   /`--'`._        `-'`         )`'
                  /        `-.            _,.-'`
                              `-.____,.-'`
'''

piranha = '''
          ,---,
  _    _,-'    `--,
 ( `-,'            `\ 
  \           ,    o \ 
  /   ,       ;       \ 
 (_,-' \       `, _  ""/
        `-,___ =='__,-'
              ````
'''

beast = '''
                   (    )
                  ((((()))
                  |o\ /o)|
                  ( (  _')
                   (._.  /\__
                  ,\___,/ '  ')
    '.,_,,       (  .- .   .    )
     \   \ \     ( '        )(    )
      \   \ \    \.  _.__ ____( .  |
       \  /\ \   .(   .'  /\  '.  )
        \(  \ \.-' ( /    \/    \)
         '  ()) _'.-|/\/\/\/\/\|
             '\ \ .( |\/\/\/\/\/|
               '((  \    /\    /
               ((((  '.__\/__.')
                ((,) /   ((()   )
                 "..-,  (()("   /
                  _//.   ((() ."
          _____ //,/" ___ ((( ', ___
                           ((  )
                            / /
                          _/,/'
                        /,/,"
'''

python = '''
       ---_ ......._-_--.
      (|\ /      / /| \  \
      /  /     .'  -=-'   `.
     /  /    .'             )
   _/  /   .'        _.)   /
  / o   o        _.-' /  .'
  \          _.-'    / .'*|
   \______.-'//    .'.' \*|
    \|  \ | //   .'.' _ |*|
     `   \|//  .'.'_ _ _|*|
      .  .// .'.' | _ _ \*|
      \`-|\_/ /    \ _ _ \*\ 
       `/'\__/      \ _ _ \*\ 
      /^|            \ _ _ \*
     '  `             \ _ _ \      
                       \_
'''

# Main script
print(treasure_chest)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure!") 

#Write your code below this line 👇
player_command = input("You are prepared to go on your journey and leave your village to find your fortune, but soon enough, you're at a crossroad. Where do you want to go? Type \"left\" or \"right\" > ").lower()

if player_command == "left":
    player_command = input("You've come to a lake, and, far away, you see an island in the middle of that lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across > ").lower()

    if player_command == "wait":
        player_command = input("An old man with a boat came and offered his services to cross. You arrive at the island unharmed. However, there is a house with 3 doors. One red, one yellow and one blue. Which color do you choose? > ").lower()

        if player_command == "yellow":
            print("As soon as you open the door, you see a glare that seems like.. GOLD! The treasure is waiting for you to pick it up! You win!")
        elif player_command == "red":
            print(beast)
            print("You open the red door slowly and find yourself facing a beast with an axe. You try to dodge its blow, but you are unlucky and it splits your head from your body. GAME OVER")
        elif player_command == "blue":
            print(python)
            print("You open the door and everything is pretty dark. You light a fire and right in front of you lays a huge snake, a python. It immediately jumps at you and eats you alive. GAME OVER")
        else:
            print("Being aware of the traps the doors could hide, you can't choose as you don't want to die a painful death. Instead, you decide to go back home and leave the treasure for the next idiot that decides to put their life at risk. GAME OVER")

    else:
        print(piranha)
        print("The lake was full of piranhas and they ate you alive. GAME OVER")

else:
    print(orc)
    print("You found a deadly orc, too strong for you to beat right now. GAME OVER")
    
