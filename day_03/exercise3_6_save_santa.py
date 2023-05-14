print("Welcome to the Save Santa game.")
print("Your mission is to find Santa Clause while dealing with challenges to save him.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

chimney_drawing = """
   |                         |____|____|____|/|                       |
   |  _______________        |__|____|____|_|/|     ___________       |
   | |       |    (_)|       |____|____|____|/|    |           |      |
   | |_______|_______|       |__|____|____|_|/|    | Santa's   |      |
   | |       |       |       |____|____|____|/\    |   Sweet   |      |
   | |_______|_______|      /___|____|____|__\/\   |    Home!  |      |
   |                       /_|____|____|____|_\/\  |___________|      |
   |                      /_____|____|____|____\/\                    |
   |                     /___|____|____|____|___\/\                   |
   |        ____        /_|___|  .  ..  .  |___|_\/|                  |
   |       /////_       |_____| . ./\/\  . |_____|/|                  |
   |      ooooo//_      |_|___| . (oo)o)  .|___|_|/|_                 |
   |____ ooooooo//_____/|_____|  [======]  |_____|/ /|________________|
   |    ooooooooo//   /____________________________//                 |
   |   ooooooooooo    |____________________________/                  |
   |                     /                   /                        |
   |                    /                   /                         |
   |                   /___________________/                          |
   |__________________________________________________________________|
"""

troll_drawing = """ \n
               _________
              |#########|
              |#########|
              |#########|
              |#########|
              |#########|
            __|_________|__
              |     '_ ' \
              F     (.) (.)--.__
             /                  `.
            J                    |
            F       ._          .'
           J          `-.____.-'
           F           \
          J             \
          |              \---
          |  .  `.        \_E
          |   `.  `.       L
 ,,,      |     `.  `.     |
\VVV'     |       `.  `    |
 \W|      J         ```    F
  `.    .' \              /
    `--'    )    ____.-  '
           /    /   `.   `.  .-
          /   .'      `.   `' /
          `.  \         `.   /
            `._|          `-'    \n"""


die_drawing = """ 
                                   .-/-o
                                  / /'
                             .--./ /     
                                 O'-._
                                      ` """


waterfall_draw = '''\n
                                                     ---\=,__,>,_`-.     |
       :  |  `"""V#######,,_ `-  ""##################' --z--;" /_/  `. `.   |
          |          `/"""".`|`|| } }|.""""""""|"""""  --'//`/'  `    \  '. |
    :          :      |:     ||   |  |  :   :  |   :   ,_\---_\._   :  `.\ |/
                   :  /  :   |  |   || :  :      :    //--'> ___ ``-,_   \  \
         `"^            :  ` ||   || |   :  :         '=-`',' / `-, __`-. |
      :    :          : :  : |  |    ||    :     ---  //7;<\     / ,--._ ` |
         .,      :        :  |   ||| || '       :     -/;\'/` -='/|(    \ \
        %#'            :    `| |||    |  :   :      :  // '\   // | `    | |
    :         :   `'   :  :  || # | |||    :            `    .        :  | 
                         :   | ||#|#| | ':    :    :             :       ` 
         '#"      :   :    : | ||,|, ||   :      /        :           |:  ||
  ""'                    :  \\|\ X XX///`      :|   :    |   :      : |   |
  \n
            '''


run_draw = """ \n

                        ,////,
                        /// 6|
                        //  _|
                       _/_,-'
                  _.-/'/   \   ,/;,
               ,-' /'  \_   \ / _/
               `\ /     _/\  ` /
                 |     /,  `\_/
                 |     \'
 pb  /\_        /`      /\
   /' /_``--.__/\  `,. /  \
  |_/`  `-._     `\/  `\   `.
            `-.__/'     `\   |
                          `\  \
                            `\ \
                              \_\__
                               \___)
                                \n"""


fire_drawing = """\n
    
    ,.   (   .      )        .      "
   ("     )  )'     ,'        )  . (`     '`
 .; )  ' (( (" )    ;(,     ((  (  ;)  "  )"
 _"., ,._'_.,)_(..,( . )_  _' )_') (. _..( '
 \n """

unicorn_draw = """

                  .
                 /'
                //
            .  //
            |\//7
           /' " \
          .   . .
          | (    \     '._
          |  '._  '    '. '
          /    \'-'_---. ) )
         .              :.'
         |               \
         | .    .   .     .
         ' .    |  |      |
          \^   /_-':     /
          / | |    '\  .'
         / /| |     \\  |
         \ \( )     // /
          \ | |    // /
           L! !   // /
            [_]  L[_| 
"""

window_draw = """

   o=(=(=(=(=(=(=)=)=)=)=o
     !-'-'-'-/_\-'-'-'-! 
     ! !  , /___\`  ! !!
     !!! , /  |  \`  ! !
     !!  ,|___|___`  !!!
     !_,| |_______|` `_!
     !-`| |       | |,-!
     !!!! |       | ! !!
     !!!! |       | !!!!
     !!!!_|_______|_!!!!
     !!!!___________!!!! 
     !!!!           !!!!   
     !!!!           !!!!   
     !!!!           !!!!  """

# Write your code below this line 👇
print(chimney_drawing)
escape_home = input(
    "You arrived at Santa's home but there's no one inside. You hear some noises ourside and you want to hide. Your options are: chimney, door or window. What do you chose? Please write chimney, door or window.\n"
)
escape_home_new = escape_home.lower()
escape_troll = ""
if escape_home_new == "door":
    print(troll_drawing)
    escape_troll = input(
        "You're outside the house where a huge troll looks at you with hungry eyes. You only have two posibilities: run or fight. What are you going to do? Please write run or fight.\n"
    ).lower()
    if escape_troll == "fight":
        print(
            f"{die_drawing} \n The troll is very powerful and agile so it catch you with no effort and eats you. You die! \n GAME OVER!"
        )
    elif escape_troll == "run":
        print(run_draw)
        answer_escape_troll = input(
            "The troll is very heavy so you were able to escape. Now you are very tired and  you can keep going or sleep. What do you want to do?  Please write sleep or go. \n"
        ).lower()
        if answer_escape_troll == "sleep":
            print(
                f"{die_drawing} \n The troll finds you and eats you. You die! \n GAME OVER!"
            )
        elif answer_escape_troll == "go":
            print(
                f"{waterfall_draw} \n You find a river and a garage where Santa Clause is sleeping with a bottle of vodka on his side. You win! \n GAME OVER!"
            )
        else:
            escape_troll = input("Your decision was wrong. Game Over!")

elif escape_home_new == "chimney":
    print(
        f"{fire_drawing} \n The chimney is automatic, so if detects something, unles is Santa, starts a huge fire which burns you. You die! \n GAME OVER!"
    )

elif escape_home_new == "window":
    print(window_draw)
    window = input(
        "There's no one here, so you are save. You can go both right or left. Where do you want to go? Please write right or left. \n"
    ).lower()
    if window == "right":
        print(
            f"{waterfall_draw} \n You find a river and a garage where Santa Clause is sleeping with a bottle of vodka on his side. You win! \n GAME OVER!"
        )
    elif window == "left":
        print(
            f"{unicorn_draw} \n You arived to a new world where the unicorns are huge and one of them tramples you. You die \n GAME OVER!"
        )
    else:
        print("Your decision was wrong. Game Over!")
else:
    escape_troll = input("Your decision was wrong. Game Over!")
