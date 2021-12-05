# A friend said it felt like cheating when I put the data into a JSON object, so I am stopping that....for now

file = open(r"data.txt","r")

data = []
gamma = ""
epsilon = ""
for line in file:
	data.append( line.strip() )
file.close()

itemCount = round( len( data ) / 2 )
bitLen = len( data[ 0 ] )
bitCount = []
for item in data:
    bit = 0
    while bit < bitLen:
        if len( bitCount ) == bit:
            bitCount.append( 0 )
        bitCount[ bit ] += int( item[ bit : bit + 1 ] )
        bit += 1

for counter in bitCount:
    gamma += ( "1" if counter >= itemCount else "0" )
    epsilon += ( "1" if counter < itemCount else "0" )
    

gamma = int( gamma, 2 );
epsilon = int( epsilon, 2 )
print( gamma * epsilon )
