# Flashcard Model
cards=[
{"question":"dog",
"answers":["an animal","a rock"],
"correct_answer": 1},
{"question":"cat",
"answers":["an animal","a rock"],
"correct_answer": 1},
{"question":"mouse",
"answers":["an animal","a rock"],
"correct_answer": 1}
]

score = 0

# Flashcard View
def show_card(card):
	print card["question"]
	for i, answer in enumerate(card["answers"]):
		print i+1
		print answer


# Flashcard Controller
def get_answer(card):
        global score
	answer=int(raw_input("answer? "))
	if answer==card["correct_answer"]:
                score += 1
		print "correct"
	else:
		print "incorrect"

for card in cards:
        show_card(card)
        get_answer(card)
print 'score'
print score
