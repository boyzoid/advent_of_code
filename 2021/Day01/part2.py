import json
import array

f = open( 'data.json' )
data = json.load( f )
f.close()

myCount = 0
if len( data ) > 2:
    prevSet = data[ 0 ] + data[ 1 ] + data[ 2 ];
else:
    prevSet = 0
i = 0
while i < len( data ) - 2:
    thisSet = data [ i ] + data[ i+ 1 ] + data[ i + 2 ]
    if thisSet > prevSet:
        myCount += 1
    prevSet = thisSet
    i += 1


print( myCount )

