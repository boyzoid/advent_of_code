import json
f = open( 'data.json' )
data = json.load( f )
f.close()

myCount = 0
prevDepth = data[ 0 ]
for depth in data:
    if depth > prevDepth:
        myCount += 1
    prevDepth = depth

print( myCount )

