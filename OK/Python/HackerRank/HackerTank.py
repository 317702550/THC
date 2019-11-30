me_1 = 10
me = 10
counter = 0
counter_level = 1
bugs = int(input())
levels = [input() for i in range(bugs)]
while me > 0:
        for n in range (bugs):
                if int(levels[n]) < me:
                        me = me - 1
                elif levels[n] == me:
                        me = me - int(levels[n])
                else:
                        me = me - 2*int(levels[n])
        if counter//3 == counter/3 and n != 0:
                me = me_1 + 5
                me_1 = me
                counter_level = counter_level + 1
        counter = counter + 1
        print(me)
        print(counter)
        print(counter_level)

else:
    print("You have died. Reached level %s and killed %s bugs"%(counter_level,counter))
