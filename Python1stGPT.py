from fake_useragent import UserAgent as ua
from typing import List, Dict
import urllib.parse
import json as JSON
import asyncio
import aiohttp

class Python1stGPT():
    def __init__(self, model="gpt-4o-mini"):
        self.model = model
        self.base_url = "https://duck.gpt-api.workers.dev/chat/"
        self.models = ['gpt-4o-mini', 'claude-3-haiku-20240307', 'meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo', 'mistralai/Mixtral-8x7B-Instruct-v0.1']
        
        print("😱 API loaded successfully (Python1stGPT) ")
    	
    async def chat(self, prompt, history: List[Dict[str, str]]) -> str:
        async with aiohttp.ClientSession() as session:
            history += [{"role": "user", "content": prompt}]
            history = JSON.dumps(history)
            history = urllib.parse.quote(history)
            url = f"{self.base_url}?prompt={prompt}&model={self.model}&history={history}"
            async with session.get(url) as response:
                if response.status == 200:
                    json = await response.json()
                    return json["response"]
                else:
                    return f"Error code: {response.status} (most likely due to the large flow of requests but I idk)"
                    