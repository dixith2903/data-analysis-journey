import time
import random

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "She sells seashells by the seashore.",
    "How much wood would a woodchuck chuck if a woodchuck could chuck wood?",
    "I scream, you scream, we all scream for ice cream.",   
]

def measure_accuracy(test_sentence, user_input):
    test_words = test_sentence.split(" ")
    user_words = user_input.split(" ")
    correct_words = sum(1 for t, u in zip(test_words, user_words) if t == u)
    accuracy = (correct_words / len(test_words)) * 100
    return accuracy

def typing_test():
    test_sentence = random.choice(sentences)
    print("Type the following sentence as fast as you can:")
    print(test_sentence)
    input("Press Enter to start...")
    start_time = time.time() #Measuring the start time
    user_input = input("\nStart typing: \n")
    end_time = time.time() #Measuring the end time
    time_taken = end_time - start_time
    words_count = len(test_sentence.split(" "))

    print(f"Results:")
    print(f"Time taken: {time_taken:.2f} seconds")
    print(f"Words typed: {words_count}")
    print(f"Typing speed: {words_count / time_taken * 60:.2f} words per minute")
    print(f"Accuracy: {measure_accuracy(test_sentence, user_input):.2f}%")


typing_test()