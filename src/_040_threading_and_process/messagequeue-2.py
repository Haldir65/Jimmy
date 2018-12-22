import threading
import queue

## credit
##  https://stackoverflow.com/questions/43422071/how-to-put-an-item-back-to-a-queue-queue
def worker(in_q, out_q):
    while True:
        try:
            task, data = in_q.get()
            print('worker', task, data)
            if task == "done":
                return
            elif task == "pass this":
                out_q.put(("pass", data))
            else:
                out_q.put(("fail", data))
        except Exception as e:
            print('worker exception', e)
            out_q.put("exception", data)

in_que = queue.Queue()
out_que = queue.Queue()

work_thread = threading.Thread(target=worker, args=(in_que, out_que))
work_thread.start()

# lets make every other task a fail
in_que.put(('pass this', 0))
in_que.put(('fail this', 1))
in_que.put(('pass this', 2))
in_que.put(('fail this', 3))
in_que.put(('pass this', 4))
in_que.put(('fail this', 5))

pending_tasks = 6

while pending_tasks:
    status, data = out_que.get()
    if status == "pass":
        pending_tasks -= 1
    else:
        # make failing tast pass
        in_que.put(('pass this', data))

in_que.put(("done", None))
work_thread.join()
print('done')