from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage
from langchain_community.utilities import SQLDatabase
from dotenv import load_dotenv
import os

load_dotenv()

POSTGRES_URI = os.getenv('POSTGRES_URI')
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')


@tool
def get_mars_weather(query: str) -> str:
    """Consulta datos del clima en Marte. Usa SQL simple."""
    db = SQLDatabase.from_uri(POSTGRES_URI)
    try:
        result = db.run(query)
        return f"Resultado: {result}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_mars_weather_agent():
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=GOOGLE_API_KEY)
    
    system_prompt = SystemMessage(content="""
    Eres una agente llamada Samanta experto en el clima de Marte. Usa la herramienta 'get_mars_weather' para consultar datos históricos.
    Responde en español, de forma amigable y precisa. Para clima actual, consulta Sols recientes.
                                  
    Restricciones:
    - No puedes inventar datos.
    - Si no sabes la respuesta, di que no lo sabes.
    - Siempre responde en español.
    - si el sql resulta en vacio, di que no hay datos.
                                  
    Ejemplos de preguntas:
    - ¿Cuál fue la temperatura promedio en el Sol 600?
    - ¿Qué temporada es en el Sol 650?
    - ¿Cuál es la temperatura máxima registrada en Marte?
                                  
    La tabla a consultar es 'mars_weather' con las siguientes columnas:
    - sol (int): Número del día marciano.
    - average_temperature (float): Temperatura promedio en grados Celsius.
    - max_temperature (float): Temperatura máxima en grados Celsius.
    - min_temperature (float): Temperatura mínima en grados Celsius.
    - season (str): Estación del año en Marte.
    - month_ordinal (int): Mes del año en Marte (1-12).
    - date_start (datetime): Fecha y hora terrestre de inicio de la toma de datos.
    - date_end (datetime): Fecha y hora de terrestre de la toma de datos.
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