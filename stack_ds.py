from double_linked_list import DoubleLinkedList


class Stack:
    def __init__(self):
        self.__list = DoubleLinkedList()

    def push(self, val):
        self.__list.add(val)

    def pop(self):
        val = self.__list.back()
        self.__list.remove_last()
        return val

    def is_empty(self):
        return self.__list.size == 0

    # sob cheye uporer element return korar jonno
    def peek(self):
        return self.__list.back()

    def __len__(self):
        return self.__list.size


my_stack = Stack()
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
my_stack.push(5)
print(f"last element : ", my_stack.peek())
print(f"length : ", len(my_stack))
# print(my_stack.pop(), f"deleted element {my_stack.__len__()}: ", my_stack.pop())
print(f"deleted element : ", my_stack.pop())
print("last element : ", my_stack.peek())
print(f"after delete length : ", len(my_stack))
# my_stack.pop()
