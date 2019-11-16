from globals import API_INFO

sentiment_polarity = []


def arb():
    print("")


def get_sentiment(input_text):
    inputVar = input_text
    documents = [  # Dictionary to hold basic values for the API to evaluate
        {
            "id": "1",
            "language": "en",
            "text": inputVar
        }
    ]

    sent_polarity = API_INFO.azure_text_analytics.sentiment(documents=documents)  # adding a variable for sentiment polarity
    for document in sent_polarity.documents:  # for loop to search the list for docnames and scan text for polarity
        sentiment_polarity.append("{:.4f}".format(document.score))  # appending sentiment polarity to new list

    polarity = round(float(sentiment_polarity[0]), 4)
    sentiment_polarity.clear()
    return polarity


if __name__ == '__main__':
    arb()

