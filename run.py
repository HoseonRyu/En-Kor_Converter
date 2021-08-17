from model.Hangul import HangulMe

QUERY = "dkssudgktjldy"

def main():
    converter = HangulMe()
    string = converter.sequence(QUERY)
    print(f"{string}")

if __name__ == "__main__":
    main()