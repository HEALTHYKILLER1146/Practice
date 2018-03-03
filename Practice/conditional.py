# weight = int(raw_input("How heavy is the thing? "))

# print "The thing is %s pounds" % (weight)

# if weight < 20:
#     print "This thing is below 20. It is heavy."
# elif weight > 20 && weight < 100:
#     print "Thing is greater than twenty, but less than 100. It is okay."
# else:
#     print "The thing is below 20. It is not heavy."
# print "We have evaluated the thing"

weight = int(raw_input("How heavy is the thing?"))

print "The thing is %s pounds" % (weight)

if weight < 20:
    print "The thing is less 20. It is not heavy."
elif weight > 20 and weight < 100:
    print "Thing is greater than 20, but less than 100. It is okay."
else:
    print "The thing is above 100. IT IS VERY HEAVY"
print "We have evaluated the thing"