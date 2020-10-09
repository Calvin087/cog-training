# ctrl alt m - terminate code runner
print("\n") # formatting

friends = {"Jon", "Sam", "Steve", "Rudy"}

friends_with_S = {friend for friend in friends if friend.startswith("S")}
friends_with_J = {x for x in friends if x.startswith("J")}
# looks like first and second parameters need to be the same, then the thing i'm searching, then if statement

print(friends_with_S)
print(friends_with_J)

print("\n") # formatting