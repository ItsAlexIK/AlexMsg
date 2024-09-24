import requests
import os
from termcolor import colored

BASE_URL = 'https://alex-msg.fly.dev/'

token = None
TOKEN_FILE = 'token.txt'

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_header():
    header = r"""
  █████╗ ██╗     ███████╗██╗  ██╗    ███╗   ███╗███████╗ ██████╗ 
 ██╔══██╗██║     ██╔════╝╚██╗██╔╝    ████╗ ████║██╔════╝██╔════╝ 
 ███████║██║     █████╗   ╚███╔╝     ██╔████╔██║███████╗██║  ███╗
 ██╔══██║██║     ██╔══╝   ██╔██╗     ██║╚██╔╝██║╚════██║██║   ██║
 ██║  ██║███████╗███████╗██╔╝ ██╗    ██║ ╚═╝ ██║███████║╚██████╔╝
 ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝    ╚═╝     ╚═╝╚══════╝ ╚═════╝ 
    """
    print(colored(header, 'cyan'))

def load_token():
    global token
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'r') as file:
            token = file.read().strip()

def save_token(new_token):
    global token
    token = new_token
    with open(TOKEN_FILE, 'w') as file:
        file.write(token)

def register(username, password):
    response = requests.post(f'{BASE_URL}/register', json={'username': username, 'password': password})
    if response.status_code == 200:
        print(colored("Registration successful!", 'green'))
    else:
        print(colored("Registration failed!", 'red'), response.json().get('error', 'Unknown error'))

def log_in(user, password):
    response = requests.post(f'{BASE_URL}/login', json={'username': user, 'password': password})
    if response.status_code == 200:
        print(colored("Login successful!", 'green'))
        save_token(response.json().get('token'))
        main()
    else:
        print(colored("Login failed!", 'red'), response.json().get('error', 'Unknown error'))

def log_out():
    global token
    token = None
    if os.path.exists(TOKEN_FILE):
        os.remove(TOKEN_FILE)
    print(colored("Successfully logged out.", 'red'))

def get_username():
    global token
    if token:
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get(f'{BASE_URL}/get_username', headers=headers)
        if response.status_code == 200:
            return response.json().get('username')
    return None

def send_message(receiver, message):
    global token
    if token:
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.post(f'{BASE_URL}/send_message', json={'receiver': receiver, 'message': message}, headers=headers)
        if response.status_code == 200:
            print(colored(f"Message sent to {receiver}", 'green'))
        else:
            print(colored("Failed to send message:", 'red'), response.json().get('error', 'Unknown error'))
    else:
        print(colored("You need to log in first", 'yellow'))

def show_history():
    global token
    if token:
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get(f'{BASE_URL}/history', headers=headers)
        if response.status_code == 200:
            messages = response.json().get('messages', [])
            if messages:
                print(colored("\nMessage History:", 'cyan', attrs=['bold']))
                print(colored("=" * 50, 'cyan'))
                for msg in messages:
                    print(f"{colored('From:', 'yellow')} {msg['sender']}, {colored('Content:', 'yellow')} {msg['content']}")
                print(colored("=" * 50, 'cyan'))
            else:
                print(colored("No message history found.", 'yellow'))
        else:
            print(colored("Failed to retrieve message history:", 'red'), response.json().get('error', 'Unknown error'))
    else:
        print(colored("You need to log in first to view message history.", 'yellow'))

def display_commands():
    commands = f"""
{colored(' Available Commands:', 'cyan', attrs=['bold'])}
{colored('┌' + '─' * 45 + '┐', 'cyan')}
{colored('│', 'cyan')} {colored('help', 'blue'):<30} {colored('       Show help menu', 'cyan'):<20} {colored('│', 'cyan')}
{colored('│', 'cyan')} {colored('msg-history', 'blue'):<30} {colored(' Show message history', 'cyan'):<20} {colored('│', 'cyan')}
{colored('│', 'cyan')} {colored('login name pwd', 'blue'):<30} {colored('          Log in user', 'cyan'):<20} {colored('│', 'cyan')}
{colored('│', 'cyan')} {colored('send name message', 'blue'):<30} {colored('       Send a message', 'cyan'):<20} {colored('│', 'cyan')}
{colored('│', 'cyan')} {colored('register name pwd', 'blue'):<30} {colored('  Register a new user', 'cyan'):<20} {colored('│', 'cyan')}
{colored('│', 'cyan')} {colored('logout', 'dark_grey'):<30} {colored('         Log out user', 'cyan'):<20} {colored('│', 'cyan')}
{colored('│', 'cyan')} {colored('exit', 'dark_grey'):<30} {colored(' Exit the application', 'cyan'):<20} {colored('│', 'cyan')}
{colored('└' + '─' * 45 + '┘', 'cyan')}"""
    print(commands)

def interactive_mode():
    username = get_username()
    logged_in_status = f"Logged in as: {username}" if username else "Not logged in"
    
    print(colored(f"Status: {logged_in_status}", 'yellow'))
    print(colored("Type 'help' for help", 'yellow'))

    should_exit = False

    while not should_exit:
        command = input(colored("\n>>> ", 'green')).strip().split()

        if not command:
            continue

        cmd = command[0]

        if cmd in ['help']:
            display_commands()
        elif cmd in ['register', 'reg', 'r']:
            if len(command) == 3:
                register(command[1], command[2])
            else:
                print(colored("Usage: register name password", 'red'))
        elif cmd in ['login', 'log', 'l']:
            if len(command) == 3:
                log_in(command[1], command[2])
            else:
                print(colored("Usage: login name password", 'red'))
        elif cmd in ['send', 's']:
            if username:
                if len(command) >= 3:
                    receiver = command[1]
                    message = ' '.join(command[2:])
                    send_message(receiver, message)
                    should_exit = True
                else:
                    print(colored("Usage: send name message", 'red'))
            else:
                print(colored("You need to log in first to send messages.", 'yellow'))
        elif cmd in ['msg-history', 'mh', 'msg-h']:
            show_history()
            should_exit = True
        elif cmd in ['logout', 'log-out', 'lo']:
            log_out()
            username = get_username()
            logged_in_status = f"Logged in as: {username}" if username else "Not logged in"
            print(colored(f"Status: {logged_in_status}", 'yellow'))
            should_exit = True
        elif cmd in ['exit']:
            print(colored("Exiting application...", 'green'))
            should_exit = True
            break
        else:
            print(colored("Invalid command or arguments. Type 'help' for available commands.", 'red'))

def main():
    clear_terminal()
    display_header()
    load_token()

    interactive_mode()

if __name__ == "__main__":
    main()