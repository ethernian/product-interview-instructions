# Product Interview Instructions

Instructions for ChatGPT Projects that conduct a Q&A interview about the project to be built and collect the user's answers. It creates a Q&A list defining the new product.

Planned: Preliminary Architecture Outlines (PAO) that reflect the current understanding of the product architecture and help guide the interview questions.

On request, the assistant compiles a structured product definition from confirmed user input, and the Preliminary Architecture Outlines, if available, highlighting open questions and conflicts.

---
## Delivery artifacts

[`src/`](src/) contains the interview instructions, aspect catalog and UX guide. Add all files from this folder to your ChatGPT project sources, then use the setup text below as the Project instructions.

## Getting started guide

1. In ChatGPT, create a new project or open the project you want to use for product definition.
2. Add **all files from [`src/`](src/)** to the project's sources, keeping their filenames unchanged. This includes `Product-Interview-Instructions.md`, `Product-Definition-Aspects-EN.md` and `UX-Guide.md`.
3. Open the project's menu and find its settings or instructions editor (the label may vary by interface).
4. Paste the text below into **Project instructions** and save your changes.
5. Start a new chat inside that project and describe your product idea to begin the Q&A interview.

### ChatGPT Project instructions

```text
Before starting a product-definition interview, read and follow Product-Interview-Instructions.md from the project files.

Read and apply the supporting documents it references, including Product-Definition-Aspects-EN.md and UX-Guide.md. Use these instructions consistently throughout the interview.

If a required file is missing or unreadable, tell the user which file is unavailable and ask for it. Do not invent its contents or claim to have followed it.

Treat the user's explicit decisions as authoritative. Never treat suggested answers, inferences or assumptions as confirmed decisions without the user's confirmation.
```

Project instructions apply across chats within that project. See the [official ChatGPT Projects guide](https://learn.chatgpt.com/docs/projects) for more information.

## Repository guide

| File | Purpose |
| --- | --- |
| [`src/Product-Interview-Instructions.md`](src/Product-Interview-Instructions.md) | Interview rules to upload as a project source. |
| [`src/Product-Definition-Aspects-EN.md`](src/Product-Definition-Aspects-EN.md) | Product definition aspect catalog to upload as a project source. |
| [`src/UX-Guide.md`](src/UX-Guide.md) | Interview presentation and interaction rules to upload as a project source. |
| [`README.md`](README.md) | Project overview and getting started guide. |
| [`TODO.md`](TODO.md) | Planned improvements and outstanding tasks. |
| [`HISTORY.md`](HISTORY.md) | Record of project changes and milestones. |
| [`VERSION`](VERSION) | Current semantic version. |

## Contribute

Keep prompt changes focused and easy to review. Describe what changed, why it helps, and include an example conversation when useful.

Keep the setup text in this README concise. Maintain the detailed interview rules and supporting guides in `src/`, and update the project sources when those files change.
