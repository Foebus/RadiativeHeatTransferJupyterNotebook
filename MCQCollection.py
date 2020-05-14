from InteractionOwnLibrary import MCQ


def testMCQ():
    MCQ("What is your favorite color?", ["Grey", "White", "Black", "Red"], "Red")


def testBigMCQ():
    MCQ("What is The color of Napoleon's white horse?", ["Grey", "Brown"], "Grey")


def testLittleMCQ():
    MCQ("How old is Chewbaka?", ["20", "50", "75", "102", "1032", "42", "No one knows"], "No one knows")
