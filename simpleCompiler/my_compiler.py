import sys
import os
import lexer


## Check if it has an argument
def check_if_arg():
    if len(sys.argv) < 2 or not sys.argv[1].strip() or len(sys.argv) >= 4 :
        print("Usage: python3 my_compiler.py <input_file> [--lex | --parse | --codegen]")
        return False
    return True



## we check if the file argv-isvalid
def is_valid_file(file_path):
    if not (os.path.exists(file_path) and os.path.isfile(file_path)):
        print("Cant find the file")
        return False
    return True

def stop_at_lexer(file):
    lexer.main(file)
    

def stop_at_parser(file):
    stop_at_lexer(file)
    print("No parser yet")

def stop_at_codegen(file):
    stop_at_parser(file)
    print("No codegen yet")

def special_case(selection,file):
    if selection == "--lex":
        print("Stopping at lexer")
        stop_at_lexer(file)
    elif selection == "--parse":
        print("Stopping at parser")
        stop_at_parser(file)
    elif selection == "--codegen":
        print("Stopping at codegen")
        stop_at_codegen(file)
    else:
        print("Dont have that argument")
        sys.exit()

## main function
def main():
    ## First Steps
    if not check_if_arg() :
        sys.exit()
    file_ = sys.argv[1]
    if not is_valid_file(file_):
        sys.exit()
    
    if len(sys.argv) == 3:
        special_case(sys.argv[2],file_)
    
        
    ## Select What to run if specified
if __name__ == "__main__":
    main()




