# Greet the user
print("Hello. I am a researcher of artificial minds and quantum systems. What label should I assign to your consciousness? : ")

# Get user input
name = input()

# Respond to the user's name
print(f"Data received. It is a pleasure to interact with your neural network, {name}!")

# Ask a question
print("What is the current state of your cognitive system? (good/bad) : ")
mood = input().lower()

# Use conditional statements to respond based on input
if mood == "good":
    print("Your system is exhibiting constructive interference. I am glad to record this positive data.")
elif mood == "bad":
    print("I detect emotional decoherence. I hypothesize your state will return to equilibrium soon.")
else:
    print("I see. Your feelings are in a quantum superposition, too complex to collapse into a simple binary output.")

# End the conversation
print(f"Thank you for sharing your data, {name}. Ending observation protocol. Goodbye!")