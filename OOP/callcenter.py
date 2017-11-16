from datetime import datetime

class Call(object):
    def __init__(self, uid, caller_name, caller_phone, caller_time, caller_reason):
        self.uid = uid
        self.caller_name = caller_name
        self.caller_phone = caller_phone
        self.caller_time = caller_time
        self.caller_reason = caller_reason

    def display_info(self):
        print("Caller ID: ", self.uid)
        print("Caller Name: ", self.caller_name)
        print("Caller Phone Number: ", self.caller_phone)
        print("Time of Call: ", self.caller_time)
        print("Reason for Call: ", self.caller_reason)
        print("")

caller1 = Call(14, "Ashwin", 3124432235, datetime.now(), "Inquiry")
caller1.display_info()

caller2 = Call(15, "Mike", 3125552246, datetime.now(), "Support")
caller2.display_info()

class CallCenter(object):
    def __init__(self):
        self.call_list = []
        self.queue_size = 0
        return self

    def add(self, call):
        self.call_list.append(call)
        self.queue_size += 1
        return self

    def remove(self, call):
        self.call_list.pop(0)
        self.queue_size -= 1
        return self

    def info(self):
        print self.call_list
        print self.queue_size
        return self

call_center = CallCenter()
call_center.add(caller1).add(caller2).info()
