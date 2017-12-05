import re

import pytest


def validate_allow_anagrams(passphrase):
    passphrase = re.sub('\s+', ' ', passphrase)
    words = passphrase.split(' ')
    unique_words = set(words)
    return len(words) == len(unique_words)


def sorted_string(string):
    return ''.join(sorted(string))


def validate_forbid_anagarams(passphrase):
    passphrase = re.sub('\s+', ' ', passphrase)
    words = passphrase.split(' ')
    unique_words = set([sorted_string(word) for word in words])
    return len(words) == len(unique_words)


def count_valid_passphrases(source, validate):
    with open(source) as passphrases:
        return sum([validate(passphrase)for passphrase in passphrases])


@pytest.mark.parametrize('passphrase,is_valid', [
    ('aa bb cc dd ee', True),
    ('aa bb cc dd aa', False),
    ('aa bb cc dd aaa', True),
])
def test_validate(passphrase, is_valid):
    assert is_valid == validate_allow_anagrams(passphrase)


def main():
    print('Valid passphrases, allowing anagrams:', count_valid_passphrases('input', validate_allow_anagrams))
    print('Valid passphrases, forbidding anagrams:', count_valid_passphrases('input', validate_forbid_anagarams))


if __name__ == '__main__':
    main()