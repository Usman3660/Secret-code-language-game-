import random

def encode(word):
    if len(word) >= 3:
        first_letter = word[0]
        rest = word[1:] + first_letter
        random_prefix = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=3))
        random_suffix = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=3))
        return random_prefix + rest + random_suffix
    else:
        return word[::-1]

def decode(word):
    if len(word) <= 5: 
        return word[::-1]
    else:
        trimmed_word = word[3:-3] 
        last_letter = trimmed_word[-1]
        rest = trimmed_word[:-1]
        return last_letter + rest

def main():
    encoded_messages = []  
    while True:
        choice = input("Do you want to encode or decode a message? (Type 'code', 'decode', or 'exit' to quit): ").strip().lower()

        if choice == 'code':
            message = input("Enter the message to encode: ").strip()
            words = message.split()
            encoded_words = [encode(word) for word in words]
            encoded_message = ' '.join(encoded_words)
            encoded_messages.append(encoded_message)  
            print("Encoded message:", encoded_message)

        elif choice == 'decode':
            if not encoded_messages:
                print("No encoded messages are stored yet.")
            else:
                print("Stored encoded messages:")
                for i, em in enumerate(encoded_messages, start=1):
                    print(f"{i}: {em}")
                selected_index = int(input("Select the message number to decode (enter the number): ")) - 1
                if 0 <= selected_index < len(encoded_messages):
                    message = encoded_messages[selected_index]
                    words = message.split()
                    decoded_words = [decode(word) for word in words]
                    decoded_message = ' '.join(decoded_words)
                    print("Decoded message:", decoded_message)
                else:
                    print("Invalid selection.")

        elif choice == 'exit':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please type 'code' to encode, 'decode' to decode, or 'exit' to quit.")

if __name__ == "__main__":
    main()
