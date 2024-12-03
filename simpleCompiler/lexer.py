import re ##regex library
##  We have to store our tokens in a list of tuples

TOKENS = [
    ('int\\b','INT'),
    ('void\\b','VOID'),
    ('return\\b','RETURN'),
    ('\\(','OPEN_PARANTHESIS'),
    ('\\)','CLOSE_PARANTHESIS'),
    ('{','OPEN_BRACE'),
    ('}','CLOSE_BRACE'),
    (';','SEMICOLON'),
    ('[a-zA-Z_]\\w*\\b','IDENTIFIER'),
    ('[0-9]+\\b', 'CONSTANT')
    
]


def lookup(s):
    longest_match = None
    longest_value = None
    for pattern, value in TOKENS:
        match = re.match(pattern, s)
        if match:
            ##print(f"-----Found-----{value}")
            if longest_match is None or len(match.group(0)) > len(longest_match.group(0)):
                longest_match = match
                longest_value = value
    if longest_match:
        return longest_value
    else:
        print("Error lexer my man")
        return False


def read_file(file_path):
    with open(file_path,'r') as file:
        lines = file.readlines()
    return lines

## Spliting the file
def split_by_delimeters(file):
    split_string = []
    delimeters = '[ ;{}\\(\\)]'
    pattern = f"({delimeters})"
    ##splitting spaces, semicolons, paranthesis
    index = 0
    for line in file:
        splity_gonzalez = re.split(pattern, line)
        ## filtering ['', ' ', '\n']
        splity_gonzalez_filtered = [item for item in splity_gonzalez if item not in ['', ' ','\n']]
        ## Apending if the list is not empty after
        if not splity_gonzalez_filtered:
            pass #we do nothing if the list is empty
        else:
            split_string.append(splity_gonzalez_filtered)
        index += 1 
    return split_string

## Tokenize
def tokenize(filtered_file):
    tokenized_file = []
    for line in filtered_file:
        tokenized_line = []
        for item in line:
            tokenized_item = lookup(item)
            if not tokenized_item:
                return False
            tokenized_line.append(tokenized_item)
        tokenized_file.append(tokenized_line)
    return tokenized_file 

'''
while input isn't empty:
    if input starts with whitespace:
        trim whitespace from start of input
    else:
        find longest match at start of input  for any regex
        if no match is found, raise an error
        convert matching substring into a token
        remove matching substring from startof input
'''

def main(file):
    file_lines = read_file(file)
    file_split_filtered = split_by_delimeters(file_lines)
    file_tokenized = tokenize(file_split_filtered)
    if file_tokenized is False:
        return False
    print(file_tokenized)
    return True
