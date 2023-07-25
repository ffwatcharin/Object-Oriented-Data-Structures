class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def __len__(self):
        return len(self.queue)


print(" ***Cafe***")
inp = input("Log : ").split("/")

status1, status2 = Queue(), Queue()
now, aviail_1, avial_2 = 0, 0, 0
log_id, log_wait = [], []

for i in range(1, len(inp)+1):
    wait1 = 0
    entry, coffee = inp[i-1].split(",")
    entry, coffee = int(entry), int(coffee)
    log_id.append(i)

    now = entry
    if not status1:
        aviail_1 = now + wait1 + coffee
        status1.enqueue([i, aviail_1])
        log_wait.append(wait1)
    elif not status2:
        avial_2 = now + wait1 + coffee
        status2.enqueue([i, avial_2])
        log_wait.append(wait1)
    else:
        if aviail_1 <= now < avial_2:
            aviail_1 = now + wait1 + coffee
            status1.enqueue([i, aviail_1])
            log_wait.append(wait1)
        elif aviail_1 > now >= avial_2:
            avial_2 = now + wait1 + coffee
            status2.enqueue([i, avial_2])
            log_wait.append(wait1)
        elif now >= aviail_1 and now >= avial_2:
            while status1:
                dq = status1.dequeue()
                print(f"Time {dq[1]} customer {dq[0]} get coffee")
            aviail_1 = now + wait1 + coffee
            status1.enqueue([i, aviail_1])
            log_wait.append(wait1)
            while status2:
                dq = status2.dequeue()
                print(f"Time {dq[1]} customer {dq[0]} get coffee")
        else:
            if aviail_1 - now < avial_2 - now:
                wait1 = aviail_1 - now
                aviail_1 = now + wait1 + coffee
                status1.enqueue([i, aviail_1])
                log_wait.append(wait1)
            elif avial_2 - now < aviail_1 - now:
                wait1 = avial_2 - now
                avial_2 = now + wait1 + coffee
                status2.enqueue([i, avial_2])
                log_wait.append(wait1)
            else:
                if status1.__len__() > status2.__len__():
                    wait1 = avial_2 - now
                    avial_2 = now + wait1 + coffee
                    status2.enqueue([i, avial_2])
                    log_wait.append(wait1)
                else:
                    wait1 = aviail_1 - now
                    aviail_1 = now + wait1 + coffee
                    status1.enqueue([i, aviail_1])
                    log_wait.append(wait1)

remain = []
while status1:
    remain.append(status1.dequeue())
while status2:
    remain.append(status2.dequeue())


remain_sorted = sorted(remain, key=lambda x: (x[1], x[0]))
for i in remain_sorted:
    print(f"Time {i[1]} customer {i[0]} get coffee")

if max(log_wait) != 0:
    ind = log_wait.index(max(log_wait))
    print(f"The customer who waited the longest is : {log_id[ind]}\nThe customer waited for {max(log_wait)} minutes")
else:
    print("No waiting")