from Tasks import *

if __name__ =="__main__":
    # Example
    s = 'Task 1 '
    assert filter_list([1,2,'a','b']) == [1,2],  s+"not pass 1" 
    assert filter_list([1,'a','b',0,15]) == [1,0,15],  s+"not pass 2"
    assert filter_list([1,2,'aasf','1','123',123]) == [1,2,123],  s+"not pass 3"

    s = 'Task 2 '
    assert first_non_repeating_letter("stress") == "t", s+"1-not pass"
    assert first_non_repeating_letter("sTreSS") == 'T',s+"2-not pass"
    assert first_non_repeating_letter("qwerfdTYU") == "q", s+"3-not pass"
    assert first_non_repeating_letter("qqwweerrffdDTtYyUu") == None, s+"3-not pass"
    assert first_non_repeating_letter("") == None, s+"4-Not pass"

    s = 'Task 3 '
    assert digital_root(16)==7, s+"1 not"
    assert digital_root(942)==6, s+"2-not"
    assert digital_root(132189)==6, s+"3-not"
    assert digital_root(493193)==2, s+"4-not"

    s = 'Task 4 '
    assert number_of_pairs([1, 3, 6, 2, 2, 0, 4, 5], 5) == 4, s+"not pass 1"
    assert number_of_pairs([0, 5, 1, 1, 1, 1, 1, 1], 5) == 1, s+"not pass 2"
    assert number_of_pairs([5, 0, 0, 0, 0, 0, 4, 5], 5) == 10, s+"not pass 3"

    # s = 'Task 5 '
    # t = "Fred:Corwill;Wilfred:Corwill;Barney:TornBull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill";
    # sort_friends(t)

    s = 'Extended 1 '
    assert nextBigger(12)  == 21, s+"not pass 1"
    assert nextBigger(513) == 531, s+"not pass 2" 
    assert nextBigger(2017) == 2071, s+"not pass 3"
    assert nextBigger(9) ==  -1, s+"not pass 4"
    assert nextBigger(111) ==  -1, s+"not pass 5"
    assert nextBigger(531) ==  -1, s+"not pass 6"

    s = 'Extended 2 '
    assert ip32_to_txt(2149583361) == "128.32.10.1", s+"not pass 1"
    assert ip32_to_txt(32) == "0.0.0.32", s+"not pass 2"
    assert ip32_to_txt(0) ==  "0.0.0.0", s+"not pass 3"