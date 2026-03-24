#This program will print different shapes based on user input. The user can choose to print a triangle, square, parallelogram, or rhombus
# by entering the shape name and the size of the shape. 
# The functions for each shape are defined separately and called in the main function based on user input.


#All the functions can be defined outside the main function, and they can be called inside the main function
#All of them can be in sepearate python files and imported in the main file, but for simplicity we are keeping them in the same file.

def triangle(n):                           
    for i in range(n):      
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))   #here '*' is a string that is been concatenated.
        
def square(n):
    for i in range(n): 
        print('* ' * n)
    
def parellelogram(n):
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * n)
        
def rhombus(n):
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))   #For upper triangle
    for i in range(n - 2, -1, -1):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))   #For lower triangle
        
        
def main():
    is_running = True
    while is_running:            #Loop untill the user enters "f" to exit
    N = int(input("Enter the size of the shapes: "))
    value = input("Enter the shape you want to print (triangle/square/parallelogram/rhombus): or (f) to exit ").lower()
    if value == "triangle" or value == "square" or value == "parallelogram" or value == "rhombus":
        if value == "triangle":
            triangle(N)
        elif value == "square":
            square(N)
        elif value == "parallelogram":
            parellelogram(N)
        elif value == "rhombus":
            rhombus(N)
    else:
        if value == "f":
            is_running = false
        else:
            print("Invalid shape. Please choose triangle, square, parallelogram, or rhombus.")   
    
if __name__ == "__main__":    #There must be a main function to run the code, otherwise it will not execute when imported as a module.
    main()
