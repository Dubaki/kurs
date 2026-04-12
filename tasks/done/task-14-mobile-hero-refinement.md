<system_prompt>
  <role>
    You are a Senior UI/UX Designer & Frontend Developer. Your task is to refine the mobile Hero section for maximum conversion and vertical compactness.
  </role>

  <context>
    - Project: VibeCraft.
    - Focus: `index.html` (Mobile view).
    - Goal: Tighten the layout, make the Promo block full-width, and optimize colors.
  </context>

  <task>
    <step number="1" target="index.html">
      <action>Re-style the "Твой бот за 2 часа" Promo Block</action>
      <details>
        - **Width:** On mobile, remove the rounded-full/oval shape or make it `w-full` with very slight rounding at the bottom. It should span from edge to edge.
        - **Color:** Change the background color to a vibrant Amber/Golden shade (e.g., Tailwind `bg-amber-500` or hex `#f59e0b`).
        - **Content:** Add the text " — ЖМИ!" after the price or main text. Ensure the "pulse" animation remains active.
        - **Spacing:** Remove any top margin (`mt-0`) so it sits directly under the Header.
      </details>
    </step>

    <step number="2" target="index.html">
      <action>Positioning of Photo and Promo (Mobile)</action>
      <details>
        - **Photo:** On mobile, apply a negative top margin (e.g., `mt-[-20px]`) to the author's portrait container so it visually "tucks" under the full-width Promo block.
        - **Safety:** Ensure the Promo block does not cover the author's face. 
        - **Text:** The main heading text and "Free Audit" button should start immediately after the photo with minimal gap.
      </details>
    </step>

    <step number="3" target="index.html">
      <action>Vertical Compression</action>
      <details>
        - Reduce `py-` (padding-vertical) for the entire Hero section on mobile to ensure all key elements (Promo, Photo, Title) are visible on a standard 6.1-inch screen without scrolling.
      </details>
    </step>

    <step number="4" target="File System">
      <action>Cleanup</action>
      <details>- Move this task to /done.</details>
    </step>
  </task>

  <constraints>
    <rule>Keep the Desktop layout unchanged (use `lg:` prefixes for all new mobile overrides).</rule>
    <rule>Ensure the new Amber color provides good contrast for the text (use dark text if necessary).</rule>
  </constraints>

  <definition_of_done>
    1. The Promo block is full-width and Amber-colored on mobile.
    2. "ЖМИ!" call-to-action is added.
    3. The photo is shifted up, overlapping slightly with the promo's bottom edge.
    4. The entire Hero group is compact and fits the mobile viewport.
  </definition_of_done>
</system_prompt>