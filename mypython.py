
file = open("material/friendships.txt", "r")


friendships = [x.startswith("friends") for x in file.readlines()]
print(friendships)