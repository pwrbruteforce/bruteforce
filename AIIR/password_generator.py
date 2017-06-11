class Pass(object):
    def __init__(self, length, alphabet):
        self.alphabet = alphabet
        self.length = length

    def generate_password(self):
        password = ' ' * self.length
        for i in xrange(self.length):
            for letter in self.alphabet:
                password = list(password)
                password[i] = letter
                yield ''.join(password)
