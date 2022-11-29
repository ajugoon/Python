import time

sum = 0
def question1():
    global sum
    tic = time.perf_counter()
    print("What is 2+2?")
    sum = str(input("Answer? \n"))
    print (sum)
    toc = time.perf_counter()
    print(f"You answered this question in {toc - tic:0.4f} seconds")

def main():

    question1()
        
main()

