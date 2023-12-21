#program called comma code
#Write a function that takes a list value as an argument and 
# returns a string with all the items separated by a comma and a space, 
# with and inserted before the last item. For example, passing the 
# previous spam list to the function would return 'apples, bananas, 
# tofu, and cats'. But your function should be able to work with any 
# list value passed to it. Be sure to test the case where an empty list 
# [] is passed to your function.
def sentence_maker(items):
    sentence = ""
    for i in items:
        if i == "":
            break
        else:
            sentence = sentence + str(i) + ", "
    return sentence



print(sentence_maker([1, "long", 24, "tardy"]))
