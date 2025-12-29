from datetime import datetime


def create_logger(name:str, enable:bool=True):

    history_list = []

    def log(level: str, message: str, **meta):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        string_type = f'{timestamp} | NAME:{name} {level} | {message} | '
        for key, value in meta.items():
            string_type += f'{key}:{value} '
        history_list.append(string_type)
        if enable==True:
            print(string_type)


    def info(message: str, **meta):
        log("INFO", message, **meta)

    def warning(message:str, **meta):
         log("WARNING", message, **meta)

    def error(message:str, **meta):
        log("ERROR", message, **meta)

    def get_history():
        return history_list[:]           # возвращаем копию списка
    
    return {
        "info": info,
        "warning": warning,
        "error": error,
        "get_history": get_history
    }

log = create_logger(name="ShopApp", enable=True)

log['info']("Пользователь вошёл", user_id=123, ip="192.168.1.10")
log['warning']("Корзина почти полная", items_count=98)
log['info']("Добавлен товар", product="Телефон", price=50000)
log['error']("Не удалось подключиться к БД", error="Connection timeout")

print("\nИстория логов:")
for entry in log['get_history']():
    print(entry)
