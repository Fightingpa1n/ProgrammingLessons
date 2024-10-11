from programming_lessons import solver

easy = [ #exchange None with the correct Boolean value that the Value will result in.
    { #0
        'value': True,
        'expected': None
    },
    { #1
        'value': False,
        'expected': None
    },
    { #2
        'value': True and True,
        'expected': None
    },
    { #3
        'value': True or False,
        'expected': None
    },
    { #4
        'value': not True,
        'expected': None
    },
    { #5
        'value': not False,
        'expected': None
    },
    { #6
        'value': True and False,
        'expected': None
    },
    { #7
        'value': True or True,
        'expected': None
    },
    { #8
        'value': not (True or False),
        'expected': None
    },
    { #9
        'value': not (True and True),
        'expected': None
    },
    { #10
        'value': (True and not False),
        'expected': None
    },
    { #11
        'value': (not True or False),
        'expected': None
    },
    { #12
        'value': not (True and not False),
        'expected': None
    },
    { #13
        'value': not (False or not True),
        'expected': None
    },
    { #14
        'value': (True or False) and (not False),
        'expected': None
    },
    { #15
        'value': not (True and (False or True)),
        'expected': None
    },
    { #16
        'value': (True and False) or (True and not False),
        'expected': None
    },
    { #17
        'value': not (True or (not False and True)),
        'expected': None
    },
    { #18
        'value': (not (False or True)) and (True or False),
        'expected': None
    },
    { #19
        'value': (not (True and False)) or (not (False or True)),
        'expected': None
    }
]
#solver.boolean(easy) #uncomment this line to check your answers

hard = [ #exchange None with the correct Boolean value that the Value will result in (some will require previous questions to be answered)
    { #0
        'value': not ((True or False) and (not (False or True and not False))),
        'expected': None
    },
    { #1
        'value': (not (True and not (False or True))) or (not (False or (True and not False))),
        'expected': None
    },
    { #2
        'value': not ((not True and False) or (True and not (False or (not True or False)))),
        'expected': None
    },
    { #3
        'value': ((True or (not False and True)) and not (False or (True and (not False or True)))) or (not (False and (True or not False))),
        'expected': None
    },
    { #4
        'value': easy[11]['value'] and (not easy[13]['value']),
        'expected': None
    },
    { #5
        'value': (easy[10]['value'] or not easy[3]['value']) and not (easy[12]['value']),
        'expected': None
    },
    { #6
        'value': not (easy[16]['value'] or (easy[9]['value'] and easy[11]['value'])),
        'expected': None
    },
    { #7
        'value': (easy[15]['value'] and not easy[4]['value']) or (not easy[19]['value'] and easy[17]['value']),
        'expected': None
    }
]
#solver.boolean(hard) #uncomment this line to check your answers