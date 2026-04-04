import re

def update_footer(html):
    html = re.sub(r'© 2024 Дядя Фёдор', r'© 2024–2025 Дядя Фёдор', html)
    return html

def update_nav(html):
    # Desktop nav
    html = re.sub(r'<nav class="hidden md:flex items-center gap-8 font-\[\'Space_Grotesk\'\] font-bold uppercase tracking-tight">.*?</nav>',
                  r'<nav class="hidden md:flex items-center gap-8 font-[\'Space_Grotesk\'] font-bold uppercase tracking-tight">\n                <a class="text-on-surface/70 hover:text-primary transition-all duration-300" href="index.html">НАЧАЛО</a>\n                <a class="text-on-surface/70 hover:text-primary transition-all duration-300" href="index.html#program">ПРОГРАММА</a>\n                <a class="text-on-surface/70 hover:text-primary transition-all duration-300" href="cases.html">КЕЙСЫ</a>\n                <a class="text-on-surface/70 hover:text-primary transition-all duration-300" href="about.html">АВТОР</a>\n            </nav>',
                  html, flags=re.DOTALL)
    # Mobile nav
    html = re.sub(r'<div class="flex justify-between items-center max-w-md mx-auto">.*?</div>\n    </div>',
                  r'<div class="flex justify-between items-center max-w-md mx-auto">\n            <a class="flex flex-col items-center gap-1 text-on-surface/60 hover:text-primary transition-colors" href="index.html">\n                <span class="material-symbols-outlined" data-icon="home">home</span>\n                <span class="text-[10px] font-headline font-black uppercase tracking-widest">Домой</span>\n            </a>\n            <a class="flex flex-col items-center gap-1 text-on-surface/60 hover:text-primary transition-colors" href="index.html#program">\n                <span class="material-symbols-outlined" data-icon="school">school</span>\n                <span class="text-[10px] font-headline font-black uppercase tracking-widest">Курсы</span>\n            </a>\n            <a class="flex flex-col items-center gap-1 text-on-surface/60 hover:text-primary transition-colors" href="cases.html">\n                <span class="material-symbols-outlined" data-icon="grid_view">grid_view</span>\n                <span class="text-[10px] font-headline font-black uppercase tracking-widest">Кейсы</span>\n            </a>\n            <a class="flex flex-col items-center gap-1 text-on-surface/60 hover:text-primary transition-colors" href="about.html">\n                <span class="material-symbols-outlined" data-icon="person">person</span>\n                <span class="text-[10px] font-headline font-black uppercase tracking-widest">Автор</span>\n            </a>\n        </div>\n    </div>',
                  html, flags=re.DOTALL)
                  
    # For cases and about page, we should apply an active class.
    # We will do this manually for those.
    return html

# ----------------- #
#  PROCESS INDEX.HTML
# ----------------- #
with open('c:\\UFA\\index.html', 'r', encoding='utf-8') as f:
    idx = f.read()

idx = update_footer(idx)
idx = update_nav(idx)

# Active desktop nav for index.html
idx = idx.replace('<a class="text-on-surface/70 hover:text-primary transition-all duration-300" href="index.html">НАЧАЛО</a>', '<a class="text-primary border-b-2 border-primary pb-1" href="index.html">НАЧАЛО</a>', 1)

# Active mobile nav for index.html
idx = idx.replace('<a class="flex flex-col items-center gap-1 text-on-surface/60 hover:text-primary transition-colors" href="index.html">', '<a class="flex flex-col items-center gap-1 text-primary" href="index.html">', 1)


# Remove BOT_TOKEN completely
idx = re.sub(r'// ─── BOT CONFIG ──────────────────────────────────────────────.*?const CHAT_ID\s*=\s*5930269100;', '', idx, flags=re.DOTALL)

# Add Social Proof
social_proof = """
        <!-- Social Proof Section -->
        <section class="py-12 bg-primary text-white border-y border-black/10 relative overflow-hidden">
            <div class="absolute inset-0 z-0 opacity-10 mix-blend-overlay"></div>
            <div class="max-w-7xl mx-auto px-8 relative z-10">
                <div class="grid grid-cols-2 md:grid-cols-4 gap-8 text-center divide-x divide-white/20">
                    <div>
                        <div class="text-4xl md:text-5xl font-black font-headline mb-2">3</div>
                        <div class="text-[10px] font-bold uppercase tracking-widest opacity-80">проекта собрано</div>
                    </div>
                    <div>
                        <div class="text-4xl md:text-5xl font-black font-headline mb-2">0 ₽</div>
                        <div class="text-[10px] font-bold uppercase tracking-widest opacity-80">на программистов</div>
                    </div>
                    <div>
                        <div class="text-4xl md:text-5xl font-black font-headline mb-2">20</div>
                        <div class="text-[10px] font-bold uppercase tracking-widest opacity-80">человек на производстве</div>
                    </div>
                    <div>
                        <div class="text-4xl md:text-5xl font-black font-headline mb-2">4</div>
                        <div class="text-[10px] font-bold uppercase tracking-widest opacity-80">недели до результата</div>
                    </div>
                </div>
            </div>
        </section>
"""
# Insert social_proof right before <!-- Flow Section -->
idx = idx.replace('<!-- Flow Section -->', social_proof + '\n        <!-- Flow Section -->')

# Add Methodology
methodology = """
        <!-- Methodology Section -->
        <section class="py-24 bg-surface border-b border-black/5" id="methodology">
            <div class="max-w-7xl mx-auto px-8">
                <div class="text-center max-w-4xl mx-auto mb-16">
                    <h2 class="text-3xl md:text-5xl font-headline font-black text-on-surface leading-tight mb-6 tracking-tighter">
                        Не просто Vibe Coding — а <span class="text-primary italic">инженерное мышление</span>
                    </h2>
                    <p class="text-xl text-on-surface-variant font-light">Мы учим не нажимать кнопки, а управлять ИИ на профессиональном уровне. Вот методологии, которые вы освоите.</p>
                </div>
                
                <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
                    <!-- ГРУППА 1 -->
                    <div>
                        <h3 class="text-[10px] font-black text-primary uppercase tracking-[0.2em] mb-6 flex items-center gap-2"><span class="material-symbols-outlined text-lg">psychology</span> Как заставить ИИ думать глубже</h3>
                        <div class="space-y-4">
                            <div class="bg-surface-container-highest p-6 rounded-2xl border border-black/5 hover:border-primary/30 transition-all hover:-translate-y-1 group">
                                <h4 class="font-headline font-black text-lg mb-2 group-hover:text-primary transition-colors">Role Prompting</h4>
                                <p class="text-sm text-on-surface-variant leading-relaxed">Задание модели конкретной роли. Меняет угол зрения и качество ответов.</p>
                            </div>
                            <div class="bg-surface-container-highest p-6 rounded-2xl border border-black/5 hover:border-primary/30 transition-all hover:-translate-y-1 group">
                                <h4 class="font-headline font-black text-lg mb-2 group-hover:text-primary transition-colors">Few-Shot Learning</h4>
                                <p class="text-sm text-on-surface-variant leading-relaxed">Обучение в промпте. Показываете примеры — модель повторяет паттерн.</p>
                            </div>
                            <div class="bg-surface-container-highest p-6 rounded-2xl border border-black/5 hover:border-primary/30 transition-all hover:-translate-y-1 group">
                                <h4 class="font-headline font-black text-lg mb-2 group-hover:text-primary transition-colors">Chain-of-Thought</h4>
                                <p class="text-sm text-on-surface-variant leading-relaxed">Цепочка рассуждений. Заставляет ИИ выводить промежуточные шаги для решения сложных задач.</p>
                            </div>
                            <div class="bg-surface-container-highest p-6 rounded-2xl border border-black/5 hover:border-primary/30 transition-all hover:-translate-y-1 group">
                                <h4 class="font-headline font-black text-lg mb-2 group-hover:text-primary transition-colors">Prompt Chaining & ReAct</h4>
                                <p class="text-sm text-on-surface-variant leading-relaxed">Разбиение задачи на конвейер и вызов внешних действий (поиск, API).</p>
                            </div>
                        </div>
                    </div>
                    
                    <!-- ГРУППА 2 -->
                    <div>
                        <h3 class="text-[10px] font-black text-primary uppercase tracking-[0.2em] mb-6 flex items-center gap-2"><span class="material-symbols-outlined text-lg">fact_check</span> Как не дать ИИ врать</h3>
                        <div class="space-y-4">
                            <div class="bg-surface-container-highest p-6 rounded-2xl border border-black/5 hover:border-primary/30 transition-all hover:-translate-y-1 group">
                                <h4 class="font-headline font-black text-lg mb-2 group-hover:text-primary transition-colors">Context Anchoring</h4>
                                <p class="text-sm text-on-surface-variant leading-relaxed">Привязка к контексту: запрет на фантазии, строгая опора на ваши факты.</p>
                            </div>
                            <div class="bg-surface-container-highest p-6 rounded-2xl border border-black/5 hover:border-primary/30 transition-all hover:-translate-y-1 group">
                                <h4 class="font-headline font-black text-lg mb-2 group-hover:text-primary transition-colors">Self-Correction & Verification</h4>
                                <p class="text-sm text-on-surface-variant leading-relaxed">ИИ сам критикует свой черновик и придумывает к нему проверочные вопросы.</p>
                            </div>
                            <div class="bg-surface-container-highest p-6 rounded-2xl border border-black/5 relative overflow-hidden group">
                                <div class="absolute top-0 right-0 w-16 h-16 bg-primary/10 rounded-bl-full flex items-start justify-end p-3"><span class="text-primary text-xs font-black">PRO</span></div>
                                <h4 class="font-headline font-black text-lg mb-2 group-hover:text-primary transition-colors">RAG (Retrieval-Augmented)</h4>
                                <p class="text-sm text-on-surface-variant leading-relaxed">Подключение вашей базы знаний. ИИ ищет ответы по вашей документации.</p>
                            </div>
                        </div>
                    </div>
                    
                    <!-- ГРУППА 3 -->
                    <div>
                        <h3 class="text-[10px] font-black text-primary uppercase tracking-[0.2em] mb-6 flex items-center gap-2"><span class="material-symbols-outlined text-lg">workspace_premium</span> Стабильные результаты</h3>
                        <div class="space-y-4">
                            <div class="bg-primary p-6 rounded-2xl shadow-lg hover:-translate-y-1 transition-transform relative text-white group">
                                <div class="absolute -top-3 left-4 bg-white text-primary px-3 py-1 rounded-full text-[9px] font-black tracking-widest uppercase shadow">Авторское</div>
                                <h4 class="font-headline font-black text-lg mb-2 mt-2">Совет 3 Моделей</h4>
                                <p class="text-sm text-white/80 leading-relaxed">Одну задачу проверяют три разных ИИ-модели. Результат — перекрёстно валидированный консенсус.</p>
                            </div>
                            <div class="bg-surface-container-highest p-6 rounded-2xl border border-black/5 hover:border-primary/30 transition-all hover:-translate-y-1 group">
                                <h4 class="font-headline font-black text-lg mb-2 group-hover:text-primary transition-colors">Управление памятью</h4>
                                <p class="text-sm text-on-surface-variant leading-relaxed">Как сохранять контекст в длинных сессиях: сжатие и структурирование.</p>
                            </div>
                            <div class="bg-surface-container-highest p-6 rounded-2xl border border-black/5 hover:border-primary/30 transition-all hover:-translate-y-1 group">
                                <h4 class="font-headline font-black text-lg mb-2 group-hover:text-primary transition-colors">Диагностика системы</h4>
                                <p class="text-sm text-on-surface-variant leading-relaxed">Маркеры деградации модели и чек-листы восстановления качества ответов.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
"""
# Insert methodology before FAQ
idx = idx.replace('<!-- FAQ Section -->', methodology + '\n        <!-- FAQ Section -->')

# Add new FAQs
new_faqs = """
                    <details class="bg-surface rounded-2xl p-6 group cursor-pointer border border-black/5 [&_summary::-webkit-details-marker]:hidden">
                        <summary class="flex justify-between items-center font-headline font-black focus:outline-none">
                            Что такое "Совет 3 Моделей"?
                            <span class="material-symbols-outlined transition-transform group-open:rotate-180 text-primary">expand_more</span>
                        </summary>
                        <p class="mt-4 text-on-surface-variant leading-relaxed font-light">Это авторская методика, при которой одну задачу проверяют три разных ИИ-модели. Вместо слепого доверия одной нейросети, вы получаете консенсус, проверенный перекрёстной валидацией. Это радикально снижает количество ошибок и галлюцинаций.</p>
                    </details>
                    <details class="bg-surface rounded-2xl p-6 group cursor-pointer border border-black/5 [&_summary::-webkit-details-marker]:hidden">
                        <summary class="flex justify-between items-center font-headline font-black focus:outline-none">
                            Мне нужно знать, что такое RAG и Chain-of-Thought до курса?
                            <span class="material-symbols-outlined transition-transform group-open:rotate-180 text-primary">expand_more</span>
                        </summary>
                        <p class="mt-4 text-on-surface-variant leading-relaxed font-light">Не сейчас. На курсе мы учим этим методикам с нуля — простым языком, на практических примерах. Вы будете применять их, даже не замечая — как водитель не думает о физике двигателя, но ведёт машину.</p>
                    </details>
"""
# Insert after `<div class="space-y-4">` in FAQ
idx = idx.replace('<div class="space-y-4">\n                    <details', '<div class="space-y-4">\n' + new_faqs + '\n                    <details')

with open('c:\\UFA\\index.html', 'w', encoding='utf-8') as f:
    f.write(idx)


# ----------------- #
#  PROCESS CASES.HTML
# ----------------- #
with open('c:\\UFA\\cases.html', 'r', encoding='utf-8') as f:
    cs = f.read()

cs = update_footer(cs)
cs = update_nav(cs)
cs = cs.replace('<a class="text-on-surface/70 hover:text-primary transition-all duration-300" href="cases.html">КЕЙСЫ</a>', '<a class="text-primary border-b-2 border-primary pb-1" href="cases.html">КЕЙСЫ</a>', 1)
cs = cs.replace('<a class="flex flex-col items-center gap-1 text-on-surface/60 hover:text-primary transition-colors" href="cases.html">', '<a class="flex flex-col items-center gap-1 text-primary" href="cases.html">', 1)

with open('c:\\UFA\\cases.html', 'w', encoding='utf-8') as f:
    f.write(cs)


# ----------------- #
#  PROCESS ABOUT.HTML
# ----------------- #
with open('c:\\UFA\\about.html', 'r', encoding='utf-8') as f:
    ab = f.read()

ab = update_footer(ab)
ab = update_nav(ab)
ab = ab.replace('<a class="text-on-surface/70 hover:text-primary transition-all duration-300" href="about.html">АВТОР</a>', '<a class="text-primary border-b-2 border-primary pb-1" href="about.html">АВТОР</a>', 1)
ab = ab.replace('<a class="flex flex-col items-center gap-1 text-on-surface/60 hover:text-primary transition-colors" href="about.html">', '<a class="flex flex-col items-center gap-1 text-primary" href="about.html">', 1)

# Add photo comment
ab = ab.replace('<img src="https://placehold.co/800x1067/e8e2d9/191c1e?font=Montserrat&text=AUTHOR+PHOTO"', '<!-- REPLACE_WITH_YOUR_PHOTO --><img src="https://placehold.co/800x1067/e8e2d9/191c1e?font=Montserrat&text=AUTHOR+PHOTO"')

with open('c:\\UFA\\about.html', 'w', encoding='utf-8') as f:
    f.write(ab)

print("Patch applied successfully.")
