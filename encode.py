# encode
# What happens?: Any alphabet you write will be automatically switched to a letter opposite to that said letter. For example, if you write letter "a" it would switch it to letter "z", and if you do letters "abcd" it would switch it to letters "zyxw". Only english alphabets can be encoded. No special characters or numbers can.
# By Mike De La Cruz

def main():

    def encode(string):
        # Initialize encoding
        chars = "abcdefghijklmnopqrstuvwxyz"
        indx = 0 
        for i in string:
            if len(string[indx]) > 1:
                currentSubString = ""
                for sub_char in i:
                    sub_index = chars.find(sub_char)
                    indx_reversed = (-sub_index - 1)
                    reversed_char = chars[indx_reversed]
                    currentSubString = currentSubString + reversed_char
                string[indx] = currentSubString
            else:
                sub_index = chars.find(string[indx])
                indx_reversed = (-sub_index - 1)
                reversed_char = chars[indx_reversed]
                string[indx] = reversed_char
            indx += 1
        # Initialize and reorganize encoded message from the string table
        encodedMessage = ""
        for i in string:
            encodedMessage = encodedMessage + " " + i
        # Finished first stage encoding message 
        print("This is the first stage of encoded words/letters: " + encodedMessage + "\n")
        # Refreshing message variable
        encodedMessage = ""
        # Final reinforcement with encoding from pythons own encoding function
        for i in string:
            indx = string.index(i)
            reinforcedString = string[indx].encode()
            string[indx] = reinforcedString
            encodedMessage = encodedMessage + " " + str(reinforcedString)
        print("This is the final stage of encoded words/letters: " + encodedMessage + "\n"); return string
    
    def decode(string):
        print("\n🛠️ [[DECODING]]\n")

        # Initialize Pythons decoding and message variable
        encodedMessage = ""
        for i in string:
            indx = string.index(i)
            decodedString = string[indx].decode()
            string[indx] = decodedString
            encodedMessage = encodedMessage + " " + decodedString
        print("Decoded Python's encoding: " + encodedMessage + "\n")
        encodedMessage = ""
        # Initialize decoding our alphabetical encoding
        chars = "abcdefghijklmnopqrstuvwxyz"
        indx = 0
        for i in string:
            if len(string[indx]) > 1:
                currentSubString = ""
                for sub_char in i:
                    sub_index = chars.find(sub_char)
                    indx_reversed = (-sub_index - 1)
                    reversed_char = chars[indx_reversed]
                    currentSubString = currentSubString + reversed_char
                string[indx] = currentSubString
            else:
                sub_index = chars.find(string[indx])
                indx_reversed = (-sub_index - 1)
                reversed_char = chars[indx_reversed]
                string[indx] = string[indx].replace(string[indx], reversed_char)
            indx += 1
        # Reorganize decoded message from a table
        for i in string:
            encodedMessage = encodedMessage + " " + i
        # Finished decoding message 
        print("These are your decoded words/letters: " + encodedMessage + "\n")

    # Gather User Input info alphabetically 
    Data = input("\nGive me words/letters from the english alphabet. No Punctutation or Special Characters allowed yet.\n (programming logic will lowercase everything): ").lower()
    print("\n\n🛠️ [[ENCODING]]")
    print("\nThese are your original words/letters: " + Data + "\n")
    Data = Data.split()
    decode(encode(Data))

if __name__ == "__main__":
    main()