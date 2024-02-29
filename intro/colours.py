# We can re-size the terminal here
import sys
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=50, cols=150))


# Reference: https://stackoverflow.com/questions/5762491/how-to-print-color-in-console-using-system-out-println

# Coloured normal text

print("\u001b[31m Welcome to UCC!!!\u001b")
print("\u001b[32m Welcome to UCC!!!\u001b")
print("\u001b[33m Welcome to UCC!!!\u001b")
print("\u001b[34m Welcome to UCC!!!\u001b")
print("\u001b[35m Welcome to UCC!!!\u001b")
print("\u001b[36m Welcome to UCC!!!\u001b")
print("\u001b[37m Welcome to UCC!!!\u001b")

# Coloured underlined normal text
print("\u001b[4;31mWelcome to UCC!!!\u001b")
print("\u001b[4;32mWelcome to UCC!!!\u001b")
print("\u001b[4;33mWelcome to UCC!!!\u001b")
print("\u001b[4;34mWelcome to UCC!!!\u001b")
print("\u001b[4;35mWelcome to UCC!!!\u001b")
print("\u001b[4;36mWelcome to UCC!!!\u001b")
print("\u001b[4;37mWelcome to UCC!!!\u001b")

# Coloured background
print("\u001b[1;41m Welcome to UCC!!!\u001b")
print("\u001b[1;42m Welcome to UCC!!!\u001b")
print("\u001b[1;43m Welcome to UCC!!!\u001b")
print("\u001b[1;44m Welcome to UCC!!!\u001b")
print("\u001b[1;45m Welcome to UCC!!!\u001b")
print("\u001b[1;46m Welcome to UCC!!!\u001b")
print("\u001b[1;47m Welcome to UCC!!!\u001b")

# Bolded text
print("\033[0;100m Welcome to UCC!!!\033")
print("\033[0;101m Welcome to UCC!!!\033")
print("\033[0;102m Welcome to UCC!!!\033")
print("\033[0;103m Welcome to UCC!!!\033")
print("\033[0;104m Welcome to UCC!!!\033")
print("\033[0;105m Welcome to UCC!!!\033")
print("\033[0;106m Welcome to UCC!!!\033")
print("\033[0;107m Welcome to UCC!!!\033")

# High Intensity Backgrounds
print("\033[1;30m Welcome to UCC!!!\033")
print("\033[1;31m Welcome to UCC!!!\033")
print("\033[1;32m Welcome to UCC!!!\033")
print("\033[1;33m Welcome to UCC!!!\033")
print("\033[1;34m Welcome to UCC!!!\033")
print("\033[1;35m Welcome to UCC!!!\033")
print("\033[1;36m Welcome to UCC!!!\033")


