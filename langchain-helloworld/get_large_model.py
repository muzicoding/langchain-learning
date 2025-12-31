#导入 dotenv 库的 load_dotenv 函数，用于加载环境变量文件（.env）中的配置
import dotenv
from langchain_openai import ChatOpenAI
import os

# 加载环境变量文件
dotenv.load_dotenv()

# 获取open-ai的api密钥
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

# 创建 ChatOpenAI 对象
llm = ChatOpenAI(model="gpt-4o-mini")

# 直接提供问题，并调用llm
response = llm.invoke("什么是大模型？")

# 打印结果
print(response)

