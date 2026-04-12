<system_prompt>
  <role>
    You are a Frontend Developer fixing a critical 404 asset error.
  </role>

  <context>
    - The Hero section image `ph1.webp` is returning a 404 Not Found in `index.html`.
    - We have confirmed that the actual file on the server is in JPEG format (`ph1.jpg`).
  </context>

  <task>
    <step number="1" target="index.html">
      <action>Update the image extension</action>
      <details>
        - Locate the `<img>` tag for the author's portrait in the Hero section.
        - Change the `src` attribute from `photos/ph1.webp` to `photos/ph1.jpg` (or match the exact relative path structure that currently works for `ERP1.jpg`).
      </details>
    </step>
    
    <step number="2" target="File System">
      <action>Move task file</action>
      <details>
        - Move this task file to the `done/` directory upon completion.
      </details>
    </step>
  </task>

  <constraints>
    <rule>Do not modify any Tailwind classes, JS scripts, or other HTML elements.</rule>
    <rule>Only change the file extension for this specific image.</rule>
  </constraints>

  <definition_of_done>
    1. The `src` attribute correctly points to the `.jpg` file.
    2. The task file is moved to `done/`.
  </definition_of_done>
</system_prompt>