
import os
from colorama import Fore, Style, init

init(autoreset=True)

# Get environment variable
app_env = os.getenv("APP_ENV", "development")

print(Fore.CYAN + "Welcome to my Docker application!")
print(Fore.YELLOW + f"Current environment: {app_env}")

if app_env == "production":
    print(Fore.GREEN + "Running in production mode!")
else:
    print(Fore.MAGENTA + "Running in development mode!")

print(Style.BRIGHT + "Docker makes deploying Python apps easy!")

