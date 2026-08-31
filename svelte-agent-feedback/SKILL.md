---
name: svelte-agent-feedback
description: Integrate or operate sv-agentation in a SvelteKit development workflow so visual annotations become structured prompts for coding agents. Use for in-browser UI review and agent handoff; never enable it in production.
---

# Svelte Agent Feedback

[sv-agentation](https://sv-agentation.com/) is a development-only inspector that captures element, text-range, grouped, and area annotations and exports structured context for coding agents.

## Integration boundary

Install the current `sv-agentation` package only after checking its release notes and Svelte compatibility. Mount it behind both browser and development guards:

```svelte
<script lang="ts">
  import { browser, dev } from '$app/environment';
  import { Agentation } from 'sv-agentation';
</script>

{#if browser && dev}
  <Agentation />
{/if}
```

Confirm that production builds tree-shake or exclude the tool. Never weaken the guard to make a preview convenient, and do not expose absolute workspace paths in production output.

## Review workflow

1. Reproduce the UI at the relevant route, viewport, theme, and data state.
2. Annotate the smallest element or text range that identifies the problem. Group elements only when one instruction applies to the entire group.
3. Write observable desired outcomes, not vague taste judgments. Include responsive or interaction conditions when they matter.
4. Choose compact output for obvious fixes, detailed output for multi-element changes, and forensic output only when computed styles or deeper DOM context are needed.
5. Give the exported prompt to the coding agent, implement the change, then re-open the same state and verify the annotation's acceptance condition.

## Privacy and safety

Annotations and forensic exports can include visible text, DOM context, computed styles, selectors, and source locations. Do not capture credentials, personal data, private customer content, or confidential paths in a prompt destined for an external service. Prefer callbacks with `copyToClipboard={false}` when the host application needs controlled handling of exported payloads.

Keep direct open-in-editor behavior opt-in and validate `workspaceRoot`; editor links should resolve only inside the intended project.
