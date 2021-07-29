text = input('Enter the whole text: ')
replace = input('Enter the leter/word you want to replace: ')
replaceFor = input('Enter the replace value: ')

def wordReplacer(text,x,y):
    if len(x) == 1:
        if x.isupper() :
            xLower = x.lower()
            print(x)
            print(xLower)
            replacedText = text.replace(x,y)
            replacedText = replacedText.replace(xLower,y)
            return print('Your Replaced Text is: ' + replacedText)
            print(x)
            print(xUpper)
            replacedText = text.replace(x,y)
            replacedText = replacedText.replace(xUpper,y)
            return print('Your Replaced Text is: ' + replacedText)
    elif len(x) > 1 :
        return print(text.replace(x,y))

wordReplacer(text,replace,replaceFor)

