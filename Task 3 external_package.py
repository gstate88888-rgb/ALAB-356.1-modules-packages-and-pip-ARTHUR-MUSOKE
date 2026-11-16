# Requires colorama
# Install with: pip install colorama

from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

print(Fore.GREEN + "Colorama is working successfully!")
print(Fore.BLUE + "This text is blue.")
print(Fore.RED + "This text is red.")
print(Style.RESET_ALL)
