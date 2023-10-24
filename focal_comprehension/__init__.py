from otree.api import *

c = cu

class C(BaseConstants):
    NAME_IN_URL = 'focal_instructions'
    PLAYERS_PER_GROUP = None
    ECU_LABEL = 'ECUs'
    NUM_ROUNDS = 1

    QUIZ_FIEDLS = [f'quiz_{n}' for n in range(1, 11)]
    QUIZ_LABELS = [
        "The other firm in my market is the same every period.",
        "My firm must decide each period how many units to sell.",
        "Each period my firm can choose only one price.",
        "My firm can lose money during a period if my partner and I don’t choose the price wisely.",
        "The table titled “FULL PROFIT TABLE” tells me how much profit my firm will make and how much profit the other firm will make given that we choose certain prices of 21 or above.",
        "If my firm chooses a price of 21 or below, my profit will depend on the other firm's price choice.",
        "If my competitor chooses a price of 21 or below, their profit will depend on my firm’s price.",
        "My team will change every round.",
        "I will be provided with information or new instructions if my team is about to change.",
        "Refer to the full table by clicking on the link. If my firm chooses a price of 33 and the other firm chooses a price of 32, "
        "what will be my payoff?"
    ]

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):
    quiz_1 = models.BooleanField()
    quiz_1_wrong_attempts = models.IntegerField(initial=0)

    quiz_2 = models.BooleanField()
    quiz_2_wrong_attempts = models.IntegerField(initial=0)

    quiz_3 = models.BooleanField()
    quiz_3_wrong_attempts = models.IntegerField(initial=0)

    quiz_4 = models.BooleanField()
    quiz_4_wrong_attempts = models.IntegerField(initial=0)

    quiz_5 = models.BooleanField()
    quiz_5_wrong_attempts = models.IntegerField(initial=0)

    quiz_6 = models.BooleanField()
    quiz_6_wrong_attempts = models.IntegerField(initial=0)

    quiz_7 = models.BooleanField()
    quiz_7_wrong_attempts = models.IntegerField(initial=0)

    quiz_8 = models.BooleanField()
    quiz_8_wrong_attempts = models.IntegerField(initial=0)

    quiz_9 = models.BooleanField()
    quiz_9_wrong_attempts = models.IntegerField(initial=0)

    quiz_10 = models.IntegerField()
    quiz_10_wrong_attempts = models.IntegerField(initial=0)

# PAGES
class Comprehension(Page):
    form_model = 'player'
    form_fields = C.QUIZ_FIEDLS

    @staticmethod
    def vars_for_template(player: Player):
        labels = C.QUIZ_LABELS
        return dict(
            fields=list(zip(C.QUIZ_FIEDLS, labels))
        )

    @staticmethod
    def error_message(player: Player, values):
        solutions = dict(
            quiz_1=(True, 'Your firm will be competing with the same firm in every period.'),
            quiz_2=(False, 'The computer automatically decides how many units to sell in a way that you do not lose money.'),
            quiz_3=(True, 'You can choose one price for your firm in each period.'),
            quiz_4=(False, 'The computer automatically chooses the quantity your firm sells to the computerized buyers and will not '
                           'allow purchase in which your firm loses money.'),
            quiz_5=(True, "Each cell in the table contains my firm's potential profit and (after the comma) the other firm’s potential profit."),
            quiz_6=(False, "If my firm chooses a price of 21 or below, my firm's profit will not depend on the other firm’s price choice."),
            quiz_7=(False, "If my competitor chooses a price of 21 or below, their profit will not depend on my firm's price."),
            quiz_8=(False, "Your team will not change every round."),
            quiz_9=(True, 'If your team is about to change, you will be informed beforehand.'),
            quiz_10 = (0, "Your payoff will be 0 and your competitor's payoff will be 50."),

        )

        error_msgs = {
            k: solutions[k][1] for k, v in values.items() if v != solutions[k][0]
        }

        for k in error_msgs.keys():
            num = getattr(player, f'{k}_wrong_attempts')
            setattr(player, f'{k}_wrong_attempts', num + 1)

        return error_msgs


class EndComprehension(Page):
    pass

class Instructions(Page):
    pass


page_sequence = [
     Instructions, Comprehension, EndComprehension
]