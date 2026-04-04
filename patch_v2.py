import re

with open('c:\\UFA\\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Header Navigation (Desktop & Mobile)
# Desktop nav:
desktop_nav = """<nav class="hidden lg:flex items-center gap-6 font-['Space_Grotesk'] font-bold uppercase tracking-tight text-[11px]">
                <a class="text-primary border-b-2 border-primary pb-1" href="index.html">НАЧАЛО</a>
                <a class="text-on-surface/70 hover:text-primary transition-all duration-300" href="index.html#process">ПРОЦЕСС</a>
                <a class="text-on-surface/70 hover:text-primary transition-all duration-300" href="index.html#program">ПРОГРАММА</a>
                <a class="text-on-surface/70 hover:text-primary transition-all duration-300" href="cases.html">КЕЙСЫ</a>
                <a class="text-on-surface/70 hover:text-primary transition-all duration-300" href="about.html">АВТОР</a>
                <a class="text-on-surface/70 hover:text-primary transition-all duration-300" href="index.html#faq">FAQ</a>
            </nav>"""
html = re.sub(r'<nav class="hidden md:flex.*?</nav>', desktop_nav, html, flags=re.DOTALL)

# Mobile bottom nav
mobile_nav = """<div class="flex justify-between items-center w-full max-w-md mx-auto px-2">
            <a class="flex flex-col items-center gap-1 text-primary" href="index.html">
                <span class="material-symbols-outlined text-[20px]" data-icon="home">home</span>
                <span class="text-[8px] font-headline font-black uppercase tracking-widest">Домой</span>
            </a>
            <a class="flex flex-col items-center gap-1 text-on-surface/60 hover:text-primary transition-colors" href="index.html#process">
                <span class="material-symbols-outlined text-[20px]" data-icon="schema">schema</span>
                <span class="text-[8px] font-headline font-black uppercase tracking-widest">Процесс</span>
            </a>
            <a class="flex flex-col items-center gap-1 text-on-surface/60 hover:text-primary transition-colors" href="index.html#program">
                <span class="material-symbols-outlined text-[20px]" data-icon="school">school</span>
                <span class="text-[8px] font-headline font-black uppercase tracking-widest">Курсы</span>
            </a>
            <a class="flex flex-col items-center gap-1 text-on-surface/60 hover:text-primary transition-colors" href="cases.html">
                <span class="material-symbols-outlined text-[20px]" data-icon="grid_view">grid_view</span>
                <span class="text-[8px] font-headline font-black uppercase tracking-widest">Кейсы</span>
            </a>
        </div>
    </div>"""
html = re.sub(r'<div class="flex justify-between items-center max-w-md mx-auto">.*?</div>\n    </div>', mobile_nav, html, flags=re.DOTALL)

# 2. Hero Section Update
hero_badge = """<p class="text-xl md:text-2xl text-on-surface-variant mb-6 font-light">Автор курса — управленец с производства, собравший ERP-систему без единой строчки кода своими руками.</p>
                        <div class="inline-flex items-center gap-2 bg-surface-container-highest px-4 py-2 rounded-lg border border-black/5 mb-6 text-sm font-bold uppercase tracking-widest text-on-surface">
                            <span class="material-symbols-outlined text-primary text-lg">account_tree</span>
                            Методология: Gemini → Claude Code → Qwen | Совет 3 Моделей
                        </div>"""
html = html.replace('<p class="text-xl md:text-2xl text-on-surface-variant mb-6 font-light">Автор курса — управленец с производства, собравший ERP-систему без единой строчки кода своими руками.</p>', hero_badge)

# 3. New Sections: Process and AI Team
process_team_sections = """
        <!-- Process Section -->
        <section class="py-24 bg-surface border-b border-black/5" id="process">
            <div class="max-w-7xl mx-auto px-8">
                <div class="text-center max-w-4xl mx-auto mb-20">
                    <h2 class="text-4xl md:text-6xl font-headline font-black text-on-surface mb-6 tracking-tighter">
                        Вы не пишете промпты.<br/><span class="text-primary italic">Вы управляете ИИ-командой.</span>
                    </h2>
                    <p class="text-xl text-on-surface-variant font-light">Большинство курсов учат подбирать слова для ChatGPT. Мы учим строить конвейер, где каждая ИИ-модель выполняет свою роль — как сотрудник в отделе.</p>
                </div>

                <!-- Conveyor scheme -->
                <div class="relative max-w-5xl mx-auto bg-surface-container-highest p-8 md:p-12 rounded-[2rem] border border-black/5 shadow-inner">
                    <div class="flex flex-col md:flex-row gap-6 md:gap-4 items-center justify-between text-center relative z-10">
                        <!-- Step 1 -->
                        <div class="flex-1 w-full flex flex-col items-center">
                            <div class="w-16 h-16 bg-white rounded-full flex items-center justify-center text-3xl shadow mb-4">💡</div>
                            <h4 class="font-black font-headline text-sm uppercase tracking-widest mb-2">ШАГ 1: ВЫ + ИДЕЯ</h4>
                            <p class="text-xs text-on-surface-variant leading-relaxed">Вы формулируете, ЧТО нужно бизнесу. Не код, не промпт — бизнес-задачу.</p>
                            <p class="text-[10px] mt-2 italic text-on-surface/50">"Мне нужен бот, который записывает клиентов"</p>
                        </div>
                        <div class="hidden md:block material-symbols-outlined text-primary/30 text-3xl">arrow_forward</div>
                        <div class="md:hidden material-symbols-outlined text-primary/30 text-3xl rotate-90">arrow_forward</div>
                        
                        <!-- Step 2 -->
                        <div class="flex-1 w-full flex flex-col items-center">
                            <div class="w-16 h-16 bg-white rounded-full flex items-center justify-center text-3xl shadow mb-4 relative">
                                📐
                                <div class="absolute -top-2 -right-6 bg-[#10B981] text-white px-2 py-0.5 rounded text-[8px] font-black uppercase shadow">Gemini Pro</div>
                            </div>
                            <h4 class="font-black font-headline text-sm uppercase tracking-widest mb-2 text-primary">Архитектор</h4>
                            <p class="text-xs text-on-surface-variant leading-relaxed">Превращает вашу идею в точное техническое задание (Task).</p>
                            <p class="text-[10px] mt-2 italic text-on-surface/50">Структурированный промпт с архитектурой</p>
                        </div>
                        <div class="hidden md:block material-symbols-outlined text-primary/30 text-3xl">arrow_forward</div>
                        <div class="md:hidden material-symbols-outlined text-primary/30 text-3xl rotate-90">arrow_forward</div>

                        <!-- Step 3 -->
                        <div class="flex-1 w-full flex flex-col items-center">
                            <div class="w-16 h-16 bg-white rounded-full flex items-center justify-center text-3xl shadow mb-4">📁</div>
                            <h4 class="font-black font-headline text-sm uppercase tracking-widest mb-2">ПАПКА «TODO»</h4>
                            <p class="text-xs text-on-surface-variant leading-relaxed">Очередь задач. Одно задание — один шаг. Никакого хаоса.</p>
                        </div>
                        <div class="hidden md:block material-symbols-outlined text-primary/30 text-3xl">arrow_forward</div>
                        <div class="md:hidden material-symbols-outlined text-primary/30 text-3xl rotate-90">arrow_forward</div>

                        <!-- Step 4 -->
                        <div class="flex-1 w-full flex flex-col items-center">
                            <div class="w-16 h-16 bg-white rounded-full flex items-center justify-center text-3xl shadow mb-4 relative">
                                ⌨️
                                <div class="absolute -top-2 -right-10 bg-primary text-white px-2 py-0.5 rounded text-[8px] font-black uppercase shadow">Claude Code Pro</div>
                            </div>
                            <h4 class="font-black font-headline text-sm uppercase tracking-widest mb-2 text-primary">Программист</h4>
                            <p class="text-xs text-on-surface-variant leading-relaxed">Выполняет ровно одно задание и перемещает его из TODO → DONE.</p>
                        </div>
                        <div class="hidden md:block material-symbols-outlined text-primary/30 text-3xl">arrow_forward</div>
                        <div class="md:hidden material-symbols-outlined text-primary/30 text-3xl rotate-90">arrow_forward</div>

                        <!-- Step 5 -->
                        <div class="flex-1 w-full flex flex-col items-center">
                            <div class="w-16 h-16 bg-white rounded-full flex items-center justify-center text-3xl shadow mb-4 relative">
                                🔍
                                <div class="absolute -top-2 -right-4 bg-tertiary text-white px-2 py-0.5 rounded text-[8px] font-black uppercase shadow">Qwen</div>
                            </div>
                            <h4 class="font-black font-headline text-sm uppercase tracking-widest mb-2 text-primary">Аудит</h4>
                            <p class="text-xs text-on-surface-variant leading-relaxed">Код проходит аудит. Qwen ищет ошибки. Claude выступает арбитром.</p>
                        </div>
                    </div>
                </div>

                <div class="mt-16 text-center">
                    <h3 class="text-2xl md:text-4xl font-headline font-black text-on-surface tracking-tighter">
                        Вы — руководитель. ИИ — ваша команда.<br/>
                        <span class="text-primary">Промпты создаёт ИИ, а не вы.</span>
                    </h3>
                </div>
            </div>
        </section>

        <!-- AI Team Section -->
        <section class="py-24 bg-surface-container-lowest border-b border-black/5" id="ai-team">
            <div class="max-w-7xl mx-auto px-8">
                <div class="text-center max-w-3xl mx-auto mb-16">
                    <h2 class="text-4xl md:text-5xl font-headline font-black text-on-surface mb-6 tracking-tighter">Три сотрудника. Чёткие роли. Ноль хаоса.</h2>
                    <p class="text-xl text-on-surface-variant font-light">Мы не используем десятки инструментов. Мы используем три ИИ-модели — каждая на своём месте.</p>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                    <!-- Архитектор -->
                    <div class="bg-surface rounded-3xl p-8 border border-black/5 shadow-sm hover:-translate-y-1 transition-transform relative">
                        <div class="absolute top-8 right-8 bg-[#10B981]/10 text-[#10B981] px-3 py-1 rounded-full text-[9px] font-black tracking-widest uppercase">Подписка Pro</div>
                        <div class="text-5xl mb-6">📐</div>
                        <h3 class="text-[10px] uppercase tracking-[0.2em] font-black opacity-50 mb-1">Gemini Pro (веб-версия)</h3>
                        <h4 class="text-3xl font-headline font-black mb-4">Архитектор</h4>
                        <p class="text-on-surface-variant text-sm mb-6 leading-relaxed flex-grow">Создаёт промпты и технические задания в идеальном формате. Думает за вас — вы только описываете, что нужно бизнесу. Архитектор переводит это в язык, который программист понимает безупречно.</p>
                        <ul class="space-y-3 text-sm text-on-surface-variant font-medium border-t border-black/5 pt-6">
                            <li class="flex items-start gap-2"><span class="material-symbols-outlined text-primary text-lg">check</span> Превращает бизнес-идею в Task</li>
                            <li class="flex items-start gap-2"><span class="material-symbols-outlined text-primary text-lg">check</span> Проектирует архитектуру</li>
                            <li class="flex items-start gap-2"><span class="material-symbols-outlined text-primary text-lg">check</span> Создаёт идеальные промпты</li>
                        </ul>
                    </div>
                    
                    <!-- Программист -->
                    <div class="bg-primary text-white rounded-3xl p-8 border border-primary/20 shadow-xl hover:-translate-y-1 transition-transform relative">
                        <div class="absolute top-8 right-8 bg-white text-primary px-3 py-1 rounded-full text-[9px] font-black tracking-widest uppercase">Финал • Подписка Pro</div>
                        <div class="text-5xl mb-6">⌨️</div>
                        <h3 class="text-[10px] uppercase tracking-[0.2em] font-black opacity-70 mb-1">Claude Code</h3>
                        <h4 class="text-3xl font-headline font-black mb-4">Программист</h4>
                        <p class="text-white/80 text-sm mb-6 leading-relaxed flex-grow">Пишет код. Только код. Выполняет одно задание за раз — берёт Task из папки TODO, делает работу, перемещает обратно. В "Совете 3 моделей" выступает финальным арбитром.</p>
                        <ul class="space-y-3 text-sm text-white/90 font-medium border-t border-white/10 pt-6">
                            <li class="flex items-start gap-2"><span class="material-symbols-outlined opacity-70 text-lg">check</span> Пишет чистый код по ТЗ</li>
                            <li class="flex items-start gap-2"><span class="material-symbols-outlined opacity-70 text-lg">check</span> Контролирует папку задач</li>
                            <li class="flex items-start gap-2"><span class="material-symbols-outlined opacity-70 text-lg">check</span> Принимает финальное решение</li>
                        </ul>
                    </div>

                    <!-- Аудитор -->
                    <div class="bg-surface rounded-3xl p-8 border border-black/5 shadow-sm hover:-translate-y-1 transition-transform relative">
                        <div class="absolute top-8 right-8 bg-black/5 text-on-surface px-3 py-1 rounded-full text-[9px] font-black tracking-widest uppercase">Бесплатная модель</div>
                        <div class="text-5xl mb-6">🔍</div>
                        <h3 class="text-[10px] uppercase tracking-[0.2em] font-black opacity-50 mb-1">Qwen Code</h3>
                        <h4 class="text-3xl font-headline font-black mb-4">Аудитор</h4>
                        <p class="text-on-surface-variant text-sm mb-6 leading-relaxed flex-grow">Проверяет работу Программиста перед финальным принятием. Ищет логические ошибки, уязвимости, несоответствия. Также подменяет Программиста, когда у Claude кончаются лимиты.</p>
                        <ul class="space-y-3 text-sm text-on-surface-variant font-medium border-t border-black/5 pt-6">
                            <li class="flex items-start gap-2"><span class="material-symbols-outlined text-primary text-lg">check</span> Аудит: логика и безопасность</li>
                            <li class="flex items-start gap-2"><span class="material-symbols-outlined text-primary text-lg">check</span> Второе независимое мнение</li>
                            <li class="flex items-start gap-2"><span class="material-symbols-outlined text-primary text-lg">check</span> Отличный резервный программист</li>
                        </ul>
                    </div>
                </div>
                <div class="text-center mt-8 text-[11px] font-bold uppercase tracking-widest text-on-surface-variant/50">
                    Резерв: Gemini CLI — запасной вариант для программирования, если Claude Code и Qwen недоступны.
                </div>
            </div>
        </section>
"""

# Replace old Program block with new Levels
program_new = """
        <!-- Program Section -->
        <section class="py-24 bg-surface border-b border-black/5" id="program">
            <div class="max-w-7xl mx-auto px-8">
                <div class="text-center max-w-4xl mx-auto mb-20">
                    <h2 class="text-4xl md:text-6xl font-headline font-black text-on-surface mb-6 tracking-tighter">4 уровня мастерства:</h2>
                    <p class="text-xl text-on-surface-variant font-light">От идеи до автономной бизнес-системы. Каждый следующий уровень включает все навыки предыдущих.</p>
                </div>
                
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                    <!-- УРОВЕНЬ 1 -->
                    <div class="bg-surface-container-lowest p-8 rounded-3xl border border-black/10 flex flex-col hover:border-primary/50 transition-all shadow-sm group">
                        <div class="flex items-center gap-4 mb-4">
                            <div class="bg-white border border-black/10 w-12 h-12 rounded-xl flex items-center justify-center text-xl shadow-sm">🎯</div>
                            <div>
                                <div class="text-[9px] uppercase tracking-widest font-black text-on-surface-variant mb-1">Уровень 1 • Белый пояс</div>
                                <h3 class="font-headline font-black text-2xl">Постановщик задач</h3>
                            </div>
                        </div>
                        <p class="text-primary font-bold mb-6 text-sm">Научитесь формулировать задачу так, чтобы ИИ понял с первого раза.</p>
                        <ul class="space-y-3 text-sm text-on-surface-variant flex-grow">
                            <li><strong class="text-on-surface">Декомпозиция:</strong> Разбиваете большую задачу на маленькие шаги — ИИ делает каждый идеально.</li>
                            <li><strong class="text-on-surface">Назначение ролей:</strong> Как нанимаете сотрудника — ставите должность и рамки.</li>
                            <li><strong class="text-on-surface">Метод примеров:</strong> Показываете ИИ образец — модель повторяет паттерн без сбоев.</li>
                        </ul>
                        <div class="mt-8 pt-4 border-t border-black/5 text-[11px] font-bold uppercase tracking-widest text-on-surface-variant">Результат: Предсказуемый код с 1 раза</div>
                    </div>

                    <!-- УРОВЕНЬ 2 -->
                    <div class="bg-[#d3e3ff] p-8 rounded-3xl border border-[#006875]/20 flex flex-col hover:shadow-lg transition-all shadow-sm group">
                        <div class="flex items-center gap-4 mb-4">
                            <div class="bg-white border border-black/10 w-12 h-12 rounded-xl flex items-center justify-center text-xl shadow-sm">🛡️</div>
                            <div>
                                <div class="text-[9px] uppercase tracking-widest font-black text-[#006875] mb-1">Уровень 2 • Синий пояс</div>
                                <h3 class="font-headline font-black text-2xl text-on-surface">Контролёр качества</h3>
                            </div>
                        </div>
                        <p class="text-[#006875] font-bold mb-6 text-sm">Научитесь не доверять ИИ на слово и получать надёжные результаты.</p>
                        <ul class="space-y-3 text-sm text-on-surface-variant flex-grow">
                            <li><strong class="text-on-surface">Совет 3 Моделей:</strong> Архитектор проектирует, Аудитор проверяет, Программист выносит решение.</li>
                            <li><strong class="text-on-surface">Самопроверка:</strong> Заставляете ИИ искать ошибки в своём же коде.</li>
                            <li><strong class="text-on-surface">Привязка к данным:</strong> Запрет на фантазии. ИИ отвечает ТОЛЬКО по вашим документам.</li>
                        </ul>
                        <div class="mt-8 pt-4 border-t border-[#006875]/20 text-[11px] font-bold uppercase tracking-widest text-[#006875]">Результат: Ноль ошибок и галлюцинаций</div>
                    </div>

                    <!-- УРОВЕНЬ 3 -->
                    <div class="bg-primary text-white p-8 rounded-3xl border border-primary-container/30 flex flex-col hover:shadow-xl transition-all shadow-lg group">
                        <div class="flex items-center gap-4 mb-4">
                            <div class="bg-white/10 border border-white/20 w-12 h-12 rounded-xl flex items-center justify-center text-xl shadow-sm">🏗️</div>
                            <div>
                                <div class="text-[9px] uppercase tracking-widest font-black text-primary-container mb-1">Уровень 3 • Бирюзовый пояс</div>
                                <h3 class="font-headline font-black text-2xl">Архитектор систем</h3>
                            </div>
                        </div>
                        <p class="text-white font-bold mb-6 text-sm opacity-90">Собираете рабочие приложения для бизнеса — как архитектор, а не программист.</p>
                        <ul class="space-y-3 text-sm text-white/80 flex-grow">
                            <li><strong class="text-white">Конвейер TODO → DONE:</strong> Task в папку → Claude выполняет → Qwen проверяет → Продакшен.</li>
                            <li><strong class="text-white">Архитектура до кода:</strong> Чертеж проекта до первого написанного файла.</li>
                            <li><strong class="text-white">Дебаггинг как ТЗ:</strong> Ошибка — не катастрофа, а просто ТЗ для починки.</li>
                        </ul>
                        <div class="mt-8 pt-4 border-t border-white/20 text-[11px] font-bold uppercase tracking-widest text-primary-container">Результат: Собранные своими руками CRM и сайты</div>
                    </div>

                    <!-- УРОВЕНЬ 4 -->
                    <div class="bg-[#191c1e] text-white p-8 rounded-3xl border border-yellow-500/30 flex flex-col hover:shadow-2xl transition-all shadow-xl group relative overflow-hidden">
                        <div class="absolute top-0 right-0 w-32 h-32 bg-yellow-500/10 blur-3xl rounded-full"></div>
                        <div class="flex items-center gap-4 mb-4 relative z-10">
                            <div class="bg-white/10 border border-yellow-500/20 w-12 h-12 rounded-xl flex items-center justify-center text-xl shadow-sm">👔</div>
                            <div>
                                <div class="text-[9px] uppercase tracking-widest font-black text-yellow-500 mb-1">Уровень 4 • Золотой пояс</div>
                                <h3 class="font-headline font-black text-2xl">Руководитель команды</h3>
                            </div>
                        </div>
                        <p class="text-yellow-400 font-bold mb-6 text-sm relative z-10">Строите автоматизации, которые работают БЕЗ вашего участия.</p>
                        <ul class="space-y-3 text-sm text-white/80 flex-grow relative z-10">
                            <li><strong class="text-white">ИИ-агенты:</strong> Сотрудники, которые сами читают почту и отвечают клиентам.</li>
                            <li><strong class="text-white">Интеграция RAG:</strong> Подключение внутренних баз данных регламентов и прайсов.</li>
                            <li><strong class="text-white">Управление памятью:</strong> Как ИИ не забывает важный контекст проекта спустя время.</li>
                        </ul>
                        <div class="mt-8 pt-4 border-t border-white/20 text-[11px] font-bold uppercase tracking-widest text-yellow-500 relative z-10">Результат: Системы работают автоматом. Вы контролируете.</div>
                    </div>
                </div>

                <div class="mt-16 text-center">
                    <button onclick="openAuditModal()" class="bg-primary text-on-primary px-10 py-5 rounded-full font-headline font-black text-sm uppercase tracking-widest hover:scale-105 transition-all shadow-xl">
                        Присоединиться к обучению
                    </button>
                </div>
            </div>
        </section>
"""

# Inject before program
idx1 = html.split('<!-- Program Section -->')[0]
idx2 = html.split('<!-- Program Section -->')[1]
idx2_after_program = idx2.split('</section>', 1)[1] # remove old program completely

html = idx1 + process_team_sections + '\n' + program_new + idx2_after_program

# 5. Add new FAQs
new_faqs = """
                    <details class="bg-surface rounded-2xl p-6 group cursor-pointer border border-black/5 [&_summary::-webkit-details-marker]:hidden">
                        <summary class="flex justify-between items-center font-headline font-black focus:outline-none">
                            Какие инструменты нужны для курса?
                            <span class="material-symbols-outlined transition-transform group-open:rotate-180 text-primary">expand_more</span>
                        </summary>
                        <p class="mt-4 text-on-surface-variant leading-relaxed font-light">Три ИИ-модели: Gemini Pro (подписка), Claude Code (подписка Pro) и Qwen Code (бесплатно). Плюс Gemini CLI как резерв. Никаких десятков приложений — минимальный стек, максимальный результат. Подробно настроим всё на первом занятии.</p>
                    </details>
                    <details class="bg-surface rounded-2xl p-6 group cursor-pointer border border-black/5 [&_summary::-webkit-details-marker]:hidden">
                        <summary class="flex justify-between items-center font-headline font-black focus:outline-none">
                            Мне нужно уметь писать промпты?
                            <span class="material-symbols-outlined transition-transform group-open:rotate-180 text-primary">expand_more</span>
                        </summary>
                        <p class="mt-4 text-on-surface-variant leading-relaxed font-light">Нет. Промпты создаёт ИИ, не вы. Вы описываете задачу человеческим языком, Архитектор (Gemini) превращает её в идеальное техническое задание, Программист (Claude Code) выполняет. Вы — руководитель, а не исполнитель.</p>
                    </details>
                    <details class="bg-surface rounded-2xl p-6 group cursor-pointer border border-black/5 [&_summary::-webkit-details-marker]:hidden">
                        <summary class="flex justify-between items-center font-headline font-black focus:outline-none">
                            Сколько стоят подписки на ИИ-инструменты?
                            <span class="material-symbols-outlined transition-transform group-open:rotate-180 text-primary">expand_more</span>
                        </summary>
                        <p class="mt-4 text-on-surface-variant leading-relaxed font-light">Gemini Pro и Claude Code Pro — платные подписки (актуальные цены на сайтах Google и Anthropic). Qwen Code — бесплатно. Суммарно это в десятки раз дешевле, чем один месяц работы программиста. Точные цены и инструкцию по оформлению дадим на старте курса.</p>
                    </details>
"""
# Replace old FAQ entries and inject new ones directly after opening div. 
faq_start = html.find('<div class="space-y-4">\n                    <details')
# Actually, the user prompts to Add these to FAQ, but wait, the prompt specifically says "В секцию FAQ добавить... Что такое Совет 3 Моделей?, Какие инструменты нужны?, и т.д."
# Since I already added "Что такое Совет..." in the last step, I'll just append these new ones.
html = html[:faq_start+24] + new_faqs + html[faq_start+24:]


with open('c:\\UFA\\index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Patch v2 applied successfully.")
