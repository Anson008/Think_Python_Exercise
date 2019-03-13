def sed(pattern, replacement, source, dest):
    try:
        fin1 = open(source, "r")
        fin2 = open(dest, "w")
    except:
        print("An error occurs when trying to open file!")

    for line in fin1:
        line = line.replace(pattern, replacement)
        fin2.write(line)

    fin1.close()
    fin2.close()


def main():
    patt = "bear"
    repl = "deer"
    source = "sed_test.txt"
    dest = source + "_replaced.txt"
    sed(patt, repl, source, dest)


if __name__ == "__main__":
    main()

