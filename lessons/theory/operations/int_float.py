#============================================== Int / Float ==============================================# (or just math operations for short)

#==================== add ====================# (+)
def math_addition(): #my jokes sure don't add up

    #examples:
    print(1 + 1) #1 | int + int
    print(1.09 + 1.91) #2 | float + float
    print(1 + 1.001) #3 | int + float

#math_addition() #(comment this in and out to only run this section of the code)


#==================== subtract ====================# (-)
def math_subtraction(): #wow I really should subtract myself from these lessons

    #examples:
    print(5 - 2) #1 | int - int
    print(5.0 - 2.0) #2 | float - float
    print(5 - 2.0) #3 | int - float

#math_subtraction() #(comment this in and out to only run this section of the code)


#==================== multiply ====================# (*)
def math_multiplication(): #Hello everybody, my name is Multiplier and welcome back to Five Nights at Freddy's

    #examples:
    print(2 * 3) #1 | int * int
    print(2.0 * 3.0) #2 | float * float
    print(2 * 3.0) #3 | int * float
    print(10 * 0.5) #4 | int * float

#math_multiplication() #(comment this in and out to only run this section of the code)


#==================== divide ====================# (/)
def math_division(): #I'm really divided on whether or not to continue with adding jokes

    #examples:
    print(8 / 2) #1 | int / int
    print(8.0 / 2.0) #2 | float / float
    print(8 / 2.0) #3 | int / float
    print(8 // 2)  #4 | int // int
    print(9 // 2.0)  #5 | float // float
    print(10.0 // 3) #6 | int // int

#math_division() #(comment this in and out to only run this section of the code)


#==================== exponentiation ====================# (**)
def math_exponentiation(): #exponetally increasing my cringe, yay...

    #examples:
    print(2 ** 3) #1 | int ** int
    print(2.0 ** 3.0) #2 | float ** float
    print(2 ** 3.5) #3 | int ** float 

#math_exponentiation() #(comment this in and out to only run this section of the code)


def explanation(): #blah blah blah, boring talk
    value_1 = 5
    value_2 = 8

    #print(value_1 + value_2) #1

    #value_3 = value_1 + value_2
    #print(value_3) #2

    #print(value_1) #3
    
    #value_1 = value_1 + value_2
    #value_1 -= value_2 # = sichselbst + wasauchimmer nachher
    #print(value_1) #4

    #value_1 += value_2 #value_1 = value_1 + value_2
    #value_1 -= value_2 #value_1 = value_1 - value_2
    #print(value_1)
    #print(value_2)

#explanation() #Note to futre self: I know you need to explain something here so I made this function ready for you ;)


#==================== add assignment ====================# +=
def math_add_assignment(): #add some more fun... or not, I'm not your Teacher... wait

    #examples:
    int_value = 1
    print(int_value) #1 | just the int without any operations
    int_value += 1
    print(int_value) #1 | the int after the addition

    float_value = 1.0
    print(float_value) #2 | just the float without any operations
    float_value += 1.0
    print(float_value) #2 | the float after the addition

    mix_value = 1
    print(mix_value) #3 | just the int without any operations
    mix_value += 1.0
    print(mix_value) #3 | the int after the addition of a float

#math_add_assignment() #(comment this in and out to only run this section of the code)


#==================== subtract assignment ====================# -=
def math_subtract_assignment(): #the quality of my jokes is really starting to subtract itself

    #examples:
    int_value = 2
    print(int_value) #1 | just the int without any operations
    int_value -= 1
    print(int_value) #1 | the int after the subtraction

    float_value = 2.0
    print(float_value) #2 | just the float without any operations
    float_value -= 1.0
    print(float_value) #2 | the float after the subtraction

    mix_value = 2
    print(mix_value) #3 | just the int without any operations
    mix_value -= 1.0
    print(mix_value) #3 | the int after the subtraction of a float

#math_subtract_assignment() #(comment this in and out to only run this section of the code)


#==================== multiply assignment ====================# 
def math_multiply_assignment(): #multiplying my problems, one assignment at a time

    #examples:
    int_value = 2
    print(int_value) #1 | just the int without any operations
    int_value *= 3
    print(int_value) #1 | the int after the multiplication

    float_value = 2.0
    print(float_value) #2 | just the float without any operations
    float_value *= 3.0
    print(float_value) #2 | the float after the multiplication

    mix_value = 2
    print(mix_value) #3 | just the int without any operations
    mix_value *= 3.0
    print(mix_value) #3 | the int after the multiplication of a float

    steve = 10
    print(steve) #4 | just the int without any operations
    steve *= 0.5
    print(steve) #4 | the int after the multiplication of a float

#math_multiply_assignment() #(comment this in and out to only run this section of the code)


#==================== divide assignment ====================#
def math_divide_assignment(): #maybe I would have these lessons faster ready if I knew how to divide my time better

    #examples:
    int_value = 8
    print(int_value) #1 | just the int without any operations
    int_value /= 2
    print(int_value) #1 | the int after the division

    float_value = 8.0
    print(float_value) #2 | just the float without any operations
    float_value /= 2.0
    print(float_value) #2 | the float after the division

    mix_value = 8
    print(mix_value) #3 | just the int without any operations
    mix_value /= 2.0
    print(mix_value) #3 | the int after the division of a float

    steve = 10
    print(steve) #4 | just the int without any operations
    steve //= 3
    print(steve) #4 | the int after the division

#math_divide_assignment() #(comment this in and out to only run this section of the code)


#==================== exponentiation assignment ====================# (**=)
def math_exponentiation_assignment(): #my cringe is exponentally increasing if I go on like this.

    #examples:
    int_value = 2
    print(int_value) #1 | just the int without any operations
    int_value **= 3
    print(int_value) #1 | the int after exponentiation (int_value = int_value ** 3), result: 8

    float_value = 4.0
    print(float_value) #2 | just the float without any operations
    float_value **= 0.5
    print(float_value) #2 | the float after exponentiation (float_value = float_value ** 0.5), result: 2.0 (square root)
