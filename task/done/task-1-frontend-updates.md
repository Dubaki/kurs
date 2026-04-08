<task_prompt>
  <task_objective>
    Выполнить серию точечных обновлений пользовательского интерфейса (UI), контента и анимаций в файлах index.html, cases.html и about.html на основе новых требований к дизайну.
  </task_objective>

  <technical_context>
    - Стек: HTML5, Tailwind CSS (через CDN), нативный JavaScript.
    - Дизайн-система: Утилитарные классы Tailwind. 
    - Важно не сломать мобильную адаптивность (классы md:, lg:).
  </technical_context>

  <files_to_modify>
    <file>index.html</file>
    <file>cases.html</file>
    <file>about.html</file>
  </files_to_modify>

  <step_by_step_instructions>
    <step target="index.html" section="Hero Section">
      <action>Поменять местами фото и текст на главной странице.</action>
      <details>
        В блоке `grid-cols-1 lg:grid-cols-12` перемести `div` с фотографией (сейчас он справа, `lg:col-span-5`) так, чтобы он был первым в DOM, а текст (`lg:col-span-7`) — вторым. Это визуально поместит фото слева, а текст справа на десктопе.
      </details>
    </step>
    
    <step target="index.html" section="Hero Section Photo">
      <action>Обновить путь к фото и изменить форму анимированной рамки.</action>
      <details>
        1. Измени путь картинки на `ufa/photos/b1.webp`.
        2. Сейчас вокруг фото крутится круглая рамка (`rounded-full`). Измени классы обертки картинки и самой рамки с `rounded-full` на `rounded-2xl` (или `rounded-none`, если нужен жесткий квадрат), чтобы анимация представляла собой вращающийся квадрат. Сохрани эффект `animate-[spin_20s_linear_infinite]`.
      </details>
    </step>

    <step target="index.html" section="Typewriter Script">
      <action>Настроить печатный текст "себя" / "сотрудников".</action>
      <details>
        1. В HTML убери класс `border-b-2` и `border-primary` у элемента `<span id="typewriter-hero">`. У слов не должно быть подчеркивания.
        2. В JavaScript массиве `heroWords` напиши слова с маленькой буквы: `['себя', 'сотрудников']`. Алгоритм печати и стирания текста должен остаться плавным и без изменений логики.
      </details>
    </step>

    <step target="index.html" section="Solution Section (Интерфейс ERP)">
      <action>Обновить картинку ERP и убрать обрезку.</action>
      <details>
        1. Измени путь картинки на `ufa/photos/erp1.jpg`.
        2. Замени класс `object-cover` у картинки на `object-contain`, чтобы интерфейс отображался целиком, без обрезки по краям. 
        3. Убери жесткий `aspect-[4/3]`, если он мешает полному отображению пропорций картинки.
        4. Добавь картинке атрибут `onclick` для открытия на весь экран (например, используй нативный Dialog/модальное окно, аналогично `audit-modal`, чтобы по клику картинка увеличивалась).
      </details>
    </step>

    <step target="cases.html" section="Modals">
      <action>Оптимизировать модальные окна кейсов и убрать лишние скриншоты.</action>
      <details>
        1. Сделай все модальные окна компактнее: уменьши внутренние отступы (например, `p-8 lg:p-12` на `p-6 lg:p-8`), уменьши `margin-bottom` у заголовков и параграфов, чтобы избежать необходимости скроллить контент вниз.
        2. Внутри `id="case-data-1"` измени текст: "Экономия более 1.5 млн рублей" на "Экономия более 1 млн рублей".
        3. Внутри `id="case-data-2"` (Сайт ремонта) очисти содержимое внутри `<div class="media" data-type="image">...</div>`. Скриншота там быть не должно, достаточно существующей ссылки.
        4. Внутри `id="case-data-3"` (Сайт VibeCraft) аналогично полностью очисти содержимое `<div class="media" data-type="image">...</div>`.
      </details>
    </step>

    <step target="about.html" section="Author Robot Photo">
      <action>Изменить анимацию робота и убрать заднюю декоративную рамку.</action>
      <details>
        1. Удали декоративный элемент под фото: `<div class="absolute -z-10 top-10 -right-10 w-full h-full border-2 border-primary/20 rounded-3xl"></div>`.
        2. Удали класс `group-hover:-translate-y-2` (зум/приближение при наведении) с обертки фотографии.
        3. Настрой "включение света" при наведении: у самого тега `<img>` (робота) добавь классы `transition-all duration-500`. По умолчанию оставь `grayscale opacity-80 mix-blend-multiply`, но при наведении (`group-hover`) сделай `group-hover:grayscale-0 group-hover:opacity-100 group-hover:mix-blend-normal`. Это создаст эффект включения цвета и свечения планшета/лампочек.
      </details>
    </step>
  </step_by_step_instructions>

  <constraints>
    - Не удалять и не ломать существующую логику модального окна `case-modal`.
    - Сохранить все классы Tailwind, отвечающие за цвета (primary, on-surface и т.д.).
    - Выполнить задачи строго по шагам и отчитаться о завершении и перенеси файл в папку done из todo.
  </constraints>
</task_prompt>