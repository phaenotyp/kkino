class Movie(object):
    def __init__(self):
        self.s = []

def splitpair(pair): 
    kv = pair.split('=') 
    if len(kv)<2: kv.append('')
    return (kv[0], kv[1]) 

def metropolis(str):
    str = str.decode("iso-8859-1")
    movies = []
    parts = ( 'name', 'time1', 'time2', 'info1', 'info2' )
    lastnumber = ''
    m = None
    # there are occurances of equal-signs(=) in the string that are not key/value delimiters.
    # those have to be replaced
    str = '->'.join(str.split('=>'))
    #print str, "\n", "\n"

    for pair in str.split('&'): # str.split('&'):
        val = False
        try: 
            (key, val) = splitpair(pair)
        except ValueError:
            print 'Err: %s/%s' % (key,val)
        if val:
            if key == 'tabelle0':
                pass

            if key.startswith('atz'):
                part = parts[int(key.split('c')[1])]
                number = int(key.split('c')[0][3:])
                if lastnumber != number:
                   if m: movies.append(m) 
                   m = Movie()  
                   lastnumber=number
                #print number,' ' ,part, ' ', val 
                # TODO regex
                if part == 'name': 
                    m.name = val
                elif part.startswith('time'): 
                    m.s.append(val) 
                elif part in ['info2','info2']:
                    pass
                    # TODO: remove or add showing depending on val
                   # TODO: send mail
    return [ m for m in movies ] 
