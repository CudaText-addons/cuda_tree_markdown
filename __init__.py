import itertools


def _is_pre(s, ch, need_space):
    if not s.startswith(ch):
        return
    r = len(list(itertools.takewhile(lambda c: ch == c, s)))
    if not need_space:
        return r
    if r < len(s) and s[r].isspace():
        return r


def is_line_ticks(s):
    return _is_pre(s, '`', False)


def is_line_head(s):
    return _is_pre(s, '#', True)


def get_headers(filename, lines):
    '''
    Generates markdown headers in format:
    line_index, header_level, header_text
    '''
    tick = False
    tick_r = 0
    for i, s in enumerate(lines):
        if not s.strip():
            continue
        r = is_line_ticks(s)
        if r:
            if tick and r == tick_r:
                tick = False
                tick_r = 0
            else:
                tick = True
                tick_r = r
            continue
        if tick:
            continue
        r = is_line_head(s)
        if r:
            yield i, r, s[r:].strip()
