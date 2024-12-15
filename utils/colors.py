from colorama import init, Fore, Back, Style

#For windows
init(autoreset=True)

class ColorConfig:
    SUCCESS = Fore.GREEN
    ERROR = Fore.RED    
    WARNING = Fore.YELLOW  
    INFO = Fore.BLUE      
    RESET = Style.RESET_ALL  
    BOLD = Style.BRIGHT 
    
    BG_SUCCESS = Back.GREEN
    BG_ERROR = Back.RED
    
def print_success(message):
    print(f"{ColorConfig.SUCCESS}{message}{ColorConfig.RESET}")
def print_error(message):
    print(f"{ColorConfig.ERROR}{message}{ColorConfig.RESET}")
def print_warning(message):
    print(f"{ColorConfig.WARNING}{message}{ColorConfig.RESET}")
def print_info(message):
    print(f"{ColorConfig.INFO}{message}{ColorConfig.RESET}")
def print_bold(message):
    print(f"{ColorConfig.BOLD}{message}{ColorConfig.RESET}")
def print_success_bg(message):
    print(f"{ColorConfig.BG_SUCCESS}{ColorConfig.SUCCESS}{message}{ColorConfig.RESET}")
def print_error_bg(message):
        print(f"{ColorConfig.BG_ERROR}{ColorConfig.ERROR}{message}{ColorConfig.RESET}") 