# GIT

1. [Sourse](#source)
2. [Content](#content)

## <a name="source">Source</a>

link: https://www.youtube.com/watch?v=zZBiln_2FhM


## <a name="content">Content</a>

Проверить, установлен ли Git на устройстве:
```python
$ git --version
```

Показать, какие есть команды:
```python
$ git --help
```

Показать список текущих дирикторий:
```python
$ dir
```

Перейти в папку:
```python
$ cd <folder_name>
```

Инициализировтаь репозиторий:
```python
$ git init
```

После инициализации создается папка .git. В данной папке будет записываться вся техническая информация, необходимая для контроля версий.
После создания файла проекта с кодом необходимо сообщить Git, что создан новый файл, чтобы Git его зафиксировал.

Выяснить статус Git:
```python
$ git status
```

Git имеет ветки, которые представляют собой версии проекта.

Начать отслеживать файл:
```python
$ git add <name>
```

Начать отслеживать все файлы:
```python
$ git add .
```

Если в файл были внесены изменения после того, как мы выполнили команду git add, нужно снова выполнять данную команду

Перестать отслеживать файл:
```python
$ git rm --cached <file>
```

После команды git add следует выполнить команду захвата изменений:
```python
$ git commit -m 'message of commmit'
```

После commit мы получаем сообщение, в котором указан, в том числе, уникальный хеш коммита, к которому потом можно будет возвращаться:

![image.png](attachment:image.png)

Если у нас есть файлы, которые не должны попалать в систему контроля версий.<br/>
Для этого требуется создать в корне папки, где выполнен, init файл '.gitignore'<br/>
В .gitignore мы прописываем все, что хотим заигнорить.<br/>
При этом файл .gitignore нужно добавить в систему контроля версий: 
```python
$ git add .gitignore
```

Для того, чтобы Git начал игнорировать папку, нужно в файле .gitignore указать через слеш:
```python
$ /folder
```

По умолчанию мы находимся в ветке master:

![image.png](attachment:image.png)

Узнать текущую ветку и список все веток:
```python
$ git branch
```

Создать новую ветку:
```python
$ git branch <name_branch>
```

Удалить ветку:
```python
$ git branch -D <name_branch>
```

Изменить ветку:
```python
$ git checkout <name_branch>
```

Создать новую ветку и сразу же на нее переколючиться:
```python
$ git checkout -b <name_branch>
```

Совместить ветки на локальном репозитории:
```python
$ git merge <name_branch>
```

При выполнении данной команды в активную ветку будут добавлены изменения, имеющиеся в ветке <name_branch>

Показать значение user:
```python
$ git config --global user.name
```

Изменить значение user:
```python
$ git config --global user.name <new_user>
```

Показать / изменить значение email:
```python
$ git config --global user.email <new_email>
```

Связать локаьлный репозиторий и удаленный:
```python
$ git remote add origin <full link to repository>
```

Залить из локального репозитория в удаленный:
```python
$ git push -u origin <active branch_name>
```

Залить на GitHub:
```python
$ git push
```

Клонировать удаленный репозиторий в локальный:
```python
$ git clone <full link to GitGun repository>
```

Слить изменения из удаленного репозитория в локальный:
```python
$ git fetch
```

Применить изменения из удаленного репозитория в локальный после выполненной команды $ git fetch:
```python
$ git merge
```

Применить изменения удаленного репозитория к локальному:
```python
$ git pull
```