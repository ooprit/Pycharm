# A - Z 65-90
# a-z  97-122
# ord(letter)
# chr (code)

orig_string = input ("Enter string to code : ")
shift = input ("enter number of characters to shift : ")
shift = int(shift)
def code(char, shift):
    if char.isalpha():
        if char.isupper() and (ord(char)+shift<=ord("Z")):
            return (chr(ord(char)+shift))
        elif char.islower() and (ord(char)+shift<=ord("z")):
            return (chr(ord(char)+shift))
        else:
            return (chr(ord(char)+shift-26))
    else:
        return (char)

def decode (char, shift):
    if char.isalpha():
        if (char.isupper() and (ord(char)-shift)<ord("A")):
            return (chr(ord(char) - shift+26))
        elif char.islower() and (ord(char) - shift < ord("a")):
            return (chr(ord(char) - shift+26))
        else:
            return (chr(ord(char) - shift))
    else:
        return (char)

coded_string = ""
for char in orig_string:
    coded_string += code(char, shift)
#    print (code(char, shift))

print ("coded string : ", coded_string)


decoded_string = ""

for char in coded_string:
    decoded_string += decode(char, shift)

print ("decoded string : ", decoded_string)


