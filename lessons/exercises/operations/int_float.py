from programming_lessons import solver

easy = [ #Exchange None with the correct numerical value based on the operation result.
    { #0
        'operation': 1 + 1,
        'expected': None
    },
    { #1
        'operation': 2 - 1,
        'expected': None
    },
    { #2
        'operation': 3 * 2,
        'expected': None
    },
    { #3
        'operation': 10 / 2,
        'expected': None
    },
    { #4
        'operation': 5 + 2.0,
        'expected': None
    },
    { #5
        'operation': 7 - 3.0,
        'expected': None
    },
    { #6
        'operation': 4 * 1.5,
        'expected': None
    },
    { #7
        'operation': 9 // 2,
        'expected': None
    },
    { #8
        'operation': 10 ** 2,
        'expected': None
    },
    { #9
        'operation': 25 // 4,
        'expected': None
    },
    { #10
        'operation': 1 + 1,
        'expected': None
    },
    { #11
        'operation': 2 - 1,
        'expected': None
    },
    { #12
        'operation': 3 * 2,
        'expected': None
    },
    { #13
        'operation': 10 / 2,
        'expected': None
    },
    { #14
        'operation': 5 + 2.0,
        'expected': None
    },
    { #15
        'operation': 7 - 3.0,
        'expected': None
    },
    { #16
        'operation': 4 * 1.5,
        'expected': None
    },
    { #17
        'operation': 9 / 3.0,
        'expected': None
    },
    { #18
        'operation': (5 + 3) * 2,
        'expected': None
    },
    { #19
        'operation': (10 - 5) / 2,
        'expected': None
    }
]
#solver.math(easy) #uncomment this line to check your answers

medium = [ #Exchange None with the correct numerical value based on the operation result.
    { #0
        'operation': 10 + 5 * 2,
        'expected': None
    },
    { #1
        'operation': (10 + 5) * 2,
        'expected': None
    },
    { #2
        'operation': 8 / (2 + 2),
        'expected': None
    },
    { #3
        'operation': 3 * (2 + 4),
        'expected': None
    },
    { #4
        'operation': 10 // 3 + 7 * 2,
        'expected': None
    },
    { #5
        'operation': 16 // (4 * 2),
        'expected': None
    },
    { #6
        'operation': 9 ** 0.5,  #(**0.5 = Square root)
        'expected': None
    },
    { #7
        'operation': (3 ** 2 + 1) // 2,
        'expected': None
    },
    { #8
        'operation': 12.5 // 2.5,
        'expected': None
    },
    { #9
        'operation': (5 * 2) ** 2,
        'expected': None
    },
    { #10
        'operation': 10 + 5 * 2,
        'expected': None
    },
    { #11
        'operation': (10 + 5) * 2,
        'expected': None
    },
    { #12
        'operation': 8 / (2 + 2),
        'expected': None
    },
    { #13
        'operation': 3 * 3 + 1,
        'expected': None
    },
    { #14
        'operation': (5.0 + 2) * 2 - 1,
        'expected': None
    },
    { #15
        'operation': (6 - 2.0) / 2 + 4,
        'expected': None
    },
    { #16
        'operation': 4 * (3 + 2) / 5,
        'expected': None
    },
    { #17
        'operation': (12 / 3) + (5 * 2),
        'expected': None
    },
    { #18
        'operation': 15 // 4,
        'expected': None
    },
    { #19
        'operation': 5 ** 2,
        'expected': None
    }
]
solver.math(medium) #uncomment this line to check your answers

hard = [ #Exchange None with the correct numerical value based on the operation result.
    { #0
        'operation': (10 + 5 * 2) - (8 / 4) + 3 ** 2,
        'expected': None
    },
    { #1
        'operation': ((6 + 4) / 2) * (3 ** 2),
        'expected': None
    },
    { #2
        'operation': (10 + (2 * 3)) / (4 - 2) + 5 ** 2,
        'expected': None
    },
    { #3
        'operation': (8 / 2 + 3) * (5 - 2) - 4 ** 2,
        'expected': None
    },
    { #4
        'operation': (20 // 3) ** 2 + (5 * 2 - 3),
        'expected': None
    },
    { #5
        'operation': (2 ** 3) // 3 + (5 - 1) ** 2,
        'expected': None
    },
    { #6
        'operation': 100 / (10 - 5) + 6 ** 2 - 4,
        'expected': None
    },
    { #7
        'operation': 15 // 4 + 2 ** 3 * (5 - 3),
        'expected': None
    },
    { #8
        'operation': ((20 / 5) + (3 ** 2)) * ((5 - 1) / 2),
        'expected': None
    },
    { #9
        'operation': (7 ** 2) // 5 + (3 ** 2) * 2,
        'expected': None
    },
    { #10
        'operation': (10 + 5 * 2) - (8 / 4) + 3 ** 2,
        'expected': None
    },
    { #11
        'operation': ((6 + 4) // 2) * (3 ** 2),
        'expected': None
    },
    { #12
        'operation': (10 + (2 * 3)) / (4 - 2) + 5 ** 2,
        'expected': None
    },
    { #13
        'operation': (8 / 2 + 3) * (5 - 2) - 4 ** 2,
        'expected': None
    },
    { #14
        'operation': medium[1]['operation'] * 2 + 1,
        'expected': None
    },
    { #15
        'operation': (medium[4]['operation'] - medium[0]['operation']) / 3,
        'expected': None
    },
    { #16
        'operation': 100 / (10 - 5) + 6 ** 2 - 4,
        'expected': None
    },
    { #17
        'operation': (15 // 4) + 2 ** 3 * (5 - medium[3]['operation']),
        'expected': None
    },
    { #18
        'operation': ((20 / 5) + (3 ** 2)) * ((5 - 1) / 2),
        'expected': None
    },
    { #19
        'operation': (medium[7]['operation'] + easy[0]['operation']) / 2,
        'expected': None
    }
]
#solver.math(hard) #uncomment this line to check your answers