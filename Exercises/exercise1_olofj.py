# -*- coding: utf-8 -*-

#Code written by Olof Jönsson, olof.jonsson@physics.uu.se
#sent to
#python@sinclair.link
#as homework. Finished 23.00 Thursday 13 Oct 2016


#EXERCISE 1
print "**************** EXERCISE 1 \n\n"

  

#This function was stolen from http://stackoverflow.com/a/25885108
# I will comment on each row to prove that I understand it

def countvowels(string): #stating the name of the function
    num_vowels=0           #setting the count to 0 when we begin
    for char in string:    # a loop over each letter in strin
        if char in "aeiouAEIOU":           #This i do not understand. Is this a looping test? Super powerful if so
           num_vowels = num_vowels+1       #ok, looks like if the test above is passed for the char, we count up one
        if char in "0123456789":           #code by me, repeat of above but testing for numbers
           print "Number encoutered: " + char       #printing a warning
    return num_vowels   #return function

my_string="this is the first exercise" #teststring defined
print '{0} vowels in the string \"{1}\"'.format(countvowels(my_string),my_string)

my_string="this is the 1st test to prove that i did part 2 of exercise 1" #teststring defined
print '{0} vowels in the string \"{1}\"'.format(countvowels(my_string),my_string)


#EXERCISE 2
print "\n**************** EXERCISE 2 \n\n"

def print_some_numbers():
    my_number=2
    while my_number<12:
        print my_number
        my_number=my_number+2
    print "Goodbye!"

print_some_numbers()

#EXERCISE 3
print "\n**************** EXERCISE 3 (difference only seen in file) \n\n"

def print_some_numbers2():
    for i in range(1,6):
        print i*2
    print "Goodbye!"

print_some_numbers2()


#EXERCISE 4
print "\n**************** EXERCISE 4 \n\n"


print "my guesses were correct!\n"


my_str = '6.00x'

for char in my_str:
    print(char)

print('done')

# the code
greeting = 'Hello!'
count = 0

for letter in greeting:
    count += 1
    if count % 2 == 0:
        print letter
    print letter

print 'done'

# the code
school = 'uppsala'
num_vowels = 0
num_cons = 0

for char in school:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        num_vowels += 1
    elif char == 'u' or char == 'p':
        print char
    else:
        num_cons -= 1

print('num_vowels is: ' + str(num_vowels))
print('num_cons is: ' + str(num_cons))

#EXERCISE 5
print "\n**************** EXERCISE 5 \n\n"

def bob_count(argument):
    result=0
    for i in range(1,len(argument)-2):
	if argument[i:i+3]=='bob': #looking for bob in the next three chars
            result=result+1
    return result

print bob_count('only one bob') #should give 1
print bob_count('robert')#should give 0
print bob_count('azcbobobegghakl')#should give 2

#EXERCISE 6
print "\n**************** EXERCISE 6 \n\n"


def longest_in_order(argument):
    longest_string=''
    test_string=''
    for i in range(0,len(argument)-1):
        if test_string=='':
            test_string=argument[i] #setting the test string to current letter if it's empty
            print 'starting with new test, {0} is the first letter'.format(test_string) #for debugging, it went ok
        elif argument[i]>=test_string[-1]:
            test_string+=argument[i] #adding this letter if it comes after the last we had before in the test 
            print '{0} comes before {1}, so {0} is now in the test string {2}'.format(argument[i],test_string[-2],test_string) #for debugging, it went ok
        else:   #this only passes if we have encountered a letter that is later     
            if len(test_string)<=len(longest_string):
                print '{0} is not longer than {1}, so we start all over again!'.format(test_string,longest_string)
                test_string=argument[i] #and we need to actually add it even if we start over
            else:
                longest_string=test_string
                test_string=argument[i] #and we need to actually add it even if we start over
                print 'our new longest string is now {0}!'.format(longest_string)
               
    return longest_string

s = 'azcbobobegghakl'

the_substring=longest_in_order(s)
print '**Output'
print 'Longest substring in alphabetical order is: ',the_substring

print "\n**************** EXERCISE 7 \n\n"
print "I don't understand what I am supposed to do"#