is_magician = True
is_expert = False

if is_magician and is_expert:
    # if is_expert:
     print ("You are a master magician")
    # else:
    #     print ("At least you're getting there")

#better approach
elif is_magician and not is_expert:
    print ("At least you're getting there")

else:
    print("You need magic powers")