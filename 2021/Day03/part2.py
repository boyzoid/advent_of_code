# A friend said it felt like cheating when I put the data into a JSON object, so I am stopping that....for now

def getRating( data, bitPosition, mostLeast ):
    bitOne = []
    bitZero = []
    newData = []
    for item in data:
        if item[ bitPosition : bitPosition+1 ] == '1':
            bitOne.append( item )
        else:
            bitZero.append( item )

    match mostLeast:
        case 'most':
            if len( bitOne ) >= len( bitZero ):
                newData = bitOne
            else:
                newData = bitZero

        case 'least':
            if len( bitZero ) <= len( bitOne ):
                newData = bitZero
            else:
                newData = bitOne
    if len( newData ) > 1:
        newData = getRating( newData, bitPosition+1, mostLeast )
    return newData

file = open(r"data.txt","r")

data = []
for line in file:
	data.append( line.strip() )
file.close()

oxygenRating = getRating( data, 0, 'most' )[ 0 ]
co2Rating = getRating( data, 0, 'least' )[ 0 ]
oxygenRatingDec = int( oxygenRating, 2 )
co2RatingDec = int( co2Rating, 2 )

print( oxygenRatingDec * co2RatingDec )