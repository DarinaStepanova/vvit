from app import routes, app #импортируем маршруты, а потом app. Если бы мы сначала импортировали app, то маршруты бы не учитывались. 

if __name__ == "__main__": #если файл программа запущена самостоятельно, то фласк запускается на 8080 порте, так как 80 не у всех свободен. host="0.0.0.0" - на локальном адрессе машины
    app.run(host="0.0.0.0", port=8080)



 # Как это можно улучшить?: 1) меняем запирающую функцию(вывести в отдельный поток(паралельно работе))(может сразу несколько пользователей работать с сайтом)
 # Чтобы теперь узнать готовность распознавания, надо внедрить socket io и javascript на веб странице для того чтобы обмениваться информацией с пользователем без ее обновления(странице)(не сделано, так как никто не знает javascript)

