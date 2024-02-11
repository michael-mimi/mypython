def hello(name, language):
    greetings = {"Englsh":"Hello", "German":"Hallo", "Spanish":"Hola"}
    message = f"{greetings[language]} {name}"
    print(message)

if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser(description="Greeting to a person.")
    parser.add_argument("-n", "--name", metavar="name",help="input the name of the person", required=True)
    parser.add_argument("-l", "--lang", metavar="language", help="choose from English, German, Spanish",choices=["English","German","Spanish"], required=True)
    args = parser.parse_args()
    hello(args.name, args.lang)
    

