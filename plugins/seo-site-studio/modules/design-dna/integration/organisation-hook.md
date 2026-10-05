# Organisation -> Design DNA Hook

Use this rule inside the Organisation router.

## Trigger

If a task creates, modifies, audits or implements any visible product surface, route through `design-dna` before production.

Includes:

- website;
- landing page;
- app;
- desktop software;
- mobile UI;
- SaaS/dashboard;
- hybrid interface;
- portfolio;
- interactive experience;
- visual redesign;
- component styling;
- motion, imagery or art direction.

## Route

```text
TASK
  -> Organisation
  -> Design DNA context load
  -> PROJECT_SKIN create/update
  -> concept/composition decision
  -> implementation route (Luna/Terra/Sol/Astra as appropriate)
  -> Anti-Slop Gate
  -> Design Quality Gate
  -> user validation when required
```

## Responsibilities

### Organisation

- detect that the task has a visual surface;
- require Design DNA;
- preserve project context;
- prevent a production agent from inventing a generic art direction.

### Design DNA

- keep the stable core;
- define or update the project skin;
- establish typography, composition, imagery, motion and exclusions;
- reject generic template patterns.

### Production agent

- implement the skin faithfully;
- do not replace the project's visual idea with framework defaults;
- preserve approved existing assets/motion unless explicitly asked to change them.

### Validation

A task is not complete until both functional and visual gates pass.
