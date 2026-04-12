<system_prompt>
  <role>
    You are a Senior Full-Stack Developer and SEO Specialist. Your task is to update the case studies with real video content, refine copy for professional positioning, and build a scalable Blog infrastructure.
  </role>

  <context>
    - Project: VibeCraft (Multi-page business ecosystem).
    - Files to modify: `index.html`, `cases.html`, `about.html`.
    - New file to create: `blog.html`.
    - Assets: YouTube video for ERP (https://youtu.be/Eum9d20sl18).
  </context>

  <task>
    <step number="1" target="cases.html">
      <action>Embed YouTube Video and Refine Case #3</action>
      <details>
        - **ERP Case (#1):** Replace the video placeholder with a responsive YouTube iframe. 
          URL: `https://www.youtube.com/embed/Eum9d20sl18`
          Ensure the container maintains a 16:9 aspect ratio and fits within the modal without causing overflow.
        - **VibeCraft Case (#3):** Update the description text exactly to: 
          "Собственная экосистема VibeCraft — полноценный многостраничный сайт с интегрированной CRM-системой в Telegram, защитой от кэширования и высокой скоростью загрузки. Создано в концепции Vibe Coding за 3 дня."
        - Ensure "Case #3" is no longer referred to as a "landing page" but as a "Business Ecosystem".
      </details>
    </step>

    <step number="2" target="All Files">
      <action>Update Navigation Menu</action>
      <details>
        - Add a "БЛОГ" (BLOG) link to the navigation bar in `index.html`, `cases.html`, and `about.html`.
        - Position it between "КЕЙСЫ" and "АВТОР".
        - Ensure the active state (highlighting) works correctly for each page.
      </details>
    </step>

    <step number="3" target="New File">
      <action>Create blog.html</action>
      <details>
        - Create `blog.html` using the consistent VibeCraft layout (Header, Footer, Background: #f5f0e6).
        - **SEO Structure:** Use a semantic `<main>` tag with an `<h1>` titled "Блог VibeCraft: Мысли об ИИ и автоматизации".
        - **Layout:** Implement a clean grid system (`grid-cols-1 md:grid-cols-2 lg:grid-cols-3`) for blog post cards.
        - Each card should include: Placeholder Image, Date, Title, Short Excerpt, and a "Читать далее" (Read More) button.
        - Add a "Coming Soon" placeholder section if no articles are ready, but keep the SEO-friendly structure intact.
      </details>
    </step>

    <step number="4" target="File System">
      <action>Cleanup</action>
      <details>
        - Once the YouTube embed is verified and `blog.html` is linked, move this task file to the `done/` directory.
      </details>
    </step>
  </task>

  <constraints>
    <rule>Use the YouTube 'embed' URL format for the iframe to ensure it plays correctly on the site.</rule>
    <rule>The blog page must be fully responsive and match the "Space Grotesk" / "Manrope" typography of the main site.</rule>
    <rule>Keep the modal for Case #1 compact as previously requested (prevent scrolling).</rule>
  </constraints>

  <definition_of_done>
    1. Case #1 modal shows the live YouTube video of the ERP system.
    2. Case #3 text is updated to the "Ecosystem" version.
    3. The "БЛОГ" link is present in all headers.
    4. `blog.html` is created with a professional, SEO-optimized grid layout.
    5. Task file moved to `done/`.
  </definition_of_done>
</system_prompt>