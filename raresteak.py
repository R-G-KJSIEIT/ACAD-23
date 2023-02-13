class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def search(self, item):
        return item in self.items


s = Stack()

while True:
    print("Enter 1 to push an element into the stack")
    print("Enter 2 to pop an element from the stack")
    print("Enter 3 to peek at the top element of the stack")
    print("Enter 4 to search for an element in the stack")
    print("Enter 5 to quit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        item = int(input("Enter the element to push: "))
        s.push(item)
    elif choice == 2:
        if s.is_empty():
            print("The stack is empty.")
        else:
            print("Popped element: ", s.pop())
    elif choice == 3:
        if s.is_empty():
            print("The stack is empty.")
        else:
            print("Top element: ", s.peek())
    elif choice == 4:
        item = int(input("Enter the element to search: "))
        result = s.search(item)
        if result:
            print("Element is present in the stack.")
        else:
            print("Element is not present in the stack.")
    elif choice == 5:
        break