from telegram.auto_auth import *

def main():
    auth_core = AutoAuth(os.path.join(os.path.dirname(__file__), 'auth', 'save_sessions'))
    auth_core.aut_start()
    print()
    pass


if __name__ == '__main__':
    main()
