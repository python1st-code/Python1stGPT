<p align="center">
  <img width="180" src="./public/ChatGPT.png" alt="ChatGPT">
  <p align="center"><b>Бесплатная обёртка для ИИ моделей</b></p>
</p>

<div id="top"></div>

> [!IMPORTANT]
> Этот репозиторий предоставляет доступ к не официальным вариантам ИИ моделей. Использование этого репозитория полностью на ваш страх и риск. Автор не несет никакой ответственности за любые последствия, связанные с использованием, форками или модификациями этого кода.

```sh
git clone https://github.com/python1st-code/Python1stGPT.git
```

<p align="center"><strong>Примеры использования</strong></p>

```python
import asyncio

from Python1stGPT import Python1stGPT, Model

gpt = Python1stGPT(Model.GPT4O_MINI) # Создаем инстанс

async def main() -> None:
    answer = await gpt.chat("Сообщение к ИИ", [{
                "role": "user",
                "content": "Сообщение к ИИ в памяти"
        }]
    ) # Генерируем ответ на наше сообщение

    print(answer) # Получаем ответ

if __name__ == "__main__":
    asyncio.run(main())

```

