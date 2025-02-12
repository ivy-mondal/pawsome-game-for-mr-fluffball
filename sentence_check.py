from openai import OpenAI


def check_line(ai_sentence, player_sentence):
    api_key = open(".env", mode="r").read()
    client = OpenAI(api_key=api_key)

    messages = [
        {"role": "user",
         "content": f"Your task is to compare sentence 1: {ai_sentence} and sentence 2: {player_sentence}. Write correct if they both convey same meaning and write incorrect if they don't , nothing else."}
    ]

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )
    result = completion.choices[0].message.content
    return result == "correct"

if __name__ == "__main__":
    print(check_line("The cat is sleeping silently", "The cat is sleeping without making any sound"))
    print(check_line("the cat is sleeping peacefully", "the cat is sleeping"))

