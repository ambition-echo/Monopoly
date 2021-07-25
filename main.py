import background
import threading
import show


def main():
    background_ = threading.Thread(target=background.main)
    show_ = threading.Thread(target=show.main)
    background_.start()
    show_.start()


if __name__ == '__main__':
    main()
