# ENVIRONMENT: Окружение проекта 66ai.ru

## Фреймворк
Отсутствует. Чистый HTML5 без JavaScript-фреймворков. Каждая страница — самодостаточный HTML-документ.

## Зависимости
| Зависимость | Тип | URL |
|---|---|---|
| Tailwind CSS | CDN | `https://cdn.tailwindcss.com?plugins=forms,container-queries` |
| Google Fonts (Space Grotesk) | CDN | `https://fonts.googleapis.com/css2?family=Space+Grotesk` |
| Google Fonts (Manrope) | CDN | `https://fonts.googleapis.com/css2?family=Manrope` |
| Google Fonts (Inter) | CDN | `https://fonts.googleapis.com/css2?family=Inter` |
| Google Fonts (Playfair Display) | CDN | `https://fonts.googleapis.com/css2?family=Playfair+Display` |
| Material Symbols | CDN | `https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined` |

## Команды запуска
Сборка **не требуется**. Сайт открывается напрямую:
- Через браузер: открыть `index.html` двойным кликом
- Через Live Server (VS Code): расширение «Live Server», правый клик → `Open with Live Server`
- Через PHP-сервер: `php -S localhost:8000` (для работы `/api/` скриптов)

## Структура проекта
```
66ai/
├── index.html              # Главная страница
├── about.html              # Об авторе
├── cases.html              # Кейсы
├── blog.html               # Блог
├── attestation.html        # Страница аттестации 66AI
├── design-preview.html     # Дизайн-превью (Индиго)
├── design-option-1.html    # Вариант 1 — Эдиториал
├── design-option-2.html    # Вариант 2 — Индиго
├── design-option-3.html    # Вариант 3 — Арктика
├── robots.txt              # SEO: правила индексации
├── sitemap.xml             # SEO: карта сайта
├── .gitignore              # Git: исключённые файлы
│
├── api/                    # Бэкенд (PHP)
│   ├── config.php.example  # Шаблон конфига Telegram
│   └── send-lead.php       # Отправка лидов в Telegram
│
├── photos/                 # Изображения
│   ├── robot_green_nodes.webp
│   └── ...
│
├── docs/                   # Документация (VibeCraft V4.1)
│   ├── BRIEF.md
│   ├── RULES.md
│   ├── ENVIRONMENT.md
│   ├── BOOT.md
│   ├── LESSONS.md
│   ├── USER_RESEARCH.md
│   ├── CURRENT_STACK.md
│   └── adr/
│       └── ADR-001_attestation-system.md
│
└── tasks/                  # Задачи
    ├── todo/
    └── done/
```

## Операционная система разработки
- ОС: Windows (win32)
- Редактор: VS Code / Qwen Code / Claude Code
- Git: репозиторий с удалённым `origin/main`

## Конфигурационные файлы
- `.gitignore` — исключает `.env`, `api/config.php`, `.vscode/`, `*.py`, `Analiz.pdf`
- `api/config.php` — хранит токен Telegram-бота и chat_id (в `.gitignore`)
