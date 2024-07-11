"""
Stack operations using an array.
"""

stack = []  #: List to represent the stack
top = -1  #: Index to represent the top of the stack
n = 0  #: Size of the stack

def push():  #: Function to push an element into the stack
    """
    Pushes an integer value onto the stack.

    Parameters:
    None

    Returns:
    None
    """
    global top, n  #: Update the global variables
    if top >= n - 1:  #: Check if the stack is full
        print("\n\tSTACK is overflow")  #: Print stack overflow message
    else:
        x = int(input("Enter a value to be pushed:"))  #: Get user input
        top += 1  #: Update the top index
        stack.append(x)  #: Append the value to the stack


def pop():  #: Function to pop an element from the stack
    """
    Pops an element from the stack.

    Parameters:
    None

    Returns:
    None
    """
    global top  #: Update the global variable
    if top < 0:  #: Check if the stack is empty
        print("\n\tStack is underflow")  #: Print stack underflow message
    else:
        print(f"\n\tThe popped element is {stack[top]}")  #: Print the popped element
        stack.pop()  #: Remove the top element from the stack
        top -= 1  #: Update the top index


def display():  #: Function to display the elements in the stack
    """
    Displays the elements in the stack.

    Parameters:
    None

    Returns:
    None
    """
    global top  #: Update the global variable
    if top >= 0:  #: Check if the stack is not empty
        print("\n The elements in STACK \n")  #: Print stack elements header
        for i in range(top, -1, -1):  #: Iterate through the stack in reverse order
            print(stack[i])  #: Print each element
        print("\n Press Next Choice")  #: Print next choice message
    else:
        print("\n The STACK is empty")  #: Print empty stack message


def main():  #: Function to run the stack operations
    """
    Runs the stack operations using an array.

    Parameters:
    None

    Returns:
    None
    """
    global n  #: Update the global variable
    print("\n Enter the size of STACK[MAX=100]:")  #: Get user input for stack size
    n = int(input())  #: Set the stack size
    print("\n\t STACK OPERATIONS USING ARRAY")  #: Print stack operations header
    print("\n\t--------------------------------")  #: Print stack operations separator
    print("\n\t 1.PUSH\n\t 2.POP\n\t 3.DISPLAY\n\t 4.EXIT")  #: Print stack operation choices
    choice = 0  #: Initialize the choice variable
    while choice != 4:  #: Run the stack operations loop
        print("\n Enter the Choice:")  #: Prompt user for choice
        choice = int(input())  #: Get user input for choice
        match choice:  #: Use a match statement to handle each choice
            case 1:  #: If choice is 1, call the push function
                push()
            case 2:  #: If choice is 2, call the pop function
                pop()
            case 3:  #: If choice is 3, call the display function
                display()
            case 4:  #: If choice is 4, print the exit point message
                print("\n\t EXIT POINT ")
            case _:  #: If choice is not 1, 2, 3, or 4, print an error message
                print("\n\t Please Enter a Valid Choice(1/2/3/4)")


if __name__ == "__main__":  #: Run the main function if this script is executed directly
    main()