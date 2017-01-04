import random as Austinness

starts = ("So, ", "Basically, ", "So, basically, ", "")
ends = (", yeah. ", ", right? ", ", so, yeah! ", ". ")
interns = ("er- ", "um- ", "basically, ")
## A list of verbs that can have "basically, " after them. 
verbs = ["is", "am", "are", "has", "wants", "were"]
punct = (".", "?", "!")

umChance = 4

text = input("Austin Translate!\nWrite your text here:\n")
while text != "":

    text = text.lower()

    for i in range(len(text)):
        if (text[0] == "i" and i == 0) or text[i-1:i+1] == " i ":
            text = text[:i] + "I" + text[i+1:]
    
    if text[-1] != ".":
        text += "."

    wordk = text.split()

    for word in range(len(wordk)):
        try:
            while wordk[word][-1] in punct:
                wordk.insert(word+1, wordk[word][-1])
                wordk[word] = wordk[word][0:-1]
        except IndexError:
            pass

    randomness = list(range(1, len(wordk)-1, 1))

    for i in randomness:
        i = i % umChance

    text = ""

    for i in range(len(wordk)):
        penetration = True
        try:
            chance = Austinness.choice(randomness)
        except IndexError:
            chance = 3
        if chance == 1:
            insertion = True
        else:
            insertion = False
            
        try:
            if (wordk[i-1] == "." and i != 0) or i == 0:
                if chance == 2 and Austinness.randint(0, 3) == 1:
                    text += Austinness.choice(("So, basically, umm... ", "So, basically, er... "))
                start = Austinness.choice(starts)
                if starts != "":
                    text += start
#                    wordk[i] = wordk[i].lower()
                if text == "" or text[-2] in punct:
                    text += wordk[i][0].upper()
                    text += wordk[i][1:]
#                if wordk[i] == "i":
#                    wordk[i] = "I"
                else:
                    text += wordk[i]
                if not wordk[i+1] in punct:
                    text += " "

            elif wordk[i] == "." or wordk[i] == wordk[-1]:
                text += Austinness.choice(ends)
                penetration = False
            elif not wordk[i+1] in punct:
                text += wordk[i] + " "
            elif wordk[i+1] in punct:
                text += wordk[i]
                penetration = False
        except IndexError:
            text += wordk[i]
        if insertion and penetration:
            if not wordk[i-1] in verbs:
                text += Austinness.choice(interns[:1])
            else:
                text += Austinness.choice(interns)
    print(text)
    text = input()
