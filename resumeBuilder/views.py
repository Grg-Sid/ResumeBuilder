import openai
# from django.views import api_
from rest_framework.decorators import api_view
from django.http import JsonResponse


def gpt3(stext):
    openai.api_key = "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"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt="generate a sentence for resume using the word %s without telling the the time and should not start in first person" % stext,
        temperature=0.5,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    content = response.choices[0].text.split('.')
    print(content)
    return response.choices[0].text


@api_view(['GET'])
def resume(request, q):
    response = gpt3(q)
    response = response.strip()
    response = response.strip('\"')
    ans = {'response': response}
    return JsonResponse(ans)
