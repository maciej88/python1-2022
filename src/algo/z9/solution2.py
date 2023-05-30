"""
Semantic versioning
https://devopedia.org/images/article/279/7179.1593248779.png

{Major}.{Minor}.{Patch}

np.

'1.3.6' oznacza major=1, minor=3, path=6


"""


def get_latest(versions: list[str]) -> str:
    max_version = versions[0]
    for version in versions:
        if version > max_version:
            max_version = version
    return max_version



def next_version(version: str, level: int) -> str:
    x = version.split('.')
    i = ([int(a) for a in x])
    a, b, c = i[0], i[1], i[2]
    if level == 0:
        return f"{a+1}.0.0"
    elif level == 1:
        return f"{a}.{b+1}.0"
    elif level == 2:
        return f"{a}.{b}.{c+1}"
    else:
        return False
