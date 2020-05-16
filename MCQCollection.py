from InteractionOwnLibrary import MCQ


def testMCQ():
    MCQ("What is your favorite color?", ["Grey", "White", "Black", "Red"], "Red")


def testBigMCQ():
    MCQ("What is The color of Napoleon's white horse?", ["Grey", "Brown"], "Grey")


def testLittleMCQ():
    MCQ("How old is Chewbaka?", ["20", "50", "75", "102", "1032", "42", "No one knows"], "No one knows")

def ViewFactorMCQ11():
    MCQ("What is the F1_1?", ["0","0.25","0.5","0.75","1"],"0")
    
def ViewFactorMCQ12():
    MCQ("What is the F1_2?", ["0","0.25","0.5","0.75","1"],"1")
    
def ViewFactorMCQ21():
    MCQ("What is the F2_1?", ["0","0.25","0.5","0.75","1"],"0.5")
    
def ViewFactorMCQ22():
    MCQ("What is the F2_2?", ["0","0.25","0.5","0.75","1"],"0.5")