import requests
from flight_deal_finder_secrets import read_secrets


LOGO = """
             ,--,                                           ,----,                      ,--,                            
          ,---.'|                               ,--,      ,/   .`|                   ,---.'|                            
    ,---,.|   | :      ,---,  ,----..         ,--.'|    ,`   .'  :          ,----..  |   | :                    ,---,.  
  ,'  .' |:   : |   ,`--.' | /   /   \     ,--,  | :  ;    ;     /         /   /   \ :   : |            ,--,  ,'  .'  \ 
,---.'   ||   ' :   |   :  :|   :     : ,---.'|  : '.'___,/    ,'         |   :     :|   ' :          ,'_ /|,---.' .' | 
|   |   .';   ; '   :   |  '.   |  ;. / |   | : _' ||    :     |          .   |  ;. /;   ; '     .--. |  | :|   |  |: | 
:   :  :  '   | |__ |   :  |.   ; /--`  :   : |.'  |;    |.';  ;          .   ; /--` '   | |__ ,'_ /| :  . |:   :  :  / 
:   |  |-,|   | :.'|'   '  ;;   | ;  __ |   ' '  ; :`----'  |  |          ;   | ;    |   | :.'||  ' | |  . .:   |    ;  
|   :  ;/|'   :    ;|   |  ||   : |.' .''   |  .'. |    '   :  ;          |   : |    '   :    ;|  | ' |  | ||   :     \ 
|   |   .'|   |  ./ '   :  ;.   | '_.' :|   | :  | '    |   |  '          .   | '___ |   |  ./ :  | | :  ' ;|   |   . | 
'   :  '  ;   : ;   |   |  ''   ; : \  |'   : |  : ;    '   :  |          '   ; : .'|;   : ;   |  ; ' |  | ''   :  '; | 
|   |  |  |   ,/    '   :  |'   | '/  .'|   | '  ,/     ;   |.'           '   | '/  :|   ,/    :  | : ;  ; ||   |  | ;  
|   :  \  '---'     ;   |.' |   :    /  ;   : ;--'      '---'             |   :    / '---'     '  :  `--'   \   :   /   
|   | ,'            '---'    \   \ .'   |   ,/                             \   \ .'            :  ,      .-./   | ,'    
`----'                        `---`     '---'                               `---`               `--`----'   `----'      

"""


class UserManager:
    def __init__(self) -> None:
        self.secrets = read_secrets
        self.SHEETY_USER_USERNAME = self.secrets["SHEETY_USER_USERNAME"]
        self.user_endpoint = (
            f"https://api.sheety.co/{self.SHEETY_USER_USERNAME}/flightDeals/users"
        )
        self.logo = LOGO
        self.welcome_print()
        self.first_name = input("What is your first name?\n")
        self.last_name = input("What is your last name?\n")
        self.email = input("What is your email?\n")
        self.email_confirm = input("Type your email again.\n")
        self.celebration = "Whoop whoop! You're in the club!"
        self.check_and_add_user()

    def add_a_new_row(self, first_name, last_name, email):
        endpoint = self.user_endpoint
        SHEETY_AUTH = self.SHEETY_USER_AUTH

        headers = {
            "Content-Type": "application/json",
            "Authorization": SHEETY_AUTH,
        }
        params = {
            "user": {
                "first": first_name,
                "last": last_name,
                "email": email,
            },
        }
        response_sheety = requests.post(url=endpoint, headers=headers, json=params)
        # print(response_sheety.status_code)

    def welcome_print(self):
        print(self.logo)
        print(
            "Welcome to Maria's Flight Club.\nWe find the best flight deals and email you.\n"
        )

    def check_and_add_user(self):
        if self.email == self.email_confirm:
            self.add_a_new_row(
                first_name=self.first_name, last_name=self.last_name, email=self.email
            )
            print(self.celebration)


if __name__ == "__main__":
    new_user = UserManager()
