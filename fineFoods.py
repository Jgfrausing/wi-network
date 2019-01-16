def avg_score_of_friends(user)
	friends = get_friends(user)
	friends_with_score = [x for x in friends if x.score is not None]

	#using clustering.py (graph cutting)
	cluster = get_users_cluster(user)

	total_weight = 0
	total_score = 0

	for friend in friends_with_score:
		#kyle is 10 times more influential
		important = 10 if friend == 'kyle' else 1
		if friend in cluster:
			total_score += friend.score*important
			total_weight += 1*important

		else:
			#friends not in users cluster are 10 times more influential
			total_score += friend.score*10*important
			total_weight += 10*important

	return total_score/total_weight