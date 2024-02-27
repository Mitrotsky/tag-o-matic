# О проекте

Короче, это небольшой скрипт, суть которого в том что он пробегает по списку файлов и создаёт записи в JSON-файле. 
В JSON-файле не так много данных, лишь теги, обозначение "безопасно для работы" и наименование файла, как у любого предмета искусства.
Создано для минимальной категоризации и не требует визуального редактора.

Да, код написан ужасно, я это знаю. 

# Как использовать

Перед запуском вам нужно убедиться, что пути указаны верно. В gallery_directory укажите путь на вашу категорию, а в data_file - JSON-файл, в который и будет вестись запись. 
Если всё было сделано успешно, то JSON-файл будет заполнен перечнем всех файлов, находившихся в директории gallery_directory, готовым шаблоном и проставленными индексами.
Для взаимодействия с записями используются команды:

***edit \<index>*** - переходит к редактированию существующей записи в удобном формате диалога через терминал. Здесь вы вводите все те данные, которые не выставлены автоматически. Сохранение происходит только после полного завершения функции. В случае прерывания ничего не изменяется.

***find \<\*tags\>*** - выводит на экран индексы, наименования файла, название в системе и его теги, если данная запись содержит введённые теги. Теги вводятся через пробел. Если тегов нет, выводит в терминал все записи. Если тег не имеет совпадений, выводит перенос строки.

***open \<index\>*** - открывает файл с соответствующим индексом в стандартном для вашей системы приложении. Например, в случае изображений на "чистой" системе это будет системная галерея.

***show*** - выводит на экран все записи, имеющиеся в JSON-файле. Не принимает аргументов, игнорирует их если таковые вводятся.

***nsfw \<true|false\>*** - переключает отображение небезопасного для работы (NSFW) контента.

***help*** - выводит на экран краткое, но исчерпывающее описание данных команд. 

***exit*** - завершает работу программы.
