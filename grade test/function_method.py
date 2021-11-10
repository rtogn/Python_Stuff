import time, logging
import loggingpackage.generic_logger as cl
final = 0
'''
class function_method():

    log = cl.customLogger(logging.DEBUG)

    def method1(self):
   

        self.log.debug('%s' % final)
   '''    


grads = {'john': 99, 'jill': 80, 'james': 72, 'ken': 50}

letters = {'A': 95, 'B':85, 'C': 75, 'F': 65}

for name,num in grads.items():
    
    f = min(letters.values(), key=lambda x:abs(x-num))

    for g, n in letters.items():
        if f == n:
            print("%s: %s" % (name, g))
        
'''
end = time.time()
final = (end - start)

demo = function_method()
demo.method1()
'''
