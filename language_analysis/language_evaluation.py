# search the string for any of the words from json that are banned


def arb():
    print("")


def response_handler():
    print("")


def get_chat_tone(sentiment_polarity):

    def tone_generator(chattone):
        if chattone == 1:
            tone = "Positive"
        elif chat_tone == 2:
            tone = "Negative"
        else:
            tone = "Average"

        return tone

    rounded_sent_pol = round(sentiment_polarity, 2)
    if rounded_sent_pol >= .80:
        chat_tone = 1
    elif rounded_sent_pol <= .25:
        chat_tone = 2
    else:
        chat_tone = 3

    tone = tone_generator(chat_tone)
    return tone


if __name__ == '__main__':
    arb()
