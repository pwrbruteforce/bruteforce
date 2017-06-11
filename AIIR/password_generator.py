import sys
import hashlib

class BruteForce(object):
    """Container contains functions for finding hash matching with given hash."""

    def __init__(self, hash, length, first_letters, alphabet):
        self.hash = hash
        self.length = length
        self.first_letters = first_letters
        self.alphabet = alphabet

    def _generate_letter(self, alphabet):
        """
        This genarator creates letters from alphabet sequence.

        :param str alphabet:

        :rtype: str
        :return: letters from alphabet
        """
        for char in alphabet:
            yield char

    def _generate_password(self, length, alphabet, first_letters):
        """
        This generator creates full password from alphabet set.

        :param int length:
        :param str alphabet:
        :param str first_letters:

        :rtype: str
        :return: passwords
        """
        if length == 1:
            for letter in self._generate_letter(first_letters):
                yield letter
        else:
            for sub_password in self._generate_password(length - 1, alphabet, first_letters):
                for letter in self._generate_letter(alphabet):
                    yield sub_password + letter

    def _MD5_hash(self,  h_str ):
        md5h = hashlib.sha1()
        md5h.update(h_str.encode('utf-8'))
        return md5h.hexdigest()

    def password(self):
        """Function returning password for searched hash, if doesnt found returns -1."""
        for assumed_password in self._generate_password(self.length, self.alphabet, self.first_letters):
            assumed_hash = self._MD5_hash(assumed_password)
            if assumed_hash == self.hash:
                return assumed_password
        return -1


