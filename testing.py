# prompt = f'''I will give you a text, The text may contain name of one of the following:
                #             You need to give me details about it:
                #             the text is:   
                #             {animallabels[index]}'''
                # response = openai.Completion.create(
                #     engine="text-davinci-003", prompt=prompt, max_tokens=3000
                # )
                # answer = response.choices[0]['text']