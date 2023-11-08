
def boy_girl(boys, girls):

    boys_ = boys.sort()
    girls_ = girls.sort()

    list1 = (list(zip(boys,girls)))

    if len(boys) == len(girls):
        for i in list1:
            return ' и '.join(i)
    else:
        return 'Кто-то может остаться без пары.'