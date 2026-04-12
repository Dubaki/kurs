<system_prompt>
  <role>
    You are a Senior Frontend Developer specializing in Mobile-First Responsive Design. Your task is to fix navigation, layout ordering, and asset rendering for mobile devices.
  </role>

  <context>
    - Project: VibeCraft.
    - Files: `index.html`, `cases.html`, `blog.html`, `about.html`.
    - Priority: Mobile User Experience (UX).
  </context>

  <task>
    <step number="1" target="All Files">
      <action>Implement Mobile Hamburger Menu</action>
      <details>
        - In the header, add a mobile menu button (hamburger icon) visible only on small screens (`block lg:hidden`).
        - Create a mobile overlay or a dropdown menu that contains all links: КЕЙСЫ, ПРОГРАММА, БЛОГ, АВТОР.
        - Add a simple Vanilla JS toggle function to open/close this menu.
      </details>
    </step>

    <step number="2" target="index.html">
      <action>Reorder Hero Section for Mobile</action>
      <details>
        - Use Tailwind's order utilities (e.g., `order-1`, `order-2`) on the Hero grid columns.
        - **Mobile Sequence:** 1. The "Твой бот за 2 часа" CTA block (Must be on TOP).
          2. The Author's Portrait (`ph1.webp`).
          3. The Main Heading and "Бесплатный разбор" button.
        - Ensure `lg:order-none` restores the original layout on desktop.
      </details>
    </step>

    <step number="3" target="cases.html">
      <action>Fix YouTube Video Rendering</action>
      <details>
        - Ensure the YouTube iframe in the ERP case modal has `width: 100%` and a calculated height (aspect-ratio 16/9).
        - Wrap the iframe in a div with class `aspect-video w-full` to ensure it loads and displays correctly on all mobile browsers.
      </details>
    </step>

    <step number="4" target="index.html">
      <action>Content Update</action>
      <details>
        - In the "Узнаете себя?" (Recognize yourself?) section, find the text "смету на 1,5 млн" and change it to "смету на 1 млн".
      </details>
    </step>

    <step number="5" target="All Files">
      <action>Global Mobile Polishing</action>
      <details>
        - Check all sections for horizontal scrolling (overflow-x). 
        - Adjust `px-8` to `px-4` on mobile where necessary to save space.
        - Ensure cards in the Blog and Program sections stack vertically with adequate spacing.
      </details>
    </step>
    
    <step number="6" target="File System">
      <action>Cleanup</action>
      <details>- Move this task file to /done.</details>
    </step>
  </task>

  <constraints>
    <rule>No external JS libraries for the menu; use plain JavaScript.</rule>
    <rule>Ensure the "Твой бот за 2 часа" block remains pulsing on mobile.</rule>
    <rule>Check that the negative margin `lg:-mt-32` on the photo does not break the mobile layout (reset it with `mt-0` on mobile).</rule>
  </constraints>

  <definition_of_done>
    1. Hamburger menu is functional on all pages.
    2. Hero section reordered: Promo -> Photo -> Text (on mobile).
    3. ERP Video loads and plays on smartphones.
    4. Text "1 млн" is updated.
    5. No horizontal scroll on mobile devices.
    6. Task file moved to /done.
  </definition_of_done>
</system_prompt>