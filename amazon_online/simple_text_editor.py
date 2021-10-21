class TextEditor:
    def __init__(self):
        self.APPEND, self.DELETE = 1, 2
        self.last_operations = [] #stack 
        self.content = [] 

    def append_to_content(self, text: str, reverse=False):
        for char in text:
            self.content.append(char)
        if not reverse:
            self.last_operations.append((self.DELETE, len(text)))
        
    def delete(self, k: int, reverse=False):
        deleted = []
        for i in range(k):
            if len(self.content) == 0: return
            char = self.content.pop()
            deleted.append(char)
        if not reverse:
            self.last_operations.append((self.APPEND, deleted[::-1]))
        
    def print_content(self, k: int):
        print(self.content[k-1])

    def undo(self):
        if len(self.last_operations) == 0: 
            return
        op, op_input = self.last_operations.pop()
        if op == self.APPEND: 
            self.append_to_content(op_input, reverse=True)
        elif op == self.DELETE: 
            self.delete(op_input, reverse=True)

#### GETTING INPUT ####
num_operations = int(input())

operations = []
for i in range(num_operations):
    op = input()
    op_id, op_input = int(op[0]), None
    if len(op) > 1:
        _ , op_input = op.split(" ")
    operations.append((op_id, op_input))

#### PROCESSING INPUT ####
my_text_editor = TextEditor()

APPEND, DELETE, PRINT, UNDO = 1,2,3,4
for op_id, op_input in operations:
    if op_id == APPEND:
        my_text_editor.append_to_content(op_input)
    elif op_id == DELETE:
        my_text_editor.delete(int(op_input))
    elif op_id == PRINT:
        my_text_editor.print_content(int(op_input))
    elif op_id == UNDO:
        my_text_editor.undo()