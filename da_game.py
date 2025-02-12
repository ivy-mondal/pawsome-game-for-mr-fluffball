from  sentence_gen  import  gib_line
from  sentence_check import  check_line

if  __name__ == "__main__":
    print("Are we pwaying?! 🤔")
    print("Correct answer is yosh obviously 😎")
    print("Gib Topic Neow 😺🔫 ")
    topic = input("Gib topic here: ")
    print("Goof! Neow wait for the sentence 🙃")
    sentence = gib_line(topic)
    print(f"Yo sentence is:  {sentence}")
    print("What will yo answer be?! 🐱")
    pwayer_answer = input("Gib yo answer here: ")
    print("Wait and me check answah UwU")
    da_verdict = check_line(sentence, pwayer_answer)
    print(f"Yo verdict is: {da_verdict}")

