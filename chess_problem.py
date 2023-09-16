print ('░█████╗░██╗░░██╗███████╗░██████╗░██████╗')
print ('██╔══██╗██║░░██║██╔════╝██╔════╝██╔════╝')
print ('██║░░╚═╝███████║█████╗░░╚█████╗░╚█████╗░')
print ('██║░░██╗██╔══██║██╔══╝░░░╚═══██╗░╚═══██╗')
print ('╚█████╔╝██║░░██║███████╗██████╔╝██████╔╝')
print ('░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░')
print ('')
print ('██╗░░░██╗██████╗░░░░░█████╗░')
print ('██║░░░██║╚════██╗░░░██╔══██╗')
print ('╚██╗░██╔╝░░███╔═╝░░░██║░░██║')
print ('░╚████╔╝░██╔══╝░░░░░██║░░██║')
print ('░░╚██╔╝░░███████╗██╗╚█████╔╝')
print ('░░░╚═╝░░░╚══════╝╚═╝░╚════╝░')
print ('')
print ('This program visualizes the solution to the problem: Place n queens on a chessboard n*n so that no queen beats the other\n ')



def printmas():
    for i in range(n):
        print(mas[i])
        print("\n")

def get_ferz(n):
    for i in range(n):
        if i % 2 == 0:
            mas[i][int( (n - 1)/ 2 - i / 2 )] = "██"
        else:
            mas[i][int( n  - 1 - (i - 1) / 2 )] = "██"

while True:
    print ('Enter field dimension  >> ')
    n = input()
    n = int(n)
    if n < 4:
        print('\n███████╗██████╗░██████╗░░█████╗░██████╗░██╗')
        print('██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║')
        print('█████╗░░██████╔╝██████╔╝██║░░██║██████╔╝██║')
        print('██╔══╝░░██╔══██╗██╔══██╗██║░░██║██╔══██╗╚═╝')
        print('███████╗██║░░██║██║░░██║╚█████╔╝██║░░██║██╗')
        print('╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝')
        print ('\nIt is possible to solve this problem only for n  > 3\n')
        continue
    else:
        mas = [0] * n
        for i in range(n):
            mas[i] = ["□"] * n
        #printmas()
        get_ferz(n)
        printmas()
        print('DONE!\nAction completed successfully\n')
        continue
