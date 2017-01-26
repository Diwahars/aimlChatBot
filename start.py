import aiml
import os

# Create the kernel and learn AIML files

kernel = aiml.Kernel()


if os.path.isfile("bot_brain.brn"):
	kernel.bootstrap(brainFile = "bot_brain.brn")
else:
	kernel.bootstrap(learnFiles = "std-startup.xml",commands = "load aiml b")
	kernel.saveBrain("bot_brain.brn")

# kernel is now ready for use.
# Press CTRL-C to break this loop
while True:
	message = raw_input("message > ")
	if message == "quit":
		exit()
	elif message == "save":
		kernel.saveBrain("bot_brain.brn")
	else:
		# Session id to identify different users 
		sessionId = 0001

		# Every session id is unique
		# The predicate name is the name of something/someone
		# that the bot know about in your session with the bot
		# The bot might know you as "george" and that your "dog" is name "tinu"

		# setPredicate() allow you to set the value of a particular predicate
		kernel.setPredicate("dog","tinu",sessionId)
		# getPredicate() allow you to retrieve the value of a particular predicate
		clients_dog_name = kernel.getPredicate("dog",sessionId)

		kernel.setPredicate("myName","george",sessionId)
		client_name = kernel.getPredicate("myName",sessionId)

		bot_response = kernel.respond(message,sessionId)
		print(bot_response)

