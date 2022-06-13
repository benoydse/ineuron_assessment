# A function in python to read the text file and replace specific content of the file.

def replace_in_file(filename, string_to_be_replaced, new_string):
    # First open the file in the read mode
    with open(filename, 'r') as f:
        content = f.read()      # read the content of the file
    new_content = content.replace(string_to_be_replaced, new_string)        # replace the old string with the new string
    with open(filename, 'w') as f:      # Now open the file in write mode
        f.write(new_content)        # finally, write the new content to the file


replace_in_file('example.txt', 'placement', 'screening')
