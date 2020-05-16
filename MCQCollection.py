from InteractionOwnLibrary import MCQ


def testMCQ():
    MCQ("What is your favorite color?", ["Grey", "White", "Black", "Red"], "Red")


def testBigMCQ():
    MCQ("What is The color of Napoleon's white horse?", ["Grey", "Brown"], "Grey")


def testLittleMCQ():
    MCQ("How old is Chewbaka?", ["20", "50", "75", "102", "1032", "42", "No one knows"], "No one knows")


def ViewFactorMCQ11():
    MCQ("What is the F1_1?", ["0", "0.25", "0.5", "0.75", "1"], "0")


def ViewFactorMCQ12():
    MCQ("What is the F1_2?", ["0", "0.25", "0.5", "0.75", "1"], "1")


def ViewFactorMCQ21():
    MCQ("What is the F2_1?", ["0", "0.25", "0.5", "0.75", "1"], "0.5")


def ViewFactorMCQ22():
    MCQ("What is the F2_2?", ["0", "0.25", "0.5", "0.75", "1"], "0.5", """
    Explanation:

$$F_{1-1}=0, F_{1-2}=1$$ Because the energy leaving the surface 1 can be totally absorbed by the surface 2.

$$F_{2-1}=\\frac{A_1}{A_2}$$ due to the reciprocity property. $$F_{2-2}=1-\\frac{A_1}{A_2}$$ due to the closeness property.

""")
