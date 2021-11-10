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

letters = {'A': 95, 'B':85, 'C': 75, 'F': 65, 'A+': 105}

for name,num in grads.items():  #for each letter grade per person
    
    for letter, value in letters.items(): # for each number per grade
        f = num - value
        if f in range(-5, 5):           
            print("%s: %s" % (name, letter))
        if f not in range(-5,5):
            print("fail")
        
'''
end = time.time()
final = (end - start)

demo = function_method()
demo.method1()
'''
