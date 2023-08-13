class Queue:
    def __init__(self):
        self.queue = []

    def push(self,data):
        self.queue.append(data)

    def pop(self):
        return self.queue.pop(0)

    def front(self):
        return self.queue[0]
    
    def size(self):
        return len(self.queue)

    def isEmpty(self):
        if self.queue:
            return False
        else:
            return True
        
    def __str__(self):
        return "[" + ", ".join(str(i) for i in self.queue) + "]"
    
print(" ***Cafe***")
cafe_queue = input("Log : ").split("/")

customers = [[int(x) for x in i.split(",")] for i in cafe_queue]

queue = Queue()

for i in customers:
    queue.push(i)

# print(queue)

balista1 = []
balista2 = []

customer_wait = 0
longest_wait = 0
customer_number = 1
timer = 0

while(balista1 or balista2 or not queue.isEmpty()):
    # print(queue,end = "\n")
    # print(balista1,end = "\n")
    # print(balista2,end = "\n")
    # print(timer)
    while balista1 and balista1[0][1] == timer and balista2 and balista2[0][1] == timer:
            customer1 = balista1.pop(0)
            customer2 = balista2.pop(0)
            if customer1[2] <= customer2[2]:
                print(f"Time {timer} customer {customer1[2]} get coffee")
                print(f"Time {timer} customer {customer2[2]} get coffee")
            else:
                print(f"Time {timer} customer {customer2[2]} get coffee")
                print(f"Time {timer} customer {customer1[2]} get coffee")

    while balista1 and balista1[0][1] == timer:
        customer = balista1.pop(0)
        print(f"Time {timer} customer {customer[2]} get coffee")

    while balista2 and balista2[0][1] == timer:
        customer = balista2.pop(0)
        print(f"Time {timer} customer {customer[2]} get coffee")

    while(not queue.isEmpty() and queue.front()[0] == timer):

        if len(balista1) == 0 and not queue.isEmpty() and queue.front()[0] == timer:
            customer = queue.pop() + [customer_number]
            customer[1] = customer[1] + timer
            balista1.append(customer)
            customer_number += 1
            if balista1[0][1] == 0:
                customer = balista1.pop(0)
                print(f"Time {timer} customer {customer[2]} get coffee")
        elif len(balista2) == 0 and not queue.isEmpty() and queue.front()[0] == timer:
            customer = queue.pop() + [customer_number]
            customer[1] = customer[1] + timer
            balista2.append(customer)
            customer_number += 1
            if balista2[0][1] == 0:
                customer = balista2.pop(0)
                print(f"Time {timer} customer {customer[2]} get coffee")
        else:
            if not queue.isEmpty() and queue.front()[0] == timer:
                customer = queue.pop()
                if balista1[-1][1] - timer <= balista2[-1][1]:
                    customer = [customer[0],customer[1] + balista1[-1][1],customer_number]
                    if(customer[0] < balista1[-1][1]):
                        wait_time = balista1[-1][1] - customer[0]
                        if longest_wait < wait_time:
                            longest_wait = wait_time
                            customer_wait = customer_number
                    balista1.append(customer)
                else:
                    customer = [customer[0],customer[1] + balista2[-1][1],customer_number]
                    if(customer[0] < balista1[-1][1]):
                        if longest_wait < wait_time:
                            longest_wait = wait_time
                            customer_wait = customer_number
                    balista2.append(customer)
                customer_number += 1

    while balista1 and balista1[0][1] == timer and balista2 and balista2[0][1] == timer:
            customer1 = balista1.pop(0)
            customer2 = balista2.pop(0)
            if customer1[2] <= customer2[2]:
                print(f"Time {timer} customer {customer1[2]} get coffee")
                print(f"Time {timer} customer {customer2[2]} get coffee")
            else:
                print(f"Time {timer} customer {customer2[2]} get coffee")
                print(f"Time {timer} customer {customer1[2]} get coffee")
    
    while balista1 and balista1[0][1] == timer:
        customer = balista1.pop(0)
        print(f"Time {timer} customer {customer[2]} get coffee")

    while balista2 and balista2[0][1] == timer:
        customer = balista2.pop(0)
        print(f"Time {timer} customer {customer[2]} get coffee")
    timer += 1

if longest_wait == 0:
    print("No waiting")
else:
    print(f"The customer who waited the longest is : {customer_wait}")
    print(f"The customer waited for {longest_wait} minutes")