import sys
import os

# from langchain import OpenAI
from langchain_openai import OpenAI
from langchain.chains import LLMMathChain

llm = OpenAI(
    temperature=0,
    openai_api_key=os.getenv('OPENAI_API_KEY')
)

llm_math = LLMMathChain.from_llm(llm=llm, verbose=True)

llm_math.invoke(sys.argv[1])
