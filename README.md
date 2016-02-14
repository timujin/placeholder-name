# Список фич для MVP

Пользователи - идентификация, аутентификация с помощью соцсетей.
Создание предсказания - текст, оценка, дата наступления (?), статус приватности.
Создание оценки или комментария для предсказания.
Установление статуса наступления (right/wrong/unknown).
Просмотр предсказания.
Просмотр всех публичных предсказаний.
Просмотр всех своих предсказаний.
Share предсказания.
Просмотр графика своей личной точности.

# Сущности базы данных

Пользователь - я не знаю, как работает аутентификация по соцсетям и что и как нам здесь нужно хранить.
Предсказание - текст, дата создания, дата наступления, статус наступления, статус приватности, автор, безопасный id/токен.
Оценка - автор, связанное предсказание, дата, величина, комментарий.

# API

Работа с пользователем - я не знаю, как работает аутентификация с помощью соцсетей, как должны выглядеть конкретные функции и как API будет узнавать пользователя - надо изучать.
GET предсказание кратко: id => текст, автор, дата.
GET предсказание полно: id => полные данные по предсказанию, включая список оценок.
GET публичные предсказания: какая-нибудь пагинация или сортировка => список кратких предсказаний.
GET предсказания пользователя: какая-нибудь пагинация или сортировка => список кратких предсказаний.
GET график пользователя: "пожалуйста" => список датапоинтов.
POST предсказания: полные данные предсказания => id нового предсказания.
POST оценки-комментария: полные данные оценки => OK.
POST статуса завершенности: предсказание, новый статус => OK.


# Нерешенные вопросы:

Термины. Надо установить строгие термины для предсказания, оценки, right\wrong\unknown (на predictionbook небольшой срачик, что эти термины не самые лучшие).
Какие используем соцсети?
Дата наступления - может, ее в MVP не будет? Если она есть, то придется еще пилить всякие нотификешоны там. Пусть каждое предсказание будет "до востребования"?
Как мы безопасно реализуем расшаривание предсказаний?
График мы храним и обновляем, или пересчитываем, когда просят?
Комментарий и оценка - одна сущность, как в predictionbook, или разные?
Название?
