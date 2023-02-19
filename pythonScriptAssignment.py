import glob
import os
from collections import OrderedDict
import socket
from pathlib import Path

dir_path = os.path.dirname(os.path.realpath(__file__))

parent_path = Path(dir_path).parent
data_path = str(parent_path)+"/data"
#print(data_path)
os.chdir(data_path)
myFiles = glob.glob('*.txt')

output = open("../output/result_.txt", "w")
output.write("Files in home/data are : ")
output.write('\n')
for x in myFiles :
    #print(x)
    output.write(x)
    output.write('\n')

output.close()

total_words = 0

for x in myFiles :
    file = open(x, "r")
    data = file.read()
    words = data.split()
    output = open("../output/result_.txt", "a")
    output.write("Total number of words in "+x+" file are: " + str(len(words)))
    output.write('\n')
    output.close()    
    total_words = total_words + len(words)
    file.close()

output = open("../output/result_.txt", "a")
output.write("Total number of words in both files are: " + str(total_words))
output.write('\n')
output.close()

frequency = {}
curr_file = "/home/data/IF.txt"

document_text = open(curr_file, 'r')
text_string = document_text.read()
words = text_string.split()
 
for word in words:
    count = frequency.get(word,0)
    frequency[word] = count + 1

frequency_list_desc_order = sorted(frequency, key=frequency.get, reverse=True)

output = open("../output/result_.txt", "a")
output.write("Top 3 words in the IF.txt are :")
output.write('\n')

ip_addr = socket.gethostbyname(socket.gethostname())

for word in frequency_list_desc_order[:3]:
    line = word + " : " + str(frequency[word])
    output.write(line)
    output.write('\n')

output.write("IP address of the machine is: " + ip_addr + "\n")
output.close()