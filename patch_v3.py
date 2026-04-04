import re

with open('c:\\UFA\\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Hero Badges
old_hero_badge = """<div class="inline-flex items-center gap-2 bg-surface-container-highest px-4 py-2 rounded-lg border border-black/5 mb-6 text-sm font-bold uppercase tracking-widest text-on-surface">
                            <span class="material-symbols-outlined text-primary text-lg">account_tree</span>
                            Методология: Gemini → Claude Code → Qwen | Совет 3 Моделей
                        </div>"""
new_hero_badges = """<div class="flex flex-wrap gap-2 mb-6">
                            <span class="bg-surface-container-highest border border-black/10 px-3 py-1.5 rounded-full text-[10px] font-black uppercase tracking-widest text-[#10B981]">Gemini Pro</span>
                            <span class="bg-surface-container-highest border border-black/10 px-3 py-1.5 rounded-full text-[10px] font-black uppercase tracking-widest text-primary">Claude Code</span>
                            <span class="bg-surface-container-highest border border-black/10 px-3 py-1.5 rounded-full text-[10px] font-black uppercase tracking-widest text-tertiary">Совет 3 Моделей</span>
                        </div>"""

if old_hero_badge in html:
    html = html.replace(old_hero_badge, new_hero_badges)
else:
    # Just in case there's whitespace difference
    html = re.sub(r'<div class="inline-flex items-center gap-2 bg-surface-container-highest.*?Совет 3 Моделей\s*</div>', new_hero_badges, html, flags=re.DOTALL)

# 2. Update Flow Step 2
html = re.sub(
    r'<h3 class="font-headline font-black text-xl mb-3">ИИ создаёт решение</h3>\s*<p class="text-sm text-on-surface-variant">Cursor и Claude генерируют рабочий код бизнес-приложения.</p>',
    '<h3 class="font-headline font-black text-xl mb-3">ИИ создаёт решение</h3>\n                        <p class="text-sm text-on-surface-variant">Gemini проектирует, Claude Code реализует.</p>',
    html
)

# 3. Remove sections: methodology, process, ai-team, program
def remove_section(html_content, section_id):
    pattern = r'<section[^>]*?id="' + section_id + r'"[^>]*>.*?</section>'
    return re.sub(pattern, '', html_content, flags=re.DOTALL)

html = remove_section(html, 'methodology')
html = remove_section(html, 'process')
html = remove_section(html, 'ai-team')
html = remove_section(html, 'program')


# 4. Inject Process and AI Team between solution and cases
# We need to find the end of `solution` section and insert there.
new_process_ai_team = """
        <!-- Process Section -->
        <section class="py-24 bg-surface-container-lowest border-b border-black/5" id="process">
            <div class="max-w-7xl mx-auto px-8">
                <div class="text-center max-w-4xl mx-auto mb-16">
                    <h2 class="text-4xl md:text-5xl font-headline font-black text-on-surface mb-6 tracking-tighter">
                        Вы не пишете промпты.<br/><span class="text-primary italic">Вы управляете ИИ-командой.</span>
                    </h2>
                    <p class="text-xl text-on-surface-variant font-light">У вас будет три ИИ-сотрудника с чёткими ролями. Вы — руководитель.</p>
                </div>

                <!-- Conveyor scheme -->
                <div class="relative max-w-6xl mx-auto">
                    <div class="flex flex-col md:flex-row gap-4 items-center justify-between text-center relative z-10">
                        <!-- Step 1 -->
                        <div class="flex-1 w-full bg-surface p-6 rounded-2xl border border-black/5 hover:-translate-y-1 transition-transform relative text-center">
                            <div class="text-4xl mb-4">💡</div>
                            <h4 class="font-black font-headline text-[10px] uppercase tracking-widest mb-2 opacity-50">ШАГ 1</h4>
                            <h3 class="font-black text-sm uppercase tracking-widest mb-3">ВЫ + ИДЕЯ</h3>
                            <p class="text-xs text-on-surface-variant leading-relaxed">Описываете задачу обычными словами</p>
                        </div>
                        <div class="hidden md:block material-symbols-outlined text-primary/30 text-2xl">arrow_forward</div>
                        <div class="md:hidden material-symbols-outlined text-primary/30 text-2xl rotate-90">arrow_forward</div>
                        
                        <!-- Step 2 -->
                        <div class="flex-1 w-full bg-surface p-6 rounded-2xl border border-black/5 hover:-translate-y-1 transition-transform relative text-center">
                            <div class="absolute -top-3 left-1/2 -translate-x-1/2 bg-[#10B981] text-white px-3 py-1 rounded-full text-[8px] font-black uppercase shadow tracking-widest whitespace-nowrap">Gemini Pro</div>
                            <div class="text-4xl mb-4 mt-2">📐</div>
                            <h4 class="font-black font-headline text-[10px] uppercase tracking-widest mb-2 opacity-50">ШАГ 2</h4>
                            <h3 class="font-black text-sm uppercase tracking-widest mb-3 text-primary">АРХИТЕКТОР</h3>
                            <p class="text-xs text-on-surface-variant leading-relaxed">Превращает идею в точное техзадание</p>
                        </div>
                        <div class="hidden md:block material-symbols-outlined text-primary/30 text-2xl">arrow_forward</div>
                        <div class="md:hidden material-symbols-outlined text-primary/30 text-2xl rotate-90">arrow_forward</div>

                        <!-- Step 3 -->
                        <div class="flex-1 w-full bg-surface p-6 rounded-2xl border border-black/5 hover:-translate-y-1 transition-transform relative text-center">
                            <div class="text-4xl mb-4">📁</div>
                            <h4 class="font-black font-headline text-[10px] uppercase tracking-widest mb-2 opacity-50">ШАГ 3</h4>
                            <h3 class="font-black text-sm uppercase tracking-widest mb-3">ЗАДАНИЕ → TODO</h3>
                            <p class="text-xs text-on-surface-variant leading-relaxed">Один шаг — одна задача</p>
                        </div>
                        <div class="hidden md:block material-symbols-outlined text-primary/30 text-2xl">arrow_forward</div>
                        <div class="md:hidden material-symbols-outlined text-primary/30 text-2xl rotate-90">arrow_forward</div>

                        <!-- Step 4 -->
                        <div class="flex-1 w-full bg-surface p-6 rounded-2xl border border-black/5 hover:-translate-y-1 transition-transform relative text-center">
                            <div class="absolute -top-3 left-1/2 -translate-x-1/2 bg-primary text-white px-3 py-1 rounded-full text-[8px] font-black uppercase shadow tracking-widest whitespace-nowrap">Claude Code</div>
                            <div class="text-4xl mb-4 mt-2">⌨️</div>
                            <h4 class="font-black font-headline text-[10px] uppercase tracking-widest mb-2 opacity-50">ШАГ 4</h4>
                            <h3 class="font-black text-sm uppercase tracking-widest mb-3 text-primary">ПРОГРАММИСТ</h3>
                            <p class="text-xs text-on-surface-variant leading-relaxed">Выполняет задание → перемещает в DONE</p>
                        </div>
                        <div class="hidden md:block material-symbols-outlined text-primary/30 text-2xl">arrow_forward</div>
                        <div class="md:hidden material-symbols-outlined text-primary/30 text-2xl rotate-90">arrow_forward</div>

                        <!-- Step 5 -->
                        <div class="flex-1 w-full bg-surface p-6 rounded-2xl border border-black/5 hover:-translate-y-1 transition-transform relative text-center">
                            <div class="absolute -top-3 left-1/2 -translate-x-1/2 bg-tertiary text-white px-3 py-1 rounded-full text-[8px] font-black uppercase shadow tracking-widest whitespace-nowrap">Совет 3 Моделей</div>
                            <div class="text-4xl mb-4 mt-2">🛡️</div>
                            <h4 class="font-black font-headline text-[10px] uppercase tracking-widest mb-2 opacity-50">ШАГ 5</h4>
                            <h3 class="font-black text-sm uppercase tracking-widest mb-3 text-primary">АУДИТ</h3>
                            <p class="text-xs text-on-surface-variant leading-relaxed">Перекрёстная проверка перед запуском</p>
                        </div>
                    </div>
                </div>

                <div class="mt-16 text-center">
                    <div class="text-2xl md:text-3xl font-headline font-black text-on-surface tracking-tighter uppercase">
                        Промпты создаёт ИИ. Код пишет ИИ. Вы — руководите.
                    </div>
                </div>
            </div>
        </section>

        <!-- AI Team Section -->
        <section class="py-24 bg-surface border-b border-black/5" id="ai-team">
            <div class="max-w-7xl mx-auto px-8">
                <div class="text-center max-w-3xl mx-auto mb-16">
                    <h2 class="text-4xl md:text-5xl font-headline font-black text-on-surface mb-4 tracking-tighter">Три сотрудника. Чёткие роли. Минимальный стек.</h2>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                    <!-- Архитектор -->
                    <div class="bg-surface-container-lowest rounded-3xl p-8 border border-black/5 hover:-translate-y-1 transition-transform">
                        <div class="text-5xl mb-4">📐</div>
                        <h4 class="text-xl font-headline font-black mb-1">АРХИТЕКТОР</h4>
                        <p class="text-xs font-bold text-[#10B981] uppercase tracking-widest mb-4">Gemini Pro</p>
                        <p class="text-on-surface-variant text-sm leading-relaxed">Проектирует решения и создаёт задания для программиста</p>
                    </div>
                    
                    <!-- Программист -->
                    <div class="bg-primary text-white rounded-3xl p-8 border border-primary/20 hover:-translate-y-1 transition-transform relative">
                        <div class="absolute top-8 right-8 bg-white/20 text-white px-3 py-1 rounded-full text-[9px] font-black tracking-widest uppercase">Финальный арбитр</div>
                        <div class="text-5xl mb-4">⌨️</div>
                        <h4 class="text-xl font-headline font-black mb-1">ПРОГРАММИСТ</h4>
                        <p class="text-xs font-bold text-white/50 uppercase tracking-widest mb-4">Claude Code Pro</p>
                        <p class="text-white/80 text-sm leading-relaxed">Пишет код и принимает финальные решения</p>
                    </div>

                    <!-- Аудитор -->
                    <div class="bg-surface-container-lowest rounded-3xl p-8 border border-black/5 hover:-translate-y-1 transition-transform relative">
                        <div class="absolute top-8 right-8 bg-black/5 text-on-surface px-3 py-1 rounded-full text-[9px] font-black tracking-widest uppercase">Бесплатно</div>
                        <div class="text-5xl mb-4">🔍</div>
                        <h4 class="text-xl font-headline font-black mb-1">АУДИТОР</h4>
                        <p class="text-xs font-bold text-tertiary uppercase tracking-widest mb-4">Qwen Code</p>
                        <p class="text-on-surface-variant text-sm leading-relaxed">Проверяет результат и страхует при исчерпании лимитов</p>
                    </div>
                </div>
                <div class="text-center mt-12 text-[11px] font-bold uppercase tracking-widest text-on-surface-variant/50">
                    Резерв: Gemini CLI. Никаких десятков приложений — три инструмента и чёткая методология.
                </div>
            </div>
        </section>
"""

html = re.sub(
    r'(</section>\s*)(<!-- Cases Section -->\s*<section[^>]*id="cases")',
    r'\1' + new_process_ai_team + r'\n\n        \2',
    html
)


# 5. Inject Program section effectively right before flow section. Wait, program should be AFTER cases, where the old one was.
# The old one was between "Cases" and "Flow".
new_program = """
        <!-- Program Section (v5) -->
        <section class="py-24 bg-surface border-b border-black/5" id="program">
            <div class="max-w-7xl mx-auto px-8">
                <div class="text-center max-w-4xl mx-auto mb-20">
                    <h2 class="text-4xl md:text-6xl font-headline font-black text-on-surface mb-6 tracking-tighter">Три ступени к результату</h2>
                    <p class="text-xl text-on-surface-variant font-light">От первого бота за выходные — до системы, которая работает без вас.</p>
                </div>
                
                <div class="grid grid-cols-1 md:grid-cols-3 gap-8 items-start">
                    <!-- Ступень 1 -->
                    <div class="bg-surface-container-lowest p-8 rounded-3xl border border-black/5 flex flex-col hover:border-primary/50 transition-all shadow-sm">
                        <div class="inline-flex items-center justify-center bg-black/5 px-3 py-1 rounded-full text-[9px] font-black uppercase tracking-widest text-on-surface-variant mb-6 w-max">Быстрый старт • 2 дня</div>
                        <h3 class="font-headline font-black text-2xl mb-4">ИИ-Конвейер за выходные</h3>
                        <p class="text-sm text-on-surface-variant mb-6">Настраиваете свою ИИ-команду (Gemini + Claude Code + Qwen), осваиваете конвейер и собираете первый рабочий инструмент для бизнеса — Telegram-бот или мини-сайт.</p>
                        
                        <div class="bg-surface p-4 rounded-xl mb-8">
                            <p class="text-[10px] uppercase font-black text-primary mb-2">ВАШ РЕЗУЛЬТАТ:</p>
                            <ul class="text-xs space-y-2 font-medium">
                                <li>— Рабочий стек ИИ-инструментов</li>
                                <li>— Первый продукт для вашего бизнеса</li>
                                <li>— Понимание: «это реально, я могу»</li>
                            </ul>
                        </div>
                        
                        <div class="mt-auto pt-6 border-t border-black/5">
                            <p class="text-xs text-on-surface-variant mb-4">Формат: скринкасты + текстовые гайды + чат поддержки 2 недели</p>
                            <p class="text-3xl font-black text-on-surface mb-6">4 990 ₽</p>
                            <button onclick="openAuditModal()" class="w-full bg-surface-container-highest border border-black/10 text-on-surface hover:bg-black/5 py-4 rounded-full font-bold uppercase text-xs tracking-widest transition-colors">Начать за 4 990 ₽</button>
                        </div>
                    </div>

                    <!-- Ступень 2 Флагман -->
                    <div class="bg-primary text-white p-8 md:p-10 rounded-3xl border border-primary-container/30 flex flex-col shadow-2xl relative md:-translate-y-6 z-10">
                        <div class="absolute -top-4 left-1/2 -translate-x-1/2 bg-[#10B981] text-white px-4 py-1.5 rounded-full text-[9px] font-black uppercase tracking-widest whitespace-nowrap shadow-md">Флагманский курс • 4 недели • Малая группа</div>
                        <h3 class="font-headline font-black text-3xl mb-4 mt-2">Бизнес-инженер</h3>
                        <p class="text-sm text-white/80 mb-6 font-light">Полный путь от бизнес-задачи до работающей системы. CRM, дашборды, боты, автоматизации — конкретно для ВАШЕГО бизнеса. Авторская методология: «Совет 3 Моделей», конвейер TODO→DONE, управление ИИ-командой.</p>
                        
                        <div class="space-y-3 mb-8">
                            <div class="bg-white/10 p-3 rounded-lg border border-white/5">
                                <p class="text-[10px] font-black uppercase text-primary-container mb-1">Уровень 1 — «Постановщик задач»</p>
                                <p class="text-xs text-white/90">Результат: ставите задачу ИИ и получаете результат с первого раза</p>
                            </div>
                            <div class="bg-white/10 p-3 rounded-lg border border-white/5">
                                <p class="text-[10px] font-black uppercase text-primary-container mb-1">Уровень 2 — «Контролёр качества»</p>
                                <p class="text-xs text-white/90">Результат: выявляете ошибки ИИ, получаете надёжный результат</p>
                            </div>
                            <div class="bg-white/10 p-3 rounded-lg border border-white/5">
                                <p class="text-[10px] font-black uppercase text-primary-container mb-1">Уровень 3 — «Архитектор систем»</p>
                                <p class="text-xs text-white/90">Результат: собираете рабочее приложение для бизнеса</p>
                            </div>
                            <div class="bg-white/10 p-3 rounded-lg border border-white/5">
                                <p class="text-[10px] font-black uppercase text-primary-container mb-1">Уровень 4 — «Руководитель ИИ-команды»</p>
                                <p class="text-xs text-white/90">Результат: автоматизации работают без вашего контроля</p>
                            </div>
                        </div>

                        <div class="mt-auto pt-6 border-t border-white/10">
                            <p class="text-xs text-white/70 mb-4">Формат: скринкасты + живые эфиры + текстовые гайды + чат</p>
                            <p class="text-3xl font-black text-white mb-6">от 19 900 ₽</p>
                            <button onclick="openAuditModal()" class="w-full bg-white text-primary hover:bg-surface py-4 rounded-full font-bold uppercase text-xs tracking-widest transition-colors shadow">Записаться на курс</button>
                        </div>
                    </div>

                    <!-- Ступень 3 -->
                    <div class="bg-surface-container-lowest p-8 rounded-3xl border border-black/5 flex flex-col hover:border-black/20 transition-all shadow-sm">
                        <div class="inline-flex items-center justify-center bg-black/5 px-3 py-1 rounded-full text-[9px] font-black uppercase tracking-widest text-on-surface-variant mb-6 w-max">Индивидуально</div>
                        <h3 class="font-headline font-black text-2xl mb-4">Персональный консалтинг</h3>
                        <p class="text-sm text-on-surface-variant mb-6">Аудит ваших процессов + совместная сборка системы. Результат быстрее, фокус на вашем бизнесе.</p>
                        
                        <div class="mt-auto pt-6 border-t border-black/5 flex flex-col h-full justify-end">
                            <p class="text-3xl font-black text-on-surface mb-6">По запросу</p>
                            <button onclick="openAuditModal()" class="w-full bg-black/5 text-on-surface hover:bg-black/10 py-4 rounded-full font-bold uppercase text-xs tracking-widest transition-colors">Обсудить задачу</button>
                        </div>
                    </div>
                </div>
            </div>
        </section>
"""

# Insert program right before flow
html = re.sub(
    r'(</section>\s*)(<!-- Flow Section -->)',
    r'\1' + new_program + r'\n\n        \2',
    html
)

# 6. Update FAQ
# We replace the entire `<div class="space-y-4"> ... </div>` inside the FAQ section.
new_faqs = """<div class="space-y-4">
                    <details class="bg-surface rounded-2xl p-6 group cursor-pointer border border-black/5 [&_summary::-webkit-details-marker]:hidden">
                        <summary class="flex justify-between items-center font-headline font-black focus:outline-none">
                            Какие инструменты нужны?
                            <span class="material-symbols-outlined transition-transform group-open:rotate-180 text-primary">expand_more</span>
                        </summary>
                        <p class="mt-4 text-on-surface-variant leading-relaxed font-light">Три ИИ-модели: Gemini Pro, Claude Code Pro и Qwen Code (бесплатно). Настроим всё на первом занятии. Никаких десятков приложений.</p>
                    </details>
                    <details class="bg-surface rounded-2xl p-6 group cursor-pointer border border-black/5 [&_summary::-webkit-details-marker]:hidden">
                        <summary class="flex justify-between items-center font-headline font-black focus:outline-none">
                            Мне нужно уметь писать промпты?
                            <span class="material-symbols-outlined transition-transform group-open:rotate-180 text-primary">expand_more</span>
                        </summary>
                        <p class="mt-4 text-on-surface-variant leading-relaxed font-light">Нет. В нашей методологии промпты создаёт ИИ, а не вы. Вы описываете задачу словами, Архитектор превращает её в техзадание, Программист выполняет. Вы — руководитель.</p>
                    </details>
                    <details class="bg-surface rounded-2xl p-6 group cursor-pointer border border-black/5 [&_summary::-webkit-details-marker]:hidden">
                        <summary class="flex justify-between items-center font-headline font-black focus:outline-none">
                            Что такое "Совет 3 Моделей"?
                            <span class="material-symbols-outlined transition-transform group-open:rotate-180 text-primary">expand_more</span>
                        </summary>
                        <p class="mt-4 text-on-surface-variant leading-relaxed font-light">Авторская методика перекрёстной проверки. Три ИИ-модели проверяют работу друг друга — вместо слепого доверия одной нейросети. Подробно разбираем на курсе.</p>
                    </details>
                    <details class="bg-surface rounded-2xl p-6 group cursor-pointer border border-black/5 [&_summary::-webkit-details-marker]:hidden">
                        <summary class="flex justify-between items-center font-headline font-black focus:outline-none">
                            Сколько стоят подписки на инструменты?
                            <span class="material-symbols-outlined transition-transform group-open:rotate-180 text-primary">expand_more</span>
                        </summary>
                        <p class="mt-4 text-on-surface-variant leading-relaxed font-light">Gemini Pro и Claude Code — платные подписки. Qwen — бесплатно. Суммарно в десятки раз дешевле одного месяца работы программиста. Точные цены и инструкцию дадим на старте.</p>
                    </details>
                    <details class="bg-surface rounded-2xl p-6 group cursor-pointer border border-black/5 [&_summary::-webkit-details-marker]:hidden">
                        <summary class="flex justify-between items-center font-headline font-black focus:outline-none">
                            Чем это отличается от других курсов по Vibe Coding?
                            <span class="material-symbols-outlined transition-transform group-open:rotate-180 text-primary">expand_more</span>
                        </summary>
                        <p class="mt-4 text-on-surface-variant leading-relaxed font-light">Другие курсы учат нажимать кнопки в Cursor. Мы учим управлять ИИ-командой по строгой методологии — с разделением ролей, конвейером задач и перекрёстным контролем качества. Автор — управленец, который собрал ERP для реального производства, а не блогер.</p>
                    </details>
                </div>"""
html = re.sub(r'<div class="space-y-4">.*?</div>\s*</div>\s*</section>', new_faqs + '\n            </div>\n        </section>', html, flags=re.DOTALL)

with open('c:\\UFA\\index.html', 'w', encoding='utf-8') as f:
    f.write(html)


# Update footer dates in all files
for file_name in ['index.html', 'cases.html', 'about.html']:
    with open('c:\\UFA\\' + file_name, 'r', encoding='utf-8') as f:
        file_html = f.read()
    file_html = re.sub(r'© 2024–2025 Дядя Фёдор', '© 2025 Дядя Фёдор', file_html)
    file_html = re.sub(r'© 2024 Дядя Фёдор', '© 2025 Дядя Фёдор', file_html)
    with open('c:\\UFA\\' + file_name, 'w', encoding='utf-8') as f:
        f.write(file_html)

print("Patch v3 applied.")
