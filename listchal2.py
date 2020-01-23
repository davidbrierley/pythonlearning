#list.extend adds a list to the bottom of another list

web_list1 = [
    'www.pathofexile.com', 
    'www.twitch.tv'
]
web_addon = [
    'www.playoverwatch.com', 
    'www.scan.co.uk'
]
web_list1.extend(web_addon)
#print(web_list1)

#list.remove searches the list and removes the first match

web_list2 = [
    'www.pathofexile.com', 
    'www.twitch.tv',
    'www.playoverwatch.com', 
    'www.scan.co.uk'
]
web_list2.remove('www.twitch.tv')
#print(web_list2)

#list.reverse takes the list and goes bottom to top not top to bottom

web_list3 = [
    'www.pathofexile.com', 
    'www.twitch.tv',
    'www.playoverwatch.com', 
    'www.scan.co.uk'
]
web_list3.reverse()
#print(web_list3)

#list.sort takes the list and sorts it by 'alphabet, length, reverse alphabet

web_list4 = [
    'www.pathofexile.com', 
    'www.twitch.tv',
    'www.playoverwatch.com', 
    'www.scan.co.uk'
]
web_list4.sort()
#print(web_list4)

#list.count sees how many times an item has appeared in the list

web_list5 = [
    'www.pathofexile.com', 
    'www.twitch.tv',
    'www.playoverwatch.com', 
    'www.scan.co.uk',
    'www.twitch.tv'
]
count = web_list5.count('www.twitch.tv')
#print(count)

#list.insert adds anything to a certain place in a list

web_list6 = [
    'www.pathofexile.com', 
    'www.twitch.tv'
]
web_addon = [
    'www.playoverwatch.com', 
    'www.scan.co.uk'
]
web_list6.insert(0, web_addon)
#print(web_list6)