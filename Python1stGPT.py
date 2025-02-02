import json
from enum import Enum
from typing import ClassVar, cast

from aiohttp import ClientSession


class Model(Enum):
    """Model enum."""

    GPT4O_MINI = "gpt-4o-mini"
    CLAUDE_3_HAIKU = "claude-3-haiku-20240307"
    LLAMA_3_70B = "meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo"
    MIXTRAL_8X7B = "mistralai/Mixtral-8x7B-Instruct-v0.1"


class Python1stGPT:
    """Python1stGPT class."""

    base_url: ClassVar[str] = "https://duck.gpt-api.workers.dev/chat/"

    def __init__(self, model: Model = Model.GPT4O_MINI) -> None:
        self.model: Model = model

    async def chat(self, prompt: str, history: list[dict[str, str]]) -> str:
        async with ClientSession() as session:
            response = await session.get(
                self.base_url,
                params={
                    "prompt": prompt,
                    "model": self.model.value,
                    "history": json.dumps(history),
                },
            )
            json_resp: dict[str, str] = await response.json()
            return cast(str, json_resp["response"])
