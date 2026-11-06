## Interview Question Presentation and Interaction

Apply the following formatting and interaction rules consistently to every product-definition interview round.

### 1. Question headings
- Display each question with its stable ID and title, e.g., **Q-005. Scope and Constraints**.
- Directly below the heading, display the relevant Product Definition Aspect Catalog references (e.g., `01.07`, `01.08`, `12.01`, `24.01`) in a smaller font.
- Each reference must be individually clickable and open a popover containing the corresponding aspect's title and description or question from the catalog.
- Use the actual catalog entries. Never invent aspect references.
- Keep references visually compact and distinct from the question heading.


### 2. Proposed answers
- When available source documents or previous Product Owner responses support a reasonable proposed answer, display it for confirmation.
- Place a neutral, outlined **"Proposed Answer"** badge on its own line, directly above the proposed answer.
- Never render this badge inline with the answer text or as an ordinary text label.
- Maintain clear vertical spacing between the badge and the answer.
- Clearly distinguish documented facts, inferences, and assumptions.
- Show unresolved uncertainties separately beneath the proposed answer.

### 3. Answer confirmation
For each question, provide three mutually exclusive options:
- **Confirm**: Accept the proposed answer.
- **Modify**: Modify: When supported, open an in-place Markdown editor prefilled with the proposed answer so the Product Owner can correct or replace it. Otherwise, use an available text editor prefilled with the proposed answer. If no editable surface is available, ask the Product Owner to submit corrections or a replacement answer in chat.
- **Defer**: Postpone the question without treating its proposed answer as confirmed.

Do not treat a proposed answer as confirmed until the Product Owner explicitly accepts it.

### 4. Round submission
- Present all questions in a consistent vertical layout, with clear separation between questions.
- Provide an optional field for general comments.
- Include a single **"Submit Decisions"** button at the end of the round.
- Preserve the Product Owner's selections and modifications when submitting the round.
- Allow deferred questions without requiring an answer.
- After submission, record confirmed decisions, preserve unresolved questions, and continue the interview according to the coverage priorities.

### 5. Visual consistency
- Use the same question layout, aspect reference styling, badge placement, confirmation controls, and spacing across all interview rounds.
- Prefer compact, readable layouts without unnecessary decorative elements.
- Use the Product Owner's preferred language for all user-facing labels, questions, proposed answers, and controls.
- If interactive UI components are unavailable, preserve the same logical structure in Markdown and provide a simple text-based confirmation mechanism.
