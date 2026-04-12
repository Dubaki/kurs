<system_prompt>
  <role>
    You are a Senior Frontend Developer. Your task is to refine the logo animation to be more subtle and fix the text alignment in the Promo block.
  </role>

  <context>
    - Project: VibeCraft.
    - Files: `index.html`, `cases.html`, `blog.html`, `about.html`.
    - Goal: Minimalist "V" icon morphing and precise 2-line text for the Promo block.
  </context>

  <task>
    <step number="1" target="index.html">
      <action>Finalize Promo Block Text Layout</action>
      <details>
        - Ensure the Royal Blue block has two lines of centered text.
        - Line 1: "Твой бот за 2 часа" (Remove all dashes).
        - Line 2: "ЖМИ!" (Bold, centered).
        - Use `flex flex-col items-center justify-center` for perfect alignment.
      </details>
    </step>

    <step number="2" target="All Files">
      <action>Refine "V" Icon Animation (Logo)</action>
      <details>
        - Target ONLY the square icon container and the letter "V" inside it.
        - **DO NOT** animate the text "VibeCraft".
        - Define a CSS animation `v-morph`:
          - **Start (0%):** Container is `bg-primary` (solid), corners have default small rounding, letter "V" is white.
          - **Middle (50%):** Container's `border-radius` changes to `50%` (circle), background becomes transparent/white with a thin `border-primary`, and the letter "V" itself changes color to Royal Blue (`#1e40af`).
          - **End (100%):** Returns to the start state.
        - Apply this to the icon part of the logo only. The animation should be slow and smooth (5-6 seconds).
      </details>
    </step>

    <step number="3" target="File System">
      <action>Cleanup</action>
      <details>- Move this task to /done.</details>
    </step>
  </task>

  <constraints>
    <rule>Only the "V" icon morphs; the "VibeCraft" text remains static.</rule>
    <rule>The letter "V" must change color from White to Royal Blue (#1e40af) and back.</rule>
    <rule>Use only vanilla CSS for the animation.</rule>
  </constraints>

  <definition_of_done>
    1. Promo block text is neatly split into 2 centered lines.
    2. Only the "V" icon container and the letter "V" animate (morphing shape and color).
    3. The rest of the header remains unchanged.
    4. Task file moved to /done.
  </definition_of_done>
</system_prompt>