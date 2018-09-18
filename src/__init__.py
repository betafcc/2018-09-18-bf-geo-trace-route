import io
import re
from collections import deque
from itertools import groupby, islice
from operator import itemgetter
from subprocess import Popen, PIPE, check_output


IP_LINE_PATTERN = re.compile(r"\s*\d+\s+(\d+\.\d+\.\d+\.\d+)")


def shell(cmd, *args, **kwargs):
    return io.TextIOWrapper(Popen(cmd, shell=True, stdout=PIPE).stdout, *args, **kwargs)


def traceroute(host):
    _ = shell(f"traceroute -n {host}")
    _ = map(lambda l: IP_LINE_PATTERN.findall(l.strip()), _)
    _ = filter(len, _)
    _ = map(lambda l: l[0], _)

    yield from _


def my_ip():
    return (
        check_output("dig +short myip.opendns.com @resolver1.opendns.com", shell=True)
        .strip()
        .decode("utf-8")
    )


def unique_justseen(it, key=None):
    return map(next, map(itemgetter(1), groupby(it, key)))


def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))


def iter_deque(it, size=2):
    it = iter(it)
    d = deque(take(size, it), maxlen=size)
    yield list(d)
    for el in it:
        d.append(el)
        yield list(d)
