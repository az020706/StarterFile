poem = '''\
Programming is fun
When the work is done
If you wanna make your work also fun
        use Python!
'''

# 'r' is read mode
# 'w' is write mode
# 't' is appending in text mode
# 'b' is binary mode

# Open for 'w'riting
f = open('poem.txt', 'w')
# Write to the file
f.write(poem)
# Close the file
f.close()

# If no mode is specified
# 'r'ead mode is assumed by default
f = open('poem.txt')
while True:
    line = f.readline()
    #Zero length indicates end of file
    if len(line) == 0:
        break
    # The 'line' already has a new line
    # at the end of each line
    # since it is reading from a file
    print(line, end='')
# Close the file
f.close()