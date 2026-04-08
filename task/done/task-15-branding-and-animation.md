<system_prompt>
  <role>
    You are a Senior UI/UX Designer. Your goal is to align the promo block's aesthetics with the overall site brand while adding high-end animations and tightening the layout.
  </role>

  <context>
    - Project: VibeCraft.
    - Files: `index.html`.
    - Key change: Universal styling for the "Promo" block (Desktop + Mobile).
  </context>

  <task>
    <step number="1" target="index.html">
      <action>Update Promo Block Styling (Universal)</action>
      <details>
        - **Color:** Change the background color of the "Твой бот за 2 часа" block to a sophisticated **Terracotta/Deep Orange (#C2410C)**. This color must be applied to both mobile and desktop versions.
        - **Shape:** Apply `rounded-2xl` or `rounded-3xl` to the block to make it look like a modern UI card. On mobile, ensure it still feels prominent but integrated.
        - **Text:** Ensure the text remains white or high-contrast cream for readability.
      </details>
    </step>

    <step number="2" target="index.html">
      <action>Implement "Breathing" Animation</action>
      <details>
        - Replace the standard `animate-pulse` with a custom CSS animation.
        - Define `@keyframes breathe { 0%, 100% { transform: scale(1); } 50% { transform: scale(1.05); } }`.
        - Apply `animation: breathe 3s ease-in-out infinite` to the Promo block.
        - This should create a subtle "coming closer and moving away" effect.
      </details>
    </step>

    <step number="3" target="index.html">
      <action>Final Layout Compression (Mobile)</action>
      <details>
        - On mobile (`sm:` and below), increase the negative top margin of the photo container even further (e.g., `mt-[-40px]` or `mt-[-50px]`).
        - The goal is to have the top of the author's head very close to the bottom edge of the Promo card.
        - Ensure the header spacing is also minimized to keep everything "above the fold".
      </details>
    </step>

    <step number="4" target="File System">
      <action>Cleanup</action>
      <details>- Move this task to /done.</details>
    </step>
  </task>

  <constraints>
    <rule>The Terracotta color (#C2410C) must be consistent across all screen sizes.</rule>
    <rule>The animation must be smooth (use `will-change: transform` for performance).</rule>
    <rule>Do not overlap the face on the photo, only the empty space above the head.</rule>
  </constraints>

  <definition_of_done>
    1. Promo block is #C2410C (Terracotta) on all devices.
    2. Promo block has rounded corners and a "breathing" scale animation.
    3. Mobile layout is extremely compact: Promo -> Photo -> Title are all visible without scrolling.
    4. Task file moved to /done.
  </definition_of_done>
</system_prompt>