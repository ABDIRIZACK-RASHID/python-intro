marks = int(input("Enter marks scored"))
if marks >= 80 and marks <= 100: \
        print("A")
elif marks >= 60 and marks <= 79:
    print("B")
elif marks >= 40 and marks <= 59:
    print("C")
elif marks >= 0 and marks <= 39:
    print("E")
else:
    print("inalid marks")
