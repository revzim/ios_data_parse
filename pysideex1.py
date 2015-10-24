#andyzim
import sys, os
from PySide import QtGui
import glob

app = QtGui.QApplication(sys.argv)
gui = QtGui.QWidget()
input_text = "Please enter the directory followed by what is inside the quotations \"/*.file_extention\".\nFor the .file_extention, for example, if you want every file that is a txt file, you would replace '.file_extention' with '*.txt':\n"
path = ""

text, ok = QtGui.QInputDialog.getText(gui, "question", input_text)

path_wo_ext = text[0:52]

if ok and os.path.isdir(path_wo_ext):
    app.exit()
    path = text
    print "%s is found and available" % path
else:
    app.exit()
    print "Chose to exit"
file_contents = []

def get_file_contents():
    if ok and os.path.isdir(path_wo_ext):
        files = glob.glob(path)
        for f in files:
            f = open(f, 'r')
            for l in f:
                file_contents.append(l)
                print "\n"
        f.close()
        return get_file_contents
    else:
        if len(path) >= 1:
            print "The path you have given, %s, was not found or does not exist" % path
            app.exit()
            print"Chose to exit"
        else:
            print

#array for each key and value
keys_and_values_ar = []
keys_and_values_dict = {}
def parse_contents():
    get_file_contents()
    #print file_contents
    for l in file_contents:
        fields = l.split("\r\n")

        #print fields
        keys_and_values_ar.append(fields)
   #print keys_and_values_ar
    return keys_and_values_ar

#split into fields
def split_fields():
    subset_data = ''
    parse_contents()
    for subset in keys_and_values_ar:
       subset = subset[0]
       split_subset = subset.split(":")
       print split_subset

split_fields()
