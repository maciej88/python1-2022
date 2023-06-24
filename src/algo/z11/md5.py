import hashlib


def calculate_md5(string):
    md5_hash = hashlib.md5()
    md5_hash.update(string.encode('utf-8'))
    return md5_hash.hexdigest()


if __name__ == '__main__':
    my_string = "bob"
    md5_digest = calculate_md5(my_string)
    print(md5_digest)

    print(hashlib.md5("bob".encode('utf-8')).hexdigest())
