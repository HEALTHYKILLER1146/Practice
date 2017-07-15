# Flashcard Model
card={"question":"dog",
"answers":["an animal","a rock"],
"correct_answer": 1}

# Flashcard View
def show_card(card):
	print card["question"]
	for i, answer in enumerate(card["answers"]):
		print i+1
		print answer


# Flashcard Controller
def get_answer(card):
	answer=int(raw_input("answer? "))
	if answer==card["correct_answer"]:
		print "correct"
	else:
		print "incorrect"

show_card(card)
get_answer(card)