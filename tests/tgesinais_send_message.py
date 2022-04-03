try:
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../'
            )
        )
    )
except ImportError:
    raise


from tgesinaisbot.tgesinais import Tge_Sinais


def send_message_tge_sinais_test():
    bot = Tge_Sinais()
    bot.send_message('oi teste send message')


if __name__ == "__main__":
    send_message_tge_sinais_test()
