# Загрузка и публикация изображений Nasa и Spacex в канал Telegram
 

## Обзор 

Этот проект содержит несколько скриптов, предназначенных для загрузки космических изображений от *Nasa* и *SpaceX* и их публикации в *Telegram-канале*. Он использует официальные *API* для получения изображений от NASA's Astronomy Picture of the Day (APOD), Earth Polychromatic Imaging Camera (EPIC) и последних запусков SpaceX. Полученные изображения сохраняются локально и могут быть запланированы для публикации в Telegram-канале через регулярные интервалы.

## Как использовать

__Клонировать репозиторий:__

```python
git clone https://github.com/Rokyl59/download_space_photo.git
```

__Установите зависимости:__

Убедитесь, что в вашей системе установлен Python 3. Используйте `pip` (или `pip3`) для установки необходимых зависимостей:

```python
pip install -r requirements.txt
```

__Получение токена Telegram:__

Чтобы использовать скрипт, вам понадобится персональный токен telegram. Чтобы его получить:

* Напишите [отцу ботов](https://t.me/BotFather) .

__Получение токена Nasa:__

Чтобы использовать скрипт, вам понадобится персональный токен Nasa. Чтобы его получить:

* Зарегистрируйтесь или войдите в свой аккаунт на [Nasa](https://api.nasa.gov/) .

__Настройка окружения:__

Создайте файл `.env` в корневом каталоге скрипта и добавьте в него следующую строку:

```
NASA_API_KEY=ВашТокен
TELEGRAM_TOKEN_API=ВашТокен
```

* Замените `ВашТокен` на ваш фактический токен Nasa.

* Замените `ВашТокен` на ваш фактический токен Telegram.


## Использование

__Загрузка и хранение изображений:__

1. Изображения *NASA Astronomy Picture of the Day(APOD)*

```python
python get_apod_images.py
```

По умолчанию скрипт загружает последние 30 изображений APOD. Вы можете изменить количество в скрипте при необходимости.

2. Изображения *NASA Earth Polychromatic Imaging Camera (EPIC)*

```python
python fetch_epic_images.py
```

Скрипт по умолчанию загружает последние 10 изображений EPIC.

3. Изображения запусков *SpaceX*

```python
python fetch_spacex_launch_images.py [--launch_id id_запуска]
```

Без указания `--launch_id` скрипт загружает изображения с последнего запуска SpaceX.

## Публикация изображений в *Telegram*

Запустите следующую команду для начала публикации фотографий в вашем Telegram-канале:

```python
python publish_photos.py --directory images --interval 4
```
Замените `images` на путь к директории, содержащей фотографии, которые вы хотите опубликовать. Опция `--interval` задает интервал между публикациями в часах (по умолчанию 4 часа).

## Примечания

* Убедитесь, что в директории, указанной для публикации фотографий, содержатся только файлы изображений.

* Скрипты создадут директорию с именем `images` в папке вашего проекта для хранения загруженных изображений.

* Вам необходимо добавить вашего бота *Telegram* в качестве администратора в ваш канал, чтобы он мог публиковать фотографии.

* Используйте `Ctrl + C` для остановки скрипта, который публикует фотографии в *Telegram*.









