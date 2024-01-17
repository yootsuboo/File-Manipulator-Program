import sys

def read_file(inputPathName):
    with open(inputPathName, 'r') as f:
        inputContent = f.read()
    return inputContent

def write_file(outputPathName, outputContent):
    with open(outputPathName, 'w') as f:
        f.write(outputContent)


def reverse(inputPathName, outputPathName):
    inputContent = read_file(inputPathName)

    outputContent = ''
    for i in range(len(inputContent)-1, -1, -1):
        outputContent += inputContent[i]

    write_file(outputPathName, outputContent)

def copy(inputPathName, outputPathName):
    inputContent = read_file(inputPathName)

    write_file(outputPathName, inputContent)

def duplicate(inputPathName, n):
    inputContent = read_file(inputPathName)
    for _ in range(int(n)):
        with open(inputPathName, 'a') as f:
            f.write("\n" + inputContent)

def replace(inputPathName, needle, newString):
    inputContent = read_file(inputPathName)
    if needle in inputContent:
        inputContent.replace(needle, newString)

    write_file(inputPathName, inputContent)

if __name__ == "__main__":
    operation = sys.argv[1]
    inputPathName = sys.argv[2]
    thirdArg = sys.argv[3]
    fourthArg = sys.argv[4] if len(sys.argv) > 4 else None

    if operation == 'reverse':
        reverse(inputPathName, thirdArg)
    elif operation == "copy":
        copy(inputPathName, thirdArg)
    elif operation == "duplicate":
        duplicate(inputPathName, thirdArg)
    elif operation == "replace" and fourthArg is not None:
        replace(inputPathName, thirdArg, fourthArg)
    else:
        print(f'Unknown operation: {operation}')
