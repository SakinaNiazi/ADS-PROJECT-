# re module used for regular expression
import re
# np can be used to call the numpy library and related functions and data types
import numpy as np
# To load the image, we simply import the image module from the pillow and call the Image
from PIL import Image
print("Huffman Compression Program")
print("=================================================================")
option= int(input("Enter 1. if you want to input an colour image file enter 2.for default gray scale case:"))
if option == 1:
    file = input("Enter the filename:")
    # Open the image form working directory using np library
    my_string = np.asarray(Image.open(file),np.uint8)
    shape = my_string.shape
    a = my_string
    print ("Enetered string is:",my_string)
    # str() function returns the string version of the object.
    my_string = str(my_string.tolist())
elif option == 2:
    # create a numpy array from scratch
    # using arange function.
    # 1024x720 = 737280 is the amount
    # of pixels.
    # np.uint8 is a data type containing
    # numbers ranging from 0 to 255
    # and no non-negative integers
    array = np.arange(0, 737280, 1, np.uint8)
    # Reshape the array into a
    # familiar resoluition
    my_string = np.reshape(array, (1024, 720))
    print ("Enetered string is:",my_string)
    a = my_string

    my_string = str(my_string.tolist())

else:
    print("You entered invalid input")
# creates a list of characters and their frequency and a list of character in use
letters = []
only_letters = []
for letter in my_string:
    if letter not in letters:
        # frequency of each letter repetition
        frequency = my_string.count(letter)
        letters.append(frequency)
        letters.append(letter)
        only_letters.append(letter)
#generates base level nodes for the huffman tree frequency
# and letter
nodes = []
while len(letters) > 0:
    nodes.append(letters[0:2])
    letters = letters[2:]     # sorting according to frequency
nodes.sort()
huffman_tree = []
huffman_tree.append(nodes)   #Make each unique character as a leaf node
# recursively combines base nodes to create the huffman tree and allocates either a 0 or 1
# to each pair of nodes pror to combining which will be later used to create the binary code for each letter.
def combine_nodes(nodes):
    pos = 0
    newnode = []
    # get two lowest node
    if len(nodes) > 1:
        nodes.sort()
        nodes[pos].append("1")   # assigning values 1 and 0 for later use
        nodes[pos+1].append("0")
        combined_node1 = (nodes[pos] [0] + nodes[pos+1] [0])
        combined_node2 = (nodes[pos] [1] + nodes[pos+1] [1])  # combining the nodes to generate pathways
        newnode.append(combined_node1)
        newnode.append(combined_node2)
        newnodes=[]
        newnodes.append(newnode)
        newnodes = newnodes + nodes[2:]
        nodes = newnodes
        huffman_tree.append(nodes)
        combine_nodes(nodes)
    return huffman_tree       # huffman tree generation

newnodes = combine_nodes(nodes)
# tree node to be inverted this is for visualization of what you might do demonstrating on it
huffman_tree.sort(reverse = True)
print("Huffman tree with merged pathways:")
# remove dplicate items in the huffman tree and create and array CHECKLIST
#  with just node
# next block is just for printing huffman tree array

checklist = []
for level in huffman_tree:
    for node in level:
        if node not in checklist:
            checklist.append(node)
        else:
            level.remove(node)
count = 0
for level in huffman_tree:
    print("Level", count,":",level)             #print huffman tree
    count+=1
print()
# builds the binary codes for each character- easy cop-out if there is
# only 1 type of character in the string
letter_binary = []
if len(only_letters) == 1:
    lettercode = [only_letters[0], "0"]
    letter_binary.append(lettercode*len(my_string))
else:
    for letter in only_letters:
        code =""
        for node in checklist:
            if len (node)>2 and letter in node[1]:
                code = code + node[2]
        lettercode =[letter,code]
        letter_binary.append(lettercode)
print(letter_binary)
print("Binary code generated:")#genrating binary code
for letter in letter_binary:
    print(letter[0], letter[1])
#creates bitstring of the original message using the new codes you have
# generated for each letter
bitstring =""
for character in my_string:
    for item in letter_binary:
        if character in item:
            bitstring = bitstring + item[1]
binary ="0b"+bitstring  #  convert the string to an actual binary digit
print("Your message as binary is:")
                                        # binary code generated
# summary of data compression
uncompressed_file_size = len(my_string)*7
compressed_file_size = len(binary)-2
print("Your original file size was", uncompressed_file_size,"bits. The compressed size is:",compressed_file_size)
print("This is a saving of ",uncompressed_file_size-compressed_file_size,"bits")
output = open("compressed.txt","w+")
print("Compressed file generated as compressed.txt")
output = open("compressed.txt","w+")
print("Decoding.......")
output.write(bitstring)

bitstring = str(binary[2:])
uncompressed_string =""
code =""
for digit in bitstring:
    code = code+digit
    pos=0                #iterating and decoding
    for letter in letter_binary:
        if code ==letter[1]:
            uncompressed_string=uncompressed_string+letter_binary[pos] [0]
            code=""
        pos+=1

print("Your UNCOMPRESSED data is:")
if option == 1:
    temp = re.findall(r'\d+', uncompressed_string)
    res = list(map(int, temp))
    res = np.array(res)
    res = res.astype(np.uint8)
    res = np.reshape(res, shape)
    print(res)
    print("Observe the shapes and input and output arrays are matching or not")
    print("Input image dimensions:",shape)
    print("Output image dimensions:",res.shape)
    data = Image.fromarray(res)
    data.save('uncompressed.png')
    if a.all() == res.all():
        print("Success")
if option == 2:
    temp = re.findall(r'\d+', uncompressed_string)
    res = list(map(int, temp))
    print(res)
    res = np.array(res)
    res = res.astype(np.uint8)
    res = np.reshape(res, (1024, 720))
    print(res)
    data = Image.fromarray(res)
    data.save('uncompressed.png')
    print("Success")
