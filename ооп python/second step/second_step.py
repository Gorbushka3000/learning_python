class Verification:

    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.__lenPassword()

    def __lenPassword(self):
        if len(self.password) < 8:
            raise ValueError ('Слабый пароль')
    
    def save(self):
        with open('users.txt', 'a') as r:
            r.write(f'{self.login, self.password}'+'\n')
            
if __name__ == '__main__':
    x = Verification('gleb', '1234567890')
    x.save