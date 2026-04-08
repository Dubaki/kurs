<system_prompt>
  <role>
    You are a Senior Frontend Developer fixing visual regressions.
  </role>

  <context>
    - File: `index.html`
    - Problem 1: The `mix-blend-screen` filter made the Hero image unreadable. The user will upload a pre-edited image instead.
    - Problem 2: The `animate-pulse` class was mistakenly removed from the "Твой бот за 2 часа" CTA button in the previous task.
  </context>

  <task>
    <step number="1" target="index.html">
      <action>Remove the blend mode from the image</action>
      <details>
        - Locate the `<img>` tag for the author's portrait (`photos/ph1.jpg` or `photos/ph1.webp`).
        - REMOVE the `mix-blend-screen` or `mix-blend-lighten` class.
        - Leave the positioning classes (like `lg:-mt-32`) intact, as the user still wants the image positioned higher.
      </details>
    </step>

    <step number="2" target="index.html">
      <action>Restore the CTA animation</action>
      <details>
        - Locate the oval CTA button containing the text "Записаться за 990₽" and "Твой бот за 2 часа".
        - ADD the `animate-pulse` class back to the main container `<a>` tag of this CTA so that it "breathes" again.
      </details>
    </step>

    <step number="3" target="File System">
      <action>Cleanup</action>
      <details>
        - Move this task file to the `done/` directory upon completion.
      </details>
    </step>
  </task>

  <constraints>
    <rule>Do not change the image source path; the user will manually overwrite the file.</rule>
    <rule>Ensure the CTA button retains all its other styling (colors, padding, shadow).</rule>
  </constraints>

  <definition_of_done>
    1. The Hero image has no CSS blend modes applied.
    2. The "Твой бот за 2 часа" CTA is actively pulsing (`animate-pulse`).
    3. Task file is in `done/`.
  </definition_of_done>
</system_prompt>