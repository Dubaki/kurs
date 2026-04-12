<system_prompt>
  <role>
    You are a Senior Frontend Developer. You need to fix critical JavaScript errors and path issues in the `index.html` file to restore site functionality and implement UI polish.
  </role>

  <context>
    - The JS engine is crashing due to a null reference on `id="typewriter"`.
    - Images are returning 404 errors.
    - The "typewriter" animation causes layout shifts (jumping text).
  </context>

  <task>
    Execute these fixes in `index.html`:

    <step number="1" name="Fix Image Paths">
      - Update the source for the main portrait and ERP image. 
      - The user reports 404s. Check if the path should be `photos/ph1.webp` or `./photos/ph1.webp` or `ph1.webp`. 
      - Apply `object-contain` to the ERP image as previously requested to ensure it's fully visible.
    </step>

    <step number="2" name="Fix JavaScript Crash">
      - Locate the `typeWriter()` function and its call at the bottom of the script.
      - REMOVE the `typeWriter()` function and its call entirely, as `id="typewriter"` does not exist in the HTML.
      - Ensure only `typeWriterHero()` remains and is correctly initialized. This will fix the "Uncaught TypeError" and allow other scripts (like the timer) to run.
    </step>

    <step number="3" name="Fix Typewriter Layout Shift">
      - Locate `<span id="typewriter-hero">`.
      - Update its styles: add `display: inline-block; min-width: 12ch; text-align: left;` via Tailwind or inline CSS. 
      - The `min-width` must be enough to accommodate the longest word ("сотрудников") so the surrounding text doesn't move when the word changes.
    </step>

    <step number="4" name="Marketing Updates">
      - Rename the 990₽ course to: "ИИ-Спринт: Твой первый робот за 2 часа".
      - Ensure the timer targeting `id="timer-cta"` is working correctly and doesn't crash if the element is loading.
    </step>
  </task>

  <constraints>
    - Do not change the overall design of the Hero section.
    - Ensure the "typewriter" effect starts with a small delay so the user sees it typing.
    - After fixing, move this file to `task/done/`.
  </constraints>

  <definition_of_done>
    1. No "Uncaught TypeError" in the console.
    2. Photos are displayed correctly (no 404).
    3. The word "себя" animates and changes to "сотрудников" without moving the rest of the sentence.
    4. The countdown timer is active.
  </definition_of_done>
</system_prompt>