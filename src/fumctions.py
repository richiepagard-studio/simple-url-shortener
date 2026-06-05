import re
import string
import itertools
from typing import Optional

class ShortenerLink(object):
    '''
    This class is shortener your url
    '''
    def __init__(
        self,
        url: str,
        domain_name: Optional[str] = None
    ) -> None:
        self.url = url
        self.domain_name = domain_name
        self.generator = self.shortener()

    def get_domain(self):
        if self.domain_name is None:
            self.domain_name = re.findall(r'^(?:https?:\/\/)?([^\/?#]+)', string=self.url)
            return self.domain_name

    def shortener(self):
        try:
            letters = string.ascii_letters
            digits = string.digits

            length = 1
            while True:
                for i in itertools.product(letters, repeat=length):
                    prefix = ''.join(i)
                    for d in digits:
                        yield prefix + d
                length += 1

        except Exception as e:
            return f'The Exeption is {e}'

    def generate(self):
        return next(self.generator)

    def main(self):
        if self.url.lower() == 'exit':
            return None

        return f'https://pijamas.ir/{self.generate()}'

    def __repr__(self):
        return f'The url with this domain name ({self.get_domain()[0]}) has been shortenered. Your shortenered url is {self.main()}'

if __name__ == '__main__':
    obj = ShortenerLink(url='https://www.sid.ir/search/paper/requirement%20Machine%20in%20Planning%20of%20industrial%20units/fa?page=1&sort=1&ftyp=all&fgrp=all&fyrs=1379%2c1402')
    print(obj)
