
def wish(func):
    def greeting():
        print('good morning')
        func()
        print('good evening')
    return greeting
    
@wish
def words():
    print('have a great day')
    
words()


