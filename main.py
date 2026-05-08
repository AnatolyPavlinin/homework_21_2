import urllib.parse  # Для декодирования POST-данных
from http.server import BaseHTTPRequestHandler, HTTPServer

# Для начала определим настройки запуска
hostName = "localhost"  # Адрес для доступа по сети
serverPort = 8080  # Порт для доступа по сети


class MyServer(BaseHTTPRequestHandler):
    """
    Специальный класс, который отвечает за
    обработку входящих запросов от клиентов
    """

    def do_GET(self):
        """Метод для обработки входящих GET-запросов"""

        # Читаем содержимое HTML-файла
        with open("contacts.html", "r", encoding="utf-8") as file:
            html_content = file.read()

        # Отправляем ответ
        self.send_response(200)  # Отправка кода ответа
        self.send_header("Content-type", "text/html")  # Тип данных: HTML
        self.end_headers()  # Завершение формирования заголовков ответа
        self.wfile.write(html_content.encode())  # Отправляем содержимое HTML-файла

    def do_POST(self):
        """Метод для обработки входящих POST-запросов"""

        # Получаем длину тела запроса (указана в заголовке Content-Length)
        content_length = int(self.headers["Content-Length"])

        # Читаем тело запроса (данные формы)
        post_data = self.rfile.read(content_length)

        # Декодируем данные формы (обычно приходят в формате application/x-www-form-urlencoded)
        parsed_post_data = urllib.parse.parse_qs(post_data.decode("utf-8"))

        # Печать принятых данных в консоль
        print("\nПриняты данные POST-запроса:")
        for key, value in parsed_post_data.items():
            print(f"{key}: {value[0]}")

        # Отправляем ответ клиенту (например, успешное сообщение)
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write("Данные успешно получены!".encode("utf-8"))


if __name__ == "__main__":
    # Инициализация веб-сервера
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print(f"Server started http://{hostName}:{serverPort}")

    try:
        # Запускаем сервер в бесконечном цикле
        webServer.serve_forever()
    except KeyboardInterrupt:
        # Остановка сервера по сочетанию клавиш Ctrl+C
        pass

    # Остановка сервера и освобождение ресурсов
    webServer.server_close()
    print("Server stopped.")
