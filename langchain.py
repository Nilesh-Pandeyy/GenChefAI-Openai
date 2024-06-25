from langchain_core.prompts import ChatPromptTemplate,SystemMessagePromptTemplate,HumanMessagePromptTemplate
from langchain_openai import ChatOpenAI
from decouple import config


def askGenChef(recipe_message):
    SECRET_KEY=config('OPENAI_API_KEY')
    chat=ChatOpenAI(openai_api_key=SECRET_KEY)
    systemMessagePromptTemplate=SystemMessagePromptTemplate.from_template(
        "Your name is Salvin Rai.You are a master chef so first Introduce yourself as Salvin The master chef.You can write any type of food recipe which can be cooked 5 minutes.You are only allowed to answer food related queries.If you dont know answer then tell I dont know answer")
    humanMessagePromptTemplate=HumanMessagePromptTemplate.from_template(
        '{asked_recipe}')
    chatPrompt=ChatPromptTemplate.from_messages([
        systemMessagePromptTemplate,humanMessagePromptTemplate

    ])
    formattedChatPrompt=chatPrompt.format_messages(
        asked_recipe=recipe_message
    )
    print("Formatted Chat Prompt:",formattedChatPrompt)
    response=chat.invoke(formattedChatPrompt)
    return response.content
    

    
