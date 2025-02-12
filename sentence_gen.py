from openai import OpenAI


def gib_line(topic):
    api_key = open(".env", mode="r").read()
    client = OpenAI(api_key=api_key)

    messages = [
        {"role": "user",
                 "content": f" Please generate a very simple and short sentence on the given  topic: {topic}. Write only the sentence, nothing else."}
                ]
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )
    result = completion.choices[0].message.content
    return result

if __name__ == "__main__":
    print(gib_line("cat"))

