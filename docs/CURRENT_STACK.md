# Текущий стек проекта 66ai.ru (ai-fedor.com)

## Стек технологий

### Тип проекта
**Статический HTML-сайт (SPA без фреймворка)** — чистый HTML/CSS/JS, без сборщиков и бандлеров. Каждая страница — отдельный `.html` файл.

### Фронтенд
| Категория | Технология | Детали |
|---|---|---|
| **Фреймворк** | Отсутствует | Чистый HTML5, без React/Vue/Next.js и т.д. |
| **Стилизация** | Tailwind CSS (CDN) | Подключается через `<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries">` |
| **Tailwind конфиг** | Inline | В каждом HTML-файле есть `<script id="tailwind-config">` с `tailwind.config = { darkMode: "class", theme: { extend: { ... } } }` |
| **Шрифты** | Google Fonts | Space Grotesk (300-900), Manrope (300-800) |
| **Иконки** | Google Material Symbols | `<link>` к `fonts.googleapis.com/css2?family=Material+Symbols+Outlined` |
| **Тема** | Светлая/тёмная | Переключение через CSS-класс `.light` / `.dark` на `<html>` |
| **Язык** | Русский | `lang="ru"` на всех страницах |

### Бэкенд
| Категория | Технология | Детали |
|---|---|---|
| **Язык** | PHP | Простые скрипты без фреймворка |
| **Функционал** | Отправка лидов в Telegram | `api/send-lead.php` — принимает JSON, отправляет сообщение через Telegram Bot API |
| **Конфигурация** | `api/config.php` | Возвращает массив с `bot_token` и `chat_id` (файл в `.gitignore`, есть `.example`) |
| **CORS** | Разрешён всем | `Access-Control-Allow-Origin: *` |

### Инструменты сборки
**Отсутствуют.** Нет `package.json`, `node_modules`, `Vite`, `Webpack`, `npm`/`yarn`. Сайт деплоится как набор статических файлов напрямую на сервер.

### Система управления контентом (CMS)
**Отсутствует.** Нет WordPress, нет headless CMS. Контент захардкожен в HTML.

---

## Структура папок

```
C:\66ai\
├── .gitignore                    # Исключает .env, api/config.php, .vscode, *.py, Analiz.pdf
├── index.html                    # Главная страница (лендинг, ~1346 строк)
├── about.html                    # Страница "Об авторе" (~229 строк)
├── cases.html                    # Страница кейсов (~379 строк)
├── blog.html                     # Страница блога (~312 строк)
├── robots.txt                    # SEO: разрешает всё, указывает sitemap
├── sitemap.xml                   # SEO: 3 URL (/, about.html, cases.html)
├── zen_*.html                    # Верификационный файл (Яндекс/Дзен)
│
├── api/
│   ├── config.php.example        # Шаблон конфига Telegram-бота
│   └── send-lead.php             # Эндпоинт отправки лидов в Telegram
│
├── photos/
│   ├── ERP1.jpg
│   ├── ph1.webp
│   ├── robot_green_nodes.png
│   └── robot_green_nodes.webp
│
├── .agents/workflows/            # Внутренние файлы Qwen/Claude
├── .claude/settings.local.json   # Локальные настройки Claude
├── .github/workflows/            # GitHub Actions (если есть)
├── .qwen/                        # Настройки Qwen Code
├── .vscode/                      # Настройки VS Code (в .gitignore)
│
├── tasks/
│   ├── done/
│   └── todo/
│
└── docs/                         # <-- Эта директория (документация)
```

### Описание страниц
| Файл | Назначение | SEO-мета |
|---|---|---|
| `index.html` | Главный лендинг, курсы по Vibe Coding | description, OG, Twitter Cards, Schema.org (Course), canonical |
| `about.html` | Биография автора | description, canonical |
| `cases.html` | Кейсы (ERP, ремонт, лендинг) | description, canonical |
| `blog.html` | Блог об ИИ и автоматизации | description, OG, Twitter Cards, canonical |

---

## SEO-статус

### ✅ Есть
- **robots.txt** — корректный, разрешает индексацию всего, указывает sitemap
- **sitemap.xml** — валидный XML, содержит 3 URL с приоритетами и частотой обновления
- **meta description** — есть на всех 4 страницах
- **Open Graph** — есть на `index.html` и `blog.html` (type, url, title, description, image)
- **Twitter Cards** — есть на `index.html` и `blog.html` (summary_large_image)
- **Canonical URL** — есть на всех страницах
- **Schema.org** — JSON-LD разметка `Course` на главной странице
- **OG image** — `robot_green_nodes.webp` (есть также `.png` версия)

### ⚠️ Проблемы
- **OG-теги отсутствуют** на `about.html` и `cases.html` — при шеринге в соцсетях может не быть превью
- **sitemap.xml не включает** `blog.html` — страница блога не индексируется через sitemap
- **Нет noindex/nofollow** — все страницы открыты для индексации (это корректно для продакшена)
- **Домен в мета-тегах** — `ai-fedor.com`, а проект упоминается как `66ai.ru` — возможна путаница, если это разные домены

### 🔍 Рекомендации по SEO
1. Добавить OG-теги на `about.html` и `cases.html`
2. Добавить `blog.html` в `sitemap.xml`
3. Проверить, что `66ai.ru` и `ai-fedor.com` — это один домен (или настроить редирект)
4. Рассмотреть добавление Schema.org разметки на другие страницы (About, BlogArticle)

---

## Рекомендации по развитию проекта

### Краткосрочные
1. **Вынести Tailwind конфиг** в отдельный файл `tailwind.config.js` для избежания дублирования между страницами
2. **Создать общий layout-компонент** — сейчас head/meta/script дублируются в каждом файле
3. **Добавить favicon** — отсутствует в `<head>`
4. **Добавить страницу 404** — `404.html`

### Среднесрочные
5. **Рассмотреть переход на SSG** (Astro, Next.js SSG, Eleventy) — даст переиспользование компонентов, автоматическую генерацию sitemap, оптимизацию изобраений
6. **Оптимизировать изображения** — использовать `<picture>` с `srcset`, lazy loading
7. **Добавить CI/CD** — автоматическую валидацию HTML, проверку ссылок
8. **Добавить аналитику** — Яндекс.Метрика, Google Analytics

### Долгосрочные
9. **Если планируется блог** — рассмотреть CMS (headless: Strapi, Sanity, Decap CMS) или генерацию из Markdown
10. **Если нужна авторизация/оплата** — потребуется бэкенд-фреймворк или serverless-функции

---

## COMPLETION LOG

**Статус:** completed
**Дата завершения:** 2026-04-12
**Исполнитель:** Claude Code (Программист)

### Сделано
- Проанализирована корневая директория проекта
- Изучены все 4 HTML-страницы (index, about, cases, blog)
- Изучены API-файлы (send-lead.php, config.php.example)
- Проверены SEO-файлы (robots.txt, sitemap.xml)
- Проверены мета-теги на всех страницах
- Определён стек: чистый HTML + Tailwind CDN + Google Fonts + PHP (Telegram bot)
- Создан файл `docs/CURRENT_STACK.md`

### Изменённые файлы
- `docs/CURRENT_STACK.md` — создан

### Верификация
- [x] Аудит проведен
- [x] Файл docs/CURRENT_STACK.md создан и заполнен
- [x] Содержит разделы: "Стек", "Структура папок", "SEO-статус", "Рекомендации"

### Побочные эффекты / риски
- Рисков нет. Аудит выполнен в режиме Read-Only, код сайта не изменён.

### Открытые вопросы
- `66ai.ru` и `ai-fedor.com` — это один домен или разные? Нужно уточнить у заказчика.
- Планируется ли расширение блога? Если да — стоит сразу考虑 переход на SSG/CMS.
