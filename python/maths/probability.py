# Random/Resevoir sampling
import random

class Rndm:
    def __init__(self):
        self.count = 0
    
    # Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.
    # O(n) - length of stream
    def getRandomFromStream(self, stream) -> int:
        r = None
        for i, element in enumerate(stream):
            if i == 0:
                r = element
            elif random.randint(1, i + 1) == 1:
                r = element
        return r

    # https://www.geeksforgeeks.org/select-a-random-number-from-stream-with-o1-space/
    def getRandom(self, x: int):
        self.count += 1
        if self.count == 1:
            return x

        num = random.randrange(self.count)
        if num == self.count - 1:
            return x
        else:
            return num

rnd = Rndm()
print(rnd.getRandomFromStream([1, 2, 3, 4, 5]))

stream = [6, 7, 8, 9, 10]
for i in range(len(stream)):
    print(rnd.getRandom(stream[i]))

# Given a function that generates perfectly random numbers between 1 and k (inclusive), where k is an input, write a function that shuffles a deck of cards represented as an array using only swaps.
CARDS = 52
def getRand(k):
    return random.randint(0, k)

def shuffle():
    cards = [i for i in range(CARDS)]

    for oldPos in cards:
        newPos = oldPos + getRand(CARDS - oldPos - 1)
        cards[newPos], cards[oldPos] = cards[oldPos], cards[newPos]
    
    return cards

print(shuffle())

