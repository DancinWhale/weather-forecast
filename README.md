<h1>Weather forecast web application</h1>
<div>Это небольшое приложение позволяет проверить ближайшую погоду в интересующим пользователя городе.</div>
<h3>Функции</h3>
<ul>
  <li>Вывод прогноза погоды для введенного города</li>
  <li>Сохранение истории поиска для каждого пользователя</li>
</ul>
<h3>Использованный стек</h3>
<ul>
  <li>FastAPI - веб-фреймворк на Python</li>
  <li>Datetime - библиотека для получения времени пользователя</li>
  <li>Requests - библиотека для выполнения HTTP-запросов</li>
  <li>pytest - для тестирования</li>
  <li>HTML, Jinja2, CSS и его фреймворк Bootstrap - для отрисовки фронтенда</li>
</ul>
<h3>Запуск приложения</h3>
<ol>
  <li>Клонируйте репозиторий<br>
  <code>https://github.com/DancinWhale/weather-forecast.git</code>
  </li>
  <li>
    Создайте виртуальное окружение и активируйте его: <br><code>python -m venv venv</code><br> <code>source venv/bin/activate  # Для Windows: venv\Scripts\activate</code>
  </li>
  <li>
    Установите все необходимое:<br>
    <code>pip install fastapi[all] pytest pytest-asyncio</code>
  </li>
  <li>Запустите приложение:<br>
    <code>uvicorn app.main:app --reload  # Если вы уже в папке app: uvicorn main:app --reload</code>
  </li>
  <li>В вашем браузере откройте ссылку: http://127.0.0.1:8000</li>
</ol>
