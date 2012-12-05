class PriorityQueue(object):

    def __init__(self):
        self.a = []
        self.d = {}
        self.a.append("garbage")

    def insert(self, key):
        if key in self.d:
            self.d[key]["ctr"] += 1
            c_index = self.d[key]["idx"]
            self.heapify_up(c_index, key)
        else:
            self.d[key] = {}
            self.d[key]["ctr"] = 1
            counter = len(self.a)
            self.a.append(key)
            self.d[key]["idx"] = counter
            self.heapify_up(counter, key)

    def heapify_up(self, c_index, key):
        if(c_index > 1):
            p_index = self.parent(c_index)
            p_key = self.a[p_index]
            if(self.d[key]["ctr"] > self.d[p_key]["ctr"]):
                self.swap(c_index, p_index)
                self.heapify_up(p_index, p_key)

    def parent(self, c_index):
        return int(c_index) / 2

    def has_a_child(self, c_index):
        if ((c_index * 2) < len(self.a)):
            return True
        return False

    def swap(self, c_index, p_index):
        val = self.a[c_index]
        par = self.a[p_index]
        self.d[val]["idx"] = p_index
        self.d[par]["idx"] = c_index
        self.a[c_index] = self.a[p_index]
        self.a[p_index] = val

    def heapify_down(self, c_index):
        if self.has_a_child(c_index):
            curr_key = self.a[c_index]
            curr_val = self.d[curr_key]["ctr"]
            child_key = self.a[self.max_child(c_index)]
            child_val = self.d[child_key]["ctr"]
            if curr_val < child_val:
                self.swap(c_index, self.max_child(c_index))
                self.heapify_down(self.max_child(self.d[child_key]["idx"]))

    def max_child(self, c_index):
        right_child = (c_index * 2) + 1
        left_child = c_index * 2
        if(right_child >= len(self.a)):
            return left_child
        else:
            right_key = self.a[right_child]
            right_ctr = self.d[right_key]["ctr"]
            left_key = self.a[left_child]
            left_ctr = self.d[left_key]["ctr"]
            if(right_ctr > left_ctr):
                return right_child
            else:
                return left_child

    def popper(self):
        retval = self.a[1]
        self.a[1] = self.a[len(self.a) - 1]
        key = self.a[len(self.a) - 1]
        self.d[key]["idx"] = 1
        self.a.remove(self.a[len(self.a) - 1])
        self.heapify_down(1)
        return retval

    def empty(self):
        if(len(self.a) == 1):
            return True
        else:
            return False
