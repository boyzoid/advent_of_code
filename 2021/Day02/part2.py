import json
f = open( 'data.json' )
data = json.load( f )
f.close()
horizontal = 0
depth = 0
aim = 0

for step in data:
    match step[ 'direction' ]:
        case 'forward':
            horizontal += step[ 'amount' ]
            if aim > 0:
                depth += step[ 'amount' ] * aim
        case 'up':
            aim -= step[ 'amount' ]

        case 'down':
            aim += step[ 'amount' ]

print( horizontal * depth )