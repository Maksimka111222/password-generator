# Лабораторна робота 02. Налаштування середовища розробки та Git workflow

ПІБ: Сєнко Володимир Павлович
Група: ІПЗ-22
Роль у команді: developer, QA
Репозиторій: [https://github.com/Maksimka111222/password-generator](https://github.com/Maksimka111222/password-generator)

## Команда

| Учасник | GitHub | Роль | Модуль |
|---|---|---|---|
| Maksym Khomych | @Maksimka111222 | team lead, developer | CLI (`src/cli.py`), CHANGELOG, реліз |
| Diana Zhuk | @dirolssis | developer | генератор паролів (`src/generator.py`), виправлення помилки |
| Volodymyr Sienko | @VEivon | developer, QA | перевірка надійності пароля (`src/strength.py`), unit-тести |

Проєкт: консольна утиліта для генерації паролів з налаштовуваною довжиною та наборами символів.

## Особистий внесок

### Гілки

Гілки видалялися після злиття, тому посилання ведуть на Pull Request кожної гілки.
`назва-гілки-PR11` (перевірка надійності пароля), [PR #11](https://github.com/Maksimka111222/password-generator/pull/11)
`назва-гілки-PR13` (unit-тести), [PR #13](https://github.com/Maksimka111222/password-generator/pull/13)
 docs/report-Volodymyr (цей звіт)

Я реалізував перевірку надійності пароля (`feat: password strength checker`) і написав unit-тести. Тести запускав на Windows через Git Bash командою py -m unittest discover.

### Pull Request

[#11](https://github.com/Maksimka111222/password-generator/pull/11) feat: password strength checker, Merged
[#13](https://github.com/Maksimka111222/password-generator/pull/13) назва PR з тестами, Merged
 Review: [#N назва PR](https://github.com/Maksimka111222/password-generator/pull/N), Approved

### Коміти

[`хеш`](https://github.com/Maksimka111222/password-generator/commit/хеш) повідомлення коміту
[`хеш`](https://github.com/Maksimka111222/password-generator/commit/хеш) повідомлення коміту

## Конфлікт злиття

Конфлікт виник у файл при злитті гілка A та гілка B: обидві змінювали який рядок. Я відкрив файл у VS Code, у блоці <<<<<<< обрав Accept Both / Incoming / Current, зберіг і зробив коміт. Якщо скріни з тренувального відтворення, напиши: «Скріншоти зроблено на тренувальному відтворенні конфлікту».

![Конфлікт у VS Code](screenshots/12a-conflict.png)
![Розв'язаний конфлікт](screenshots/12b-resolved.png)

## Робота у VS Code

Коміт, зміни у вкладці Source Control і перемикання гілки я виконав через VS Code.

![Source Control: зміни](screenshots/09-vscode-changes.png)
![Коміт](screenshots/10-vscode-commit.png)
![Перемикання гілки](screenshots/11-vscode-branch.png)

## Issues і реліз

- Issue [#N назва](https://github.com/Maksimka111222/password-generator/issues/N), закритий через PR #M
- Issue [#N назва](https://github.com/Maksimka111222/password-generator/issues/N), закритий через PR зі звітом (`Closes #N`)
- Реліз: [https://github.com/Maksimka111222/password-generator/releases/tag/v1.0.0](https://github.com/Maksimka111222/password-generator/releases/tag/v1.0.0). Тег v1.0.0 стоїть на коміті fa61392.

![Закриті Issues](screenshots/06-issues-closed.png)
![Мій Issue, закритий через PR](screenshots/07-my-issue.png)
![Реліз v1.0.0](screenshots/08-release.png)

## Результати перевірки

![Тести](screenshots/01-tests.png)
![Історія комітів main](screenshots/02-git-log.png)
![Мої коміти](screenshots/03-my-commits.png)
![Усі злиті Pull Request](screenshots/04-prs-closed.png)
![Мій Pull Request з review](screenshots/05-my-pr.png)
![PR #11](screenshots/05b-pr11.png)
![PR #13](screenshots/05c-pr13.png)

## Висновки

2–3 речення: чому навчився, що було складним.