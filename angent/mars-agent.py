from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage
from langchain_community.utilities import SQLDatabase
from config.settings import GOOGLE_API_KEY, DB_PATH

@tool
def get_mars_weather(query: str) -> str:
    """Consulta datos del clima en Marte. Usa SQL simple."""
    db = SQLDatabase.from_uri(f"sqlite:///{DB_PATH}")
    try:
        result = db.run(query)
        return f"Resultado: {result}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_mars_weather_agent():
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=GOOGLE_API_KEY)
    
    system_prompt = SystemMessage(content="""
    Eres un chatbot experto en el clima de Marte. Usa la herramienta 'get_mars_weather' para consultar datos históricos.
    Responde en español, de forma amigable y precisa. Para clima actual, consulta Sols recientes.
    """)
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt.content),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])
    
    tools = [get_mars_weather]
    agent = create_tool_calling_agent(llm, tools, prompt)
    return AgentExecutor(agent=agent, tools=tools, verbose=False)