import re
strings_list = []
pattern_list = []
# Autogenerated with DRAKON Editor 1.31

def main():
    #item 32
    main_regex()


def main_regex():
    #item 6
    print("Let's play with regex")
    #regex_1_1()		#strings
    #regex_1_2()		#special_chars
    regex_2_0()		#refactoring flow


def regex_1_1():
    #item 38
    regex = 'Python'
    
    target_strings = ["Pytho","Python","Pythons","Python2", ""]
    
    p = re.compile(regex)
    #item 42
    print("For the regex: '{}'".format(p.pattern))
    for target in target_strings:
        #item 41
        
        print("String: {} ".format(target))
        print(p.match(target))


def regex_1_2():
    #item 58
    regex_1_2_chars()
    regex_1_2_or()
    regex_1_2_dot()
    regex_1_2_dot2()
    regex_1_2_start()
    regex_1_2_end()
    
    regex_1_2_match0()
    regex_1_2_match1()
    regex_1_2_match_preceding()
    regex_1_2_match_preceding_count()
    regex_1_2_match_preceding_range()
    regex_1_2_match_range()
    regex_1_2_match_range2()


def regex_1_2_chars():
    #item 154
    target_strings = ["dna", "dnd","ddd","dads","aaa"]
    
    re1 = '...'
    p = re.compile(re1)
    #item 158
    print("For the regex: '{}'".format(p.pattern))
    for target in target_strings:
        #item 157
        
        print("String: {} ".format(target))
        print(p.match(target))


def regex_1_2_dot():
    #item 64
    target_strings = ["dna", "dnd","ddd","dads","aaa"]
    # dnd, ddd, dad - matches
    
    re1 = 'd.d'
    p = re.compile(re1)
    #item 68
    print("For the regex: '{}'".format(p.pattern))
    for target in target_strings:
        #item 67
        
        print("String: {} ".format(target))
        print(p.match(target))


def regex_1_2_dot2():
    #item 74
    target_strings = ["dna", "dnd","ddd","dads","aaa"]
    # dads match
    
    re1 = 'd.d.'
    p = re.compile(re1)
    #item 78
    print("For the regex: '{}'".format(p.pattern))
    for target in target_strings:
        #item 77
        
        print("String: {} ".format(target))
        print(p.match(target))


def regex_1_2_end():
    #item 94
    target_strings = ["isis", "climate", "sniper", " attacks", "NYC", "Shutdown"]
    # isi[s], attack[s]
    
    re1 = 's$'
    p = re.compile(re1)
    #item 98
    print("For the regex: '{}'".format(p.pattern))
    for target in target_strings:
        #item 97
        
        print("String: {} ".format(target))
        print(p.search(target))


def regex_1_2_match0():
    #item 104
    target_strings = ["","a1","A","Aa","aA","AAA"]
    re1 = '[A-F]*'
    p = re.compile(re1)
    #item 108
    print("""
    For the regex: '{}' \t {}""".format(p.pattern, target_strings))
    for target in target_strings:
        #item 107
        print("{} with {}".format(target,repr(p.search(target))))


def regex_1_2_match1():
    #item 114
    target_strings = ["","a1","A","Aa","aA","AAA"]
    re1 = '[A-F0-9]+'
    p = re.compile(re1)
    #item 118
    print("""
    For the regex: '{}' \t {}""".format(p.pattern, target_strings))
    for target in target_strings:
        #item 117
        print("{} with {}".format(target,repr(p.search(target))))


def regex_1_2_match_not():
    #item 184
    target_strings = ["","1","31","411","5111","11111111","hello", "World"]
    re1 = '[^.a-z]'
    p = re.compile(re1)
    #item 188
    print("""
    For the regex: '{}' \t {}""".format(p.pattern, target_strings))
    for target in target_strings:
        #item 187
        print("{} with {}".format(target,repr(p.search(target))))


def regex_1_2_match_preceding():
    #item 124
    target_strings = ["", "it","itititit"]
    re1 = 'it?'
    p = re.compile(re1)
    #item 128
    print("""
    For the regex: '{}' \t {}""".format(p.pattern, target_strings))
    for target in target_strings:
        #item 127
        print("{} with {}".format(target,repr(p.search(target))))


def regex_1_2_match_preceding_count():
    #item 134
    target_strings = ["","1","11","111","1111","11111111"]
    re1 = '[0-9]{3}'
    p = re.compile(re1)
    #item 138
    print("""
    For the regex: '{}' \t {}""".format(p.pattern, target_strings))
    for target in target_strings:
        #item 137
        print("{} with {}".format(target,repr(p.search(target))))


def regex_1_2_match_preceding_range():
    #item 144
    target_strings = ["","1","11","111","1111","11111111"]
    re1 = '[0-9]{3,5}'
    p = re.compile(re1)
    #item 148
    print("""
    For the regex: '{}' \t {}""".format(p.pattern, target_strings))
    for target in target_strings:
        #item 147
        print("{} with {}".format(target,repr(p.search(target))))


def regex_1_2_match_range():
    #item 164
    target_strings = ["","1","31","411","5111","11111111"]
    re1 = '[.2-4]'
    p = re.compile(re1)
    #item 168
    print("""
    For the regex: '{}' \t {}""".format(p.pattern, target_strings))
    for target in target_strings:
        #item 167
        print("{} with {}".format(target,repr(p.search(target))))


def regex_1_2_match_range2():
    #item 174
    target_strings = ["","1","31","411","5111","11111111","hello", "world"]
    re1 = '[.a-zA-Z]'
    p = re.compile(re1)
    #item 178
    print("""
    For the regex: '{}' \t {}""".format(p.pattern, target_strings))
    for target in target_strings:
        #item 177
        print("{} with {}".format(target,repr(p.search(target))))


def regex_1_2_or():
    #item 48
    re1 = 'David'
    re2 = 'Python'
    
    target_strings = ["Python","John","snow","David", "knows"]
    
    p = re.compile(re1+"|"+re2)
    #item 52
    print("For the regex: '{}'".format(p.pattern))
    for target in target_strings:
        #item 51
        
        print("String: {} ".format(target))
        print(p.match(target))


def regex_1_2_start():
    #item 84
    target_strings = ["carbon","tax","revolt","climate"]
    # [c]arbon, [c]limate
    
    re1 = '^c'
    p = re.compile(re1)
    #item 88
    print("For the regex: '{}'".format(p.pattern))
    for target in target_strings:
        #item 87
        
        print("String: {} ".format(target))
        print(p.match(target))


def regex_2_0():
    #item 204
    #regex_2_refactoring()
    #regex_2___()
    regex_2___1()


def regex_2___():
    #item 210
    print("""
    Identifiers: 
    \ used to escape a character 
    \d any number 
    \D anything but a number 
    \s space 
    \S anything but a space 
    \w any character 
    \W anything but a character 
    . any character except a new line 
    \. actually a period 
    \b whitespace around words 
    
    Modifiers: 
    {1,3} we're expecting 1-3 
    + Match 1 or more 
    ? Match 0 or 1 
    * Match 0 or more 
    $ match the end of a string 
    ^ match the beginning of a string 
    | matches either or e.g. \d{1-3}|\w{5-6} 
    [] Match range or "variance" e.g. [A-Za-z] or [1-5a-qA-Z] 
    {x} expecting "x" amount 
    
    White Space characters: 
    \n new line 
    \s space 
    \t tab 
    \e escape (rare) 
    \f form feed (rare) 
    \r return
    
     DON'T FORGET!: . + * ? [ ] $ ^ ( ) { } \ |﻿
    """)


def regex_2___1():
    #item 216
    strings_list.append('''
    abcdefghijklmnopqurtuvwxyz
     xyz
    ABCDEFGHIJKLMNOPQRSTUVWXYZ
    
    1234567890
    
    
    MetaCharacters (Need to be escaped):
    . ^ $ * + ? { } [ ] \ | ( )
    
    DavidsIT.Site
    
    404-576-3096
    123.777.1234
    123*777*1234
    800-777-1234
    900-777-1234
    
    192.168.0.1
    10.10.10.1
    
    admin:P@ssword
    
    David
    Fights for
    Individualism
    MYOBs: MyObligation is to tell you to Mind Your own business
    
    ''')
    #item 218
    strings_list.append( """grinding is a good start but 
    work your way to a conclusion other than grind""")
    #item 217
    pattern_list.append(r'abc')
    pattern_list.append(r'ABC')
    
    #pattern_list.append(r'.')  # lots of printout
    
    pattern_list.append(r'xyz')
    pattern_list.append(r'\bxyz')
    pattern_list.append(r'\Bxyz')
    
    pattern_list.append(r'grind')
    pattern_list.append(r'^grind')
    pattern_list.append(r'grind$')
    for pattern in pattern_list:
        #item 242
        regex_2___1_print(strings_list,pattern)


def regex_2___1_print(strings_list, pattern):
    #item 241
    print("\n"+pattern)
    pattern = re.compile(pattern)
    for element in strings_list:
        #item 238
        matches = pattern.finditer(element)
        for match in matches:
            #item 235
            print(match)


def regex_2_refactoring():
    #item 194
    
    re1 = '[.a-zA-Z]'
    
    strings_list.append("2")
    
    
    p = re.compile(re1)
    #item 198
    print("""
    For the regex: '{}' \t {}""".format(p.pattern, strings_list))
    for target in strings_list:
        #item 197
        print("{} with {}".format(target,repr(p.search(target))))

main()
