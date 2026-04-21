# Design Rationale: Daily Reflection Tree

## 1. Psychological Grounding & Question Design
The tree's questions were designed to bypass the user's intellectual defenses. Instead of asking conceptual questions (e.g., "Do you feel entitled?"), the tree asks behavioral questions (e.g., "When you interacted with colleagues today, what was the underlying transaction?"). 

* **Axis 1 (Locus of Control):** Grounded in Julian Rotter's social learning theory. The questions assess whether the user perceives events as contingent upon their own behavior (Victor/Internal) or upon luck, fate, and others (Victim/External).
* **Axis 2 (Orientation):** Informed by Adlerian psychology and organizational citizenship behavior. Entitlement is framed not as malice, but as a transactional focus on extraction, while contribution is framed as a focus on systemic value creation.
* **Axis 3 (Radius of Concern):** Draws from Abraham Maslow's later work on self-transcendence and Kohlberg's stages of moral development. The options force the user to identify the actual scope of their decision-making (Me vs. Team vs. Organization).

## 2. Branching and Trade-Offs
The primary architectural trade-off was between nuance and determinism. 
* **The Trade-off:** Instead of routing users to 8 unique nodes per axis based on every possible permutation of answers, I implemented a "Signal Tally" system. Each answer contributes to a dominant state (e.g., `locus:victor`). The Decision nodes route based on the majority signal (>= 2 out of 3).
* **The Benefit:** This ensures strict determinism, makes the data structure auditable, and prevents combinatorial explosion, while still providing a highly personalized reflection at the end of each axis.

## 3. Designing for Non-Moralizing Reframing
A key constraint was ensuring the tool acts as a "wise colleague" rather than a judge. When a user lands on the "Victim" or "Ego" branches, the language validates their feelings before offering a reframe (e.g., *"It's normal to feel constrained, but remember: you always retain the power to choose your response..."*). This reduces cognitive dissonance and prevents the user from feeling shamed.

## 4. Future Improvements
With more time, I would implement **Cross-Axis Synthesis Nodes**. Currently, the axes are evaluated in isolation. Ideally, the system would recognize meta-patterns—for example, if a user scores high in "Victor" (Agency) but high in "Egocentric" (Self-focus), the final summary would adapt to address that specific "Mercenary" persona.
