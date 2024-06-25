def convert(input_str):
    return input_str.replace(":)", "🙂").replace(":(", "🙁")

def main():
    user_input = input()
    converted_text = convert(user_input)
    print(converted_text)

if __name__ == "__main__":
    main()
