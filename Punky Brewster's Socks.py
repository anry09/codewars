def get_socks(name, socks):
    if name == 'Punky':
        for s in socks:
            for y in socks:
                if s != y:
                    return [s, y]
        return []
    else:
        for s in socks:
            if socks.count(s) > 1:
                return [s, s]
        return []