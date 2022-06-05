import requests
import time


def getUserId(user):
    try:
        return requests.get(user).text.split("money&target=mail")[1].split("&")[0]
    except IndexError:
        print("Профиль закрыт :(")


def getOnlineFriendsIds(id):
    x = requests.get("https://api.vk.com/method/friends.getOnline?user_id=" + id + "&"
                       "access_token=?&v=5.131").text.split("[")
    ids = x[1].split("]")
    return(ids[0].split(","))


def getFriendsIds(id):
    x = requests.get("https://api.vk.com/method/friends.get?user_id=" + id + "&"
                       "access_token=?&v=5.131").text.split("[")
    ids = x[1].split("]")
    return(ids[0].split(","))


def getFriendInfo(id):
    infoById = requests.get(
        "https://api.vk.com/method/users.get?user_id=" + id + "&"
        "access_token=?&v=5.131").text.split('"')
    return(infoById[7] + " " + infoById[11])


c = 0
# 296403278
userInput = input("Введите id пользователя или ссылку на Vk: ")
if len(userInput.split("/")) > 1:
    user = getFriendInfo(getUserId(str(userInput)))
    userId = getUserId(str(userInput))
else:
    user = getFriendInfo(str(userInput))
    userId = user

print("Друзья онлайн у пользователя: " + str(user))
for i in getOnlineFriendsIds(userId):
    if c == 10:
        time.sleep(1)
        c = 0
    else:
        c += 1
        print(getFriendInfo(i))

print("\n")

print("Все друзья пользователя: " + str(user))
for i in getFriendsIds(userId):
    if c == 10:
        time.sleep(1)
        c = 0
    else:
        c += 1
        print(getFriendInfo(i))