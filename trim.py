#def trim(s):
#    while s != '':
#        if s[0] == ' ':
#            s = s[1:]
#        else:
#            break
#    while s != '':
#        if s[-1] == ' ':
#            s = s[:-1]
#        else:
#            break
#    return s
def trim(s):
    while (s != '') & (s[0] == ' '):
        s = s[1:]
    while (s != '') & (s[-1] == ' '):
        s = s[:-1]
    return s
