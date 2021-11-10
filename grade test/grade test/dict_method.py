import time, logging
import loggingpackage.generic_logger as cl
final = 0

class dict_method():

    log = cl.customLogger(logging.DEBUG)

    def method1(self):
   

        self.log.debug('%s' % final)
       
start = time.time()        

def let_rng(dictionary, grade, rng):
    for i in rng:
        dictionary[i] = grade
"""
the above function takes args dictionary, grade and rng. Later we will make rng an actual range. All it does apply a given string (grade)
and append it into a dictionary. So for each i in a given range: append (key i) with (value 'grade'). We make i the key as a dictionary cannot
have duplicate keys
"""
grads = {'john': 95, 'jill': 85, 'james': 75, 'ken': 65}

test = (88)
letgrade = {}
let_rng(letgrade, 'A', range(90,100))
let_rng(letgrade, 'B', range(80,89))
let_rng(letgrade, 'C', range(70,79))
let_rng(letgrade, 'F', range(0,69))

"""
Essentially the above block of code creates a giant dictionary where ever number from 0-100 has a key of the correct grade string
Which is kind of insane
{90: 'A', 91: 'A', 92: 'A', 93: 'A'........0: 'F'}
"""


for name,num in grads.items():
    L = (letgrade[num])
    print("%s: %s" % (name, L))    

end = time.time()
final = (end - start)

demo = dict_method()
demo.method1()
