#this is the shell-bang line
print('Hello World from main')

def hi():
    print('Hello, World! - from definition')

class HelloLanguages():
    def __init__(self, *args):
        super(HelloLanguages, self).__init__(*args)
        
    def printHello(self, language):
        print('Hello, {}! - from class method'.format(language))
        
        print(f'Hello, {language}! - from class method')
        
        
        print('Hello, %s! - from class method' % (language))
    
    def say_hello(recipient):
        return('Hello, {}!'.format(recipient))
  
if __name__ == '__main__':
    hi()
    new_hello = HelloLanguages()
    #__init__ should set intital state.
