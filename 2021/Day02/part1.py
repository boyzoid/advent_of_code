import json
f = open( 'data.json' )
data = json.load( f )
f.close()
horizontal = 0
depth = 0

for step in data:
    match step[ 'direction' ]:
        case 'forward':
            horizontal += step[ 'amount' ]
        case 'up':
            depth -= step[ 'amount' ]
        case 'down':
            depth += step[ 'amount' ]

print( horizontal * depth )