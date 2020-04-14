
CYPHER = 'PVKQ@l>@n>kBAn=?o<pml?<AkBC<ml<@;@pC'

SIGNED = True # SWITCHER
if not SIGNED:
    print('I was corrupted... :( Help me.')

for offset in range(30):
    FLAG = ''.join([chr(ord(l) - offset + SIGNED) for l in CYPHER])
    print(f'Your flag: {FLAG}')

if SIGNED: print('Congratz!')