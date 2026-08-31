# `/brain` usage

The skill should trigger automatically for substantive analysis and decision work. The user can also invoke it explicitly with `/brain`.

## Should trigger

- `/brain Compare these two vendor offers and tell me which is cheaper over 12 months. Include setup fees and flag anything you cannot verify.`
- “Review this contract excerpt for termination, liability, and IP ownership. Tell me what is certain and what needs the full agreement.”
- “Can you calculate the growth rate from these figures and double-check the math?”
- “I need a recommendation between these two plans before I forward the answer to my CFO.”
- “What is the current price and version of this tool?”

## Should not trigger by itself

- “Translate this one sentence into French.”
- “Make this paragraph friendlier without changing its facts.”

These simple requests can still trigger Brain when the user asks for factual verification, a decision, multiple deliverables, or high-stakes content.

## Expected response shape

Answer first. Then give the shortest supporting path. End with a compact risks/assumptions block. Use `Likely:`, `Assuming:`, and `Unknown:` exactly where uncertainty exists; do not turn verified facts into hedges.

