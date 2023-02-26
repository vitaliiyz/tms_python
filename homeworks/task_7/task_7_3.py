from string import ascii_lowercase


class Cipher:
    def __init__(self, keyword):
        self._keyword = keyword
        self._alphabet = list(ascii_lowercase)

    @property
    def keyword(self):
        return self._keyword

    @property
    def alphabet(self):
        return self._alphabet

    def generate_new_alphabet(self):
        new_alphabet = self.alphabet.copy()

        for i in self.keyword:
            new_alphabet.remove(i)

        return list(self.keyword) + new_alphabet

    def encode(self, text: str):
        generated_alphabet = self.generate_new_alphabet()
        encoded_list = []

        for letter in text:
            if letter in self.alphabet:
                encoded_list.append(generated_alphabet[self.alphabet.index(letter)])
            elif letter.lower() in self.alphabet:
                encoded_list.append(generated_alphabet[self.alphabet.index(letter.lower())].upper())
            else:
                encoded_list.append(letter)

        return ''.join(encoded_list)

    def decode(self, text: str):
        generated_alphabet = self.generate_new_alphabet()
        decoded_list = []

        for letter in text:
            if letter in generated_alphabet:
                decoded_list.append(self.alphabet[generated_alphabet.index(letter)])
            elif letter.lower() in generated_alphabet:
                decoded_list.append(self.alphabet[generated_alphabet.index(letter.lower())].upper())
            else:
                decoded_list.append(letter)

        return ''.join(decoded_list)


cipher = Cipher("crypto")
print(cipher.encode("Hello world"))
print(cipher.decode("Fjedhc dn atidsn"))
