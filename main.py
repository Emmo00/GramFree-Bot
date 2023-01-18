from bot import Bot


def main():
    bot = Bot()
    print('video time')
    bot.video()
    print('video done')
    bot.go_home()
    print('contract time')
    bot.smart_contracts()
    bot.close_window()
    print('all done')


if __name__ == '__main__':
    main()
