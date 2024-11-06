### Sistemas de multi-agentes de inteligencias artificiais

# Biblioteca
from crewai_tools import tool
from crewai import Agent, Task, Crew
from langchain_groq import ChatGroq
from langchain_community.tools import DuckDuckGoSearchRun

# Modelo LLM - Llama3 70B
llm = ChatGroq(temperature=0.7,
               groq_api_key='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',
               model_name='llama3-70b-8192')

# Ferramentas - Busca na internet com DuckDuckGo
@tool('DuckDuckGoSearchRun')
def search_tool(search_query: str):
  ''' Search the web for infotmation on a given topic'''
  return DuckDuckGoSearchRun().run(search_query)

# Topico do blog
topic = "Queimadas no mato grosso"

# Agentes
researcher = Agent(
    role = "Senior Researcher",
    goal = f"Pesquisar noticas sobre {topic}.",
    backstory = "Um pesquisador experiente que tem muita experiencia na área e com vasto conhecimento sobre a regiao do mato grosso",
    verbose = True,
    tools = [search_tool],
    llm = llm,
)

writer = Agent(
    role = "Top Writer",
    goal = f"Cria uma noticia sobre {topic}. ",
    backstory = "É um escritor experiente que escreve noticias em sites regionais",
    verbose = True,
    tools = [search_tool],
    llm = llm,
)

# Tarefas
research_task = Task(
    description = f"Pesquisa sobre as ultimas noticias sobre {topic}.",
    expected_output = "Escreva tres paragrafos em portugues brasil",
    tools = [search_tool],
    agent = researcher,
)

write_task = Task(
    description = f"Escritor experiente que tem experiencia sobre {topic} ",
    expected_output = f"Escreve  5 paragrafos sobre o {topic} em formato markdawn",
    tools = [search_tool],
    agent = researcher,
    output_file = "my-blog.md"
)

# Orquestrador
crew = Crew(
    agents=[researcher, writer],
    tasks = [research_task, write_task]
)

result = crew.kickoff(
    inputs = {"topic": "topic"}
)
