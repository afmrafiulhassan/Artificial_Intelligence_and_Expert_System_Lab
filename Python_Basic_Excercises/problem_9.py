#Write a Python program that accepts a filename from the user and prints the extension of the file.

fileName = input("Enter a file name: ")
fileExtension = fileName.split('.')[-1]

print("Your file extension is '.{}'.".format(fileExtension))
