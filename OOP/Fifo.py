class Queue:
    def __init__(self, queue_list):
        self.queue_list = queue_list

    def show (self):
        print(queue_list)

    def put (self, elem):
        self.queue_list.append(elem)
        print ((elem) "dodany do kolejki")
    def pop (self):
        list.pop()

    def empty (self):
        return len(self.queue_list) == 0
