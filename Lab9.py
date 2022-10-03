file = open("imp_file.txt", "w")
file.write("Python is an interpreted, high-level, and general-purpose programming language.")
file.close()
#########################################################################################################
file1 = input("Enter name of input file: ")
file1 = open("imp_file.txt", "r")
file2 = input("Enter name of output file: ")
print("Displaying the contents of the output file")
print(file1.read())
###########################################################################################################
try:
    file2 = open("out_file.txt")
except:
    print("out_file.txt does no exist!!!!")
#######################################################################################
file1 = open("imp_file.txt", "r")
file2 = open("out_file.txt", "w")
######################################################################################
linesforfile1 = file1.readlines()
numberoflines = len(linesforfile1)
numberofcharacters = 0
for i in linesforfile1:
    numberofcharacters = numberofcharacters + len(i)
    file2.write(i)
print("########################### after copy from input to output###################")
print("\t", numberoflines,"lines and" "\t", numberofcharacters, "characters have been copied to the output file"
      "\n" )
file1.close()
file2.close()
#####################################################################################################
file2 = open("out_file.txt", "a")
file2.write("\nIt was created by Guido van Rossum and first released in 1991.")
file2.close()
##################################################################################################

file2 = open("out_file.txt", "r")
linesforfile2 = file2.readlines()
numberoflines = len(linesforfile2)

numberofcharacters = 0
for i in linesforfile2:
    numberofcharacters = numberofcharacters + len(i)
    numberoflines = len(linesforfile2)
file2.close()
file2 = open("out_file.txt", "r")
print("####################### After appending to the output file#################################")
print("Updated Number of Lines in output file is: ", numberoflines)
print("Updated Number of characters in output file is: ", numberofcharacters)
print("\nDisplaying the content of the output file.................")
print(file2.read())
file2.close()
###############################################################################################

