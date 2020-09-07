from random import uniform
from math import exp

mapper = ["rock", "scissor", "paper"]


def generate_opponent_policy(difficulty='easy'):
    ret = {}
    var = 0.5
    if difficulty == 'easy':
        logit = [uniform(-var, var), uniform(-var, var), uniform(-var, var)]
        logit_exp = [exp(x) for x in logit]
        for x, y in ((x, y) for x in mapper for y in mapper):
            ret[x, y] = {
                "rock": logit_exp[0] / sum(logit_exp),
                "scissor": logit_exp[1] / sum(logit_exp),
                "paper": logit_exp[2] / sum(logit_exp)}
    else:
        for x, y in ((x, y) for x in mapper for y in mapper):
            logit = [uniform(-var, var), uniform(-var, var), uniform(-var, var)]
            logit_exp = [exp(x) for x in logit]
            ret[x, y] = {
                "rock": logit_exp[0] / sum(logit_exp),
                "scissor": logit_exp[1] / sum(logit_exp),
                "paper": logit_exp[2] / sum(logit_exp)}
    return ret


def sample(p):
    """sample one element from the probability distribution.

    Parameters
    ----------
    p : list of floats.
        probability of drawing rock, proability of drawing scissor, probability of drawing paper
    Return
    ----------
    string
        chosen form(rock, scissor, paper)
    """
    r = 0
    q = []
    for x in p:
        r += p[x]
        q.append(r)

    v = uniform(0, 1)
    for i in range(3):
        if v <= q[i]:
            return mapper[i]
    return mapper[2]


def evalute_rsp(form_of_a, form_of_b):
    """
        given two forms, return result of the game.

    Parameters
    ----------
    form_of_a : string
        one of "rock", "scissor", "paper", which the player a drawed
    form_of_b : string
        one of "rock", "scissor", "paper", which the player b drawed
    Returns
    -------
    int
        1 if player a wins,
        0 if draws,
        and -1 if player b wins
    """
    form = {('rock', 'rock'): 0,
            ('rock', 'scissor'):1,
            ('rock', 'paper'): -1,
            ('scissor', 'rock'): -1,
            ('scissor', 'scissor'): 0,
            ('scissor', 'paper'): 1,
            ('paper', 'rock'): 1,
            ('paper', 'scissor'): -1,
            ('paper', 'paper'): 0}
    
    return form[(form_of_a, form_of_b)]


def generate_policy_exploration(my_history, opponent_history,
                                my_form_last_time, opponent_form_last_time):
    return {"rock": 0.333,
            "scissor": 0.333,
            "paper": 0.334}


def generate_policy_exploitation(my_history, opponent_history,
                                 my_form_last_time, opponent_form_last_time):
    """
        You must fill here
    """
    if difficulty == 'easy':
        historys = []
        historys.append(opponent_history.count('rock'))
        historys.append(opponent_history.count('scissor'))
        historys.append(opponent_history.count('paper'))
        ind = historys.index(max(historys))
        if ind == 0:
            return {"rock": 0,
            "scissor": 0,
            "paper": 1}
        if ind == 1:
            return {"rock": 1,
            "scissor": 0,
            "paper": 0}
        if ind ==2:
            return {"rock": 0,
            "scissor": 1,
            "paper": 0}

    else:
        hist = {('rock', 'rock'): {'rock' : 0, 'scissor': 0, 'paper' : 0},
            ('rock', 'scissor'):{'rock' : 0, 'scissor': 0, 'paper' : 0},
            ('rock', 'paper'): {'rock' : 0, 'scissor': 0, 'paper' : 0},
            ('scissor', 'rock'): {'rock' : 0, 'scissor': 0, 'paper' : 0},
            ('scissor', 'scissor'): {'rock' : 0, 'scissor': 0, 'paper' : 0},
            ('scissor', 'paper'): {'rock' : 0, 'scissor': 0, 'paper' : 0},
            ('paper', 'rock'): {'rock' : 0, 'scissor': 0, 'paper' : 0},
            ('paper', 'scissor'): {'rock' : 0, 'scissor': 0, 'paper' : 0},
            ('paper', 'paper'): {'rock' : 0, 'scissor': 0, 'paper' : 0}
            }
        for opponent_last, my_last,opponent_curr in zip(opponent_history,my_history,opponent_history[1:]):
            hist[(my_last,opponent_last)][opponent_curr] += 1

        list1 = list(hist[(my_form_last_time, opponent_form_last_time)].values())
        dex = list1.index(max(list1))
        if dex == 0:
            return {"rock": 0,
            "scissor": 0,
            "paper": 1}
        if dex == 1:
            return {"rock": 1,
            "scissor": 0,
            "paper": 0}
        if dex ==2:
            return {"rock": 0,
            "scissor": 1,
            "paper": 0}



def run(difficulty='easy'):
    """

    Parameters
    ----------
    Return
    ----------
    reward

    """
    opponent_policy = generate_opponent_policy(difficulty=difficulty)
    result_sum = 0
    statistics = {
        "opponent_history": [],
        "my_history": [],
        "my_form_last_time": "rock",
        "opponent_form_last_time": "rock"}

    # Exploration Phase
    for i in range(1000):
        my_policy = generate_policy_exploration(**statistics)
        my_action = sample(my_policy)
        opponent_action = sample(opponent_policy[(statistics['my_form_last_time'], statistics['opponent_form_last_time'])])
        result = evalute_rsp(my_action, opponent_action)
        statistics['my_history'].append(my_action)
        statistics['opponent_history'].append(opponent_action)
        statistics['my_form_last_time'] = my_action
        statistics['opponent_form_last_time'] = opponent_action

    # Exploitation Phase
    statistics['my_form_last_time'] = 'rock'
    statistics['opponent_form_last_time'] = 'rock'
    for i in range(1000):
        my_policy = generate_policy_exploitation(**statistics)
        my_action = sample(my_policy)
        opponent_action = sample(opponent_policy[(statistics['my_form_last_time'], statistics['opponent_form_last_time'])])
        result = evalute_rsp(my_action, opponent_action)
        result_sum += result
        statistics['my_form_last_time'] = my_action
        statistics['opponent_form_last_time'] = opponent_action
    return result_sum


if __name__ == "__main__":
    cnt = 10
    for difficulty in ("easy", "hard"):
        ret = []
        for i in range(cnt):
            ret.append(run(difficulty=difficulty))
        print("[%s]\taverage game results: %0.2f" % (difficulty, sum(ret) / cnt))
        print("result:", ret, '\n')
