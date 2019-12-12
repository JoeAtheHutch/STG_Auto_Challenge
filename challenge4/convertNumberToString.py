import math

class ConvertNumberToString:
    
    #I don't think there is any value to this method, but I feel better having a constructor. Old Java habits
    def ConvertNumberToString(self):
        someNum = 0

    def getNumberString(self, someNum):
        if(someNum == 0):
            return 'zero'

        # I learned about dictonaries
        largeNumNames = {0: '', 3: 'thousand', 6: 'million', 9: 'billion', 12: 'trillion'}

        word = ''
        numLength = len(str(someNum))
        workNum = someNum
        
        while(numLength > 0):
            # I decided the best logic was to reduce the number to three digit segments, and work left to right.
            # Of course, this requires stripping off an amount less than three digts first, then working on three digit groups
            if(numLength % 3 != 0):
                numLength = numLength - numLength % 3
                leadNum = int(math.floor(workNum/(10**numLength)))
                workNum = workNum % 10**numLength
            else:
                numLength = numLength - 3
                leadNum = int(math.floor(workNum/(10**numLength)))
                workNum = workNum % 10**numLength
            word += self.makeItString(leadNum)
            word += largeNumNames[numLength] + ' '
        
        # since my logic involved always adding a trailing space, I strip out any extra spaces from the string before returning
        return word.strip()


    def makeItString(self, thisNum):
        numString = ''

        # And I thought, "Why use just one dictionary?"
        ones = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
        teens = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
            18: 'eighteen', 19: 'nineteen'}
        tens = {2: 'twenty', 3:'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}
        hundreds = {1: 'one hundred', 2: 'two hundred', 3: 'three hundred', 4: 'four hundred', 5: 'five hundred', 6: 'six hundred', 
            7: 'seven hundred', 8: 'eight hundred', 9: 'nine hundred'}

        
        if(thisNum >= 100):
            numString += hundreds[int(math.floor(thisNum/100))] + ' '
            thisNum = thisNum % 100
        if(thisNum > 20):
            numString += tens[int(math.floor(thisNum/10))] + ' '
            thisNum = thisNum % 10
        if(10 <= thisNum < 20):
            numString += (teens[thisNum] + ' ')
            thisNum = 0 
        if(10 > thisNum > 0):
            numString+= ones[thisNum] + ' '
            pass
        return(numString)