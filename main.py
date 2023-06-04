from telegram.auto_auth import *

def main():
    auth_core = AutoAuth(os.path.join(os.path.dirname(__file__), 'auth', 'save_sessions'))

    result_connect = auth_core.check_connect()

    if not result_connect:
        auth_core.aut_start()

    print()


    #


if __name__ == '__main__':
    main()
