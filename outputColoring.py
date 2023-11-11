"""This script can be imported as a module and used as a library. """

CRED = '\033[91m'
CGREEN = '\033[92m'
CEND = '\033[0m'

    
def print_error(message):
    print(f"{CRED}{message}{CEND}")
    
def print_success(message):
    print(f"{CGREEN}{message}{CEND}")

def main():
    print_error("Welcome err")
    print_success("Welcome_success")    


if __name__ == '__main__':
    main()
    