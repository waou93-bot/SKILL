---
name: svelte-data-tables
description: Design or implement Svelte 5 data-table experiences with SV Table and TanStack Table, including filters, sorting, selection, pagination, bulk actions, exports, and states. Use for data-heavy Svelte interfaces, not ordinary static tables.
---

# Svelte Data Tables

Use [SV Table](https://sv-table.vercel.app/) as a source of focused components and examples, while keeping the application data model authoritative.

## Model the behavior first

Determine which state is client-side and which is server-driven: sorting, filters, search, pagination, row selection, and column visibility. For server-driven tables, make the URL or a documented store the canonical state and cancel or supersede stale requests.

Define stable row identifiers before selection or bulk actions. Decide whether selection spans only the visible page or the full filtered result set, and make that scope explicit in the UI.

## Integration workflow

1. Inspect the project's Svelte version, current TanStack Table package, shadcn-svelte setup, and data-fetching pattern.
2. Verify SV Table's current compatibility and registry instructions. Its documentation may target a changing TanStack version, so never upgrade the application's table stack implicitly.
3. Select the smallest necessary pieces: filters, headers, pagination, selection, actions, loading/empty states, export, or a complete example.
4. Adapt copied components to the project's types and state ownership instead of preserving demo data shapes.
5. Cover loading, empty, no-results, partial-error, and retry states without changing column geometry unnecessarily.

## Quality requirements

- Keep native table semantics when the layout is genuinely tabular. Label selection controls and action menus with row context.
- Provide keyboard-reachable sorting, filtering, pagination, and menus with visible focus states.
- Avoid rendering unbounded datasets; choose pagination or virtualization based on measured scale.
- For CSV export, define whether the export contains the page, current filtered result, selection, or full dataset. Generate large exports server-side and prevent hidden or unauthorized fields from leaking.
- Test deterministic sorting, locale-sensitive formatting, time zones, null values, long content, narrow screens, and repeated actions.
