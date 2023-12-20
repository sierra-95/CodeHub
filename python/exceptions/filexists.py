#!/usr/bin/env python3
def file_not_exist_error():
    raise OSError("File doesn't exist")

def unexpected_error():
    raise RuntimeError("Something unexpected happened while reading the file")

def main():
    file_exists = False
    something_unexpected = True  # Simulating an unexpected scenario during reading

    try:
        if not file_exists:
            file_not_exist_error()
        
        if something_unexpected:
            unexpected_error()

        file=open("0main.py", "r")
        content = file.read()
        print("File content:", content)
        file.close()
    except OSError as os_err:
        print("Caught an OS error:", os_err)
    except RuntimeError as rt_err:
        print("Caught a runtime error:", rt_err)

if __name__ == "__main__":
    main()
