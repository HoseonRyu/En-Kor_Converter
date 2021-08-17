from model.Hangul import HangulMe

def main():
    converter = HangulMe()
    flg = True
    print('Type "fin" When you want to stop the program.')
    while flg:
        input_ = input("")
        if input_ == "fin":
            break
        string = converter.sequence(input_)
        print(f"{string}")
    print("done!\n")

    
if __name__ == "__main__":
    main()
