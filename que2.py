def fileLength(filename):
    try:
        file = open(filename)
        lines = file.readline()
        return len(lines)
    except FileNotFoundError:
        print(f"File {filename} not found.")


