# RULES: Правила разработки 66ai.ru

## 1. Стек
Чистый HTML5, Tailwind CSS (через CDN без сборки), Google Fonts, PHP для `/api`.

## 2. Архитектура
Проект является статическим HTML-сайтом (SPA-подобный). Каждая страница — самодостаточный `.html` файл с inline Tailwind-конфигурацией. Сборка не требуется, npm/node_modules отсутствуют.

## 3. Структура страниц
- `<head>` содержит: meta charset, viewport, description, OG-теги, Twitter Cards, canonical, Schema.org JSON-LD
- `<header>` — навигация с мобильным меню (гамбургер)
- `<main>` — основной контент
- `<footer>` — подвал с копирайтом
- Tailwind-конфиг inline через `<script id="tailwind-config">`

## 4. Стилизация
- Tailwind CSS подключается через CDN: `https://cdn.tailwindcss.com?plugins=forms,container-queries`
- Все стили — через Tailwind-классы и inline `<style>` для кастомных анимаций
- Кастомная палитра определяется в `tailwind.config.theme.extend.colors`

## 5. СТРОГИЕ ТАБУ
1. **Никакого английского текста в UI-интерфейсе.** Все заголовки, кнопки, подписи — строго на русском. Исключение: бренд «VibeCraft», названия технологий, классы CSS.
2. **Запрет на чистый `#000000` и `#FFFFFF`.** Использовать только приглушённые оттенки: графит `#0F172A`, кремовый `#F5F0E6` и т.д.
3. **Запрет на изменение базовой светлой кремовой палитры сайта без приказа.** Если требуется тёмная тема — она указывается явно через `class="dark"` на `<html>`.
4. **Запрет на вынос стилей в `.css` файлы.** Только inline Tailwind и `<style>` в `<head>`.
5. **Никакого «AI-слопа».** Запрещены фиолетовые светящиеся нейросети, дешёвые градиенты, шаблонные «AI-картинки».

## 6. SEO-правила
- Каждая страница обязана иметь `<link rel="canonical" href="https://66ai.ru/..." />`
- OG-теги (`og:url`, `og:title`, `og:description`, `og:image`) — на каждой странице
- Twitter Cards (`twitter:card`, `twitter:title`, `twitter:image`) — на каждой странице
- `robots.txt` и `sitemap.xml` поддерживаются в актуальном состоянии
- Schema.org JSON-LD размещается на релевантных страницах

## 7. Именование файлов
- HTML-страницы: `kebab-case.html` (например, `about.html`, `design-option-1.html`)
- API-скрипты: `kebab-case.php` (например, `send-lead.php`)
- Изображения: `kebab-case.webp` (предпочтительно) или `.png`, `.jpg`
- Документация: `UPPER_SNAKE_CASE.md` или `adr/ADR-XXX_name.md`

## 8. Контекстные правила
- Проект является статическим HTML — **сборка не требуется**
- Нет `package.json`, `node_modules`, `webpack`, `vite`
- Деплой: прямая загрузка файлов на сервер
- Мобильная навигация: фиксированная нижняя панель (до 767px)
- Десктопная навигация: горизонтальное меню в header

## 9. Работа с задачами
- Каждая задача — файл в `tasks/todo/` с контекстом, описанием, правилами и COMPLETION LOG
- После выполнения: заполнить лог, перенести файл в `tasks/done/`
- ADR (Architecture Decision Records) хранятся в `docs/adr/`

## 10. Коммиты и Git
- После завершения задачи: `git add -A`, `git commit`, `git push origin main`
- Сообщения коммитов — на русском, краткие, по существу
- Формат: `<тип>: <описание>` (feat, docs, infra, ui, fix)
