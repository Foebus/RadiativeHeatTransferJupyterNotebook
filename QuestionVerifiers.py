
def check_exercise_q1(q):
    correct_res = 184.6891736
    check_exercise(correct_res, q, 0.001)


def check_exercise_q2(q):
    correct_res = -184.6891736
    check_exercise(correct_res, q, 0.001)


def check_exercise(expected, got, accepted_delta):
    if abs(got-expected) <= accepted_delta:
        print("Hooray, you got it right!")
    else:
        print("Your solution is a bit too far from the right one, try again!")

