<context>
Цель: Создать проектную документацию согласно VibeCraft V4.1 и устранить SEO-блокеры, мешающие индексации в Яндексе. 
Главная проблема: в коде зашит старый домен ai-fedor.com, что сбивает поисковых роботов.

ЗАВИСИМОСТИ: 001_extract-tech-stack (done)
ЗАТРАГИВАЕМЫЕ ФАЙЛЫ: docs/RULES.md, docs/BRIEF.md, index.html, about.html, cases.html, blog.html, sitemap.xml
ТИП: infra
</context>

<task>
1. Создать файл `docs/RULES.md` со следующим содержанием:
   "# RULES: Правила разработки 66ai.ru
   - Стек: Чистый HTML5, Tailwind CSS (CDN), Google Fonts, PHP (api/).
   - Сборка: Отсутствует. Никаких npm/node_modules.
   - Табу: Запрещено выносить стили в .css файлы. Только inline Tailwind.
   - SEO: Каждая страница должна иметь canonical на https://66ai.ru."

2. Создать файл `docs/BRIEF.md` со следующим содержанием:
   "# BRIEF: Описание проекта 66ai.ru
   Миссия: Платформа обучения Vibe Coding и ИИ-Аттестации.
   Цели: 
   1. SEO и индексация (Яндекс). 
   2. Чистота кода и скорость. 
   3. Редизайн под боли ЦА. 
   4. Кейсы и Аттестация 66AI."

3. Во ВСЕХ HTML-файлах заменить `ai-fedor.com` на `https://66ai.ru` (в canonical и og:url).
4. Добавить Open Graph теги (title, description, image, url) в `about.html` и `cases.html`.
5. Обновить `sitemap.xml`: заменить домены на https://66ai.ru и добавить страницу /blog.html.
6. ВЕРИФИКАЦИЯ: `grep -r "ai-fedor.com" .` не должен ничего находить. Файлы в docs/ должны существовать.
7. Заполнить COMPLETION LOG и перенести в tasks/done/.
</task>

<rules>
- Использовать только существующие пути к фото: `photos/robot_green_nodes.webp`.
- Исполнитель: Claude Code.
</rules>

---
## COMPLETION LOG
**Статус:** completed
**Дата завершения:** 2026-04-12
**Исполнитель:** Claude Code

### Сделано
- Создан docs/RULES.md
- Создан docs/BRIEF.md
- Заменён `ai-fedor.com` → `https://66ai.ru` во всех 4 HTML-файлах (canonical, OG, Twitter, Schema.org)
- Добавлены OG-теги (title, description, image, url, twitter:card) в about.html и cases.html
- Обновлён sitemap.xml: новый домен + добавлен blog.html

### Изменённые файлы
- `docs/RULES.md` — создан
- `docs/BRIEF.md` — создан
- `index.html` — замена домена в OG, Twitter, Schema.org
- `about.html` — замена домена + добавлены OG/Twitter теги
- `cases.html` — замена домена + добавлены OG/Twitter теги
- `blog.html` — замена домена в OG, Twitter, Schema.org
- `sitemap.xml` — новый домен + добавлен blog.html

### Верификация
- [x] `grep -r "ai-fedor.com"` — 0 совпадений в .html/.xml
- [x] docs/RULES.md существует
- [x] docs/BRIEF.md существует
- [x] OG-теги добавлены в about.html и cases.html
- [x] blog.html добавлен в sitemap.xml