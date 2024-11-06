<p align="center">
  <img width="180" src="./public/ChatGPT.png" alt="ChatGPT">
  <p align="center"><b>Бесплатная обёртка для ИИ моделей</b></p>
</p>

<p align="center"><strong>Разработано и написано <a href="https://github.com/python1st-code">@python1st</a></strong></p>

<div id="top"></div>

> [!IMPORTANT]
> Этот репозиторий предоставляет доступ к не официальному варианту ChatGPT. Использование этого репозитория полностью на ваш страх и риск. Автор не несет никакой ответственности за любые последствия, связанные с использованием, форками или модификациями этого кода.

```sh
git clone https://github.com/python1st-code/Python1stGPT.git
```

<p align="center"><strong>Примеры использования</strong></p>

```python
from Python1stGPT import Python1stGPT

gpt = Python1stGPT('gpt-4o-mini') # Создаем класс
print(gpt.models) # Список доступных моделей ИИ

answer = await gpt.chat("Сообщение к ИИ", [
        {"role": "user",
        "content": "Сообщение к ИИ в памяти"}
    ]
) # Генерируем ответ на наше сообщение

print(answer) # Получаем ответ
```

