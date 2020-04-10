CYPHER = 'PVKQ@l>@n>kBAn=?o<pml?<AkBC<ml<@;@pC'

SIGNED = False # SWITCHER
if not SIGNED:
    print('I was corrupted... :( Help me.')

FLAG = ''.join([chr(ord(l) - 9 - SIGNED) for l in CYPHER])
print(f'Your flag: {FLAG}')

if SIGNED: print('Congratz!')
