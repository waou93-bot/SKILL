# HyperFrames skill maintenance

The installed CLI version is 0.7.64. Read the existing local skills first, including general-video, motion-graphics, product-launch-video and the domain skills. Local workflows preserve Design DNA, project briefs, review gates and companion flows. A branch-default catalog can differ from the release for the installed CLI.

For scaffolding with 0.7.64, set the environment variable `HYPERFRAMES_SKIP_SKILLS=1` before `hyperframes init`. For example, in PowerShell use `$env:HYPERFRAMES_SKIP_SKILLS = '1'` for the command's session.

For maintenance or a missing workflow:

1. Check the actual CLI and project pin. Use the bundled references or the corresponding [release tag](https://github.com/heygen-com/hyperframes/tree/v0.7.64/skills).
2. Stage the selected workflow and dependencies outside installed catalogs and compare against both local copies. Preserve locally adapted routing, Design DNA blocks, scripts, and references.
3. Back up and merge the selected changes. Check links, commands and cross-workflow references before relying on them.
4. If a workflow is unavailable for that release, explain the limitation and use an installed route only when it covers the deliverable.

The 0.7.64 updater can prune unpublished skills and can refresh dependencies even for named updates. Use a staged merge for this customized installation.
