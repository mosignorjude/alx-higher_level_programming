#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    content = dir(hidden_4)
    for i in range(len(content)):
        if content[i][0] != "_" and content[i][1] != "_":
            print(content[i])
